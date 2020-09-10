"""

RRT* for simulations

Author: Ellie Cho
Editor: Yashwanth Nakka

"""


import math
import os
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from RRT import RRT
from Node import Node

show_animation = True
show_graph = False


class RRTStar(RRT):
    """
    Class for RRT Star planning
    """
    def __init__(self, start, goal, obstacle_list, rand_area, rand_angle, vrange,
                 expand_dis=3.0, path_resolution=0.5, goal_sample_rate=5, max_iter=500,
                 connect_circle_dist=50.0
                 ):
        """
        Setting Parameter
        start:Start Position [x,y,0,0,0,0]
        goal:Goal Position [x,y,0,0,0,0]
        obstacleList:obstacle Positions [[x,y,size],...]
        randArea:Random Sampling Area [min,max]
        """
        self.start = Node([start[0], start[1], 0, 0, 0, 0])
        self.end = Node([goal[0], goal[1], 0, 0, 0, 0])
        self.min_rand = rand_area[0]
        self.max_rand = rand_area[1]
        self.expand_dis = expand_dis
        self.path_resolution = path_resolution
        self.goal_sample_rate = goal_sample_rate
        self.max_iter = max_iter
        self.obstacle_list = obstacle_list
        self.node_list = []
        
        
        self.connect_circle_dist = connect_circle_dist
        self.goal_node = Node([goal[0], goal[1], 0, 0, 0, 0])

    def planning(self, animation=True, search_until_max_iter=True):
        """
        rrt star path planning
        animation: flag for animation on or off
        search_until_max_iter: search until max iteration for path improving or not
        """

        self.node_list = [self.start]
        for i in range(self.max_iter):
            print("Iter:", i, ", number of nodes:", len(self.node_list))
            rnd_node = self.get_random_node()
            nearest_ind = self.get_nearest_node_index(self.node_list, rnd_node)
            nearest_node = self.node_list[nearest_ind]
            new_node = self.steer(nearest_node, rnd_node, self.expand_dis)
            #print("x:", new_node.x[0], "y:", new_node.x[1])
            if self.check_collision(new_node, self.obstacle_list):
                near_inds = self.find_near_nodes(new_node)
                new_node = self.choose_parent(new_node, near_inds)
                if new_node:
                    self.node_list.append(new_node)
                    self.rewire(new_node, near_inds)
                    # print("x:", new_node.x[0], "y:", new_node.x[1])

            if animation and i % 5 == 0:
                self.draw_graph1(rnd_node)

            if (not search_until_max_iter) and new_node:  # check reaching the goal
                last_index = self.search_best_goal_node()
                if last_index:
                    print ("last")
                    return self.generate_final_course(last_index)


        print("reached max iteration")


        last_index = self.search_best_goal_node()
        if last_index:
            print ("last")
            return self.generate_final_course(last_index)

        return None

    def choose_parent(self, new_node, near_inds):
        """
        chooses the parent with minimum cost and returns the node
        
        """


        if not near_inds:
            return None

        # search nearest cost in near_inds
        costs = []
        for i in near_inds:
            near_node = self.node_list[i]
            t_node = self.steer(near_node, new_node)
            if t_node and self.check_collision(t_node, self.obstacle_list):
                costs.append(self.calc_new_cost(near_node, new_node))
            else:
                costs.append(float("inf"))  # the cost of collision node
        min_cost = min(costs)
        # print("min cost:", min_cost)

        if min_cost == float("inf"):
            print("There is no good path.(min_cost is inf)")
            return None

        min_ind = near_inds[costs.index(min_cost)]
        new_node = self.steer(self.node_list[min_ind], new_node)
        new_node.parent = self.node_list[min_ind]
        new_node.cost = min_cost

        return new_node
    def search_best_goal_node(self):
        """
        searches for the goal node with the least cost and returns the index

        """
        dist_to_goal_list = [self.calc_dist_to_goal(n.x[0], n.x[1]) for n in self.node_list]
        goal_inds = [dist_to_goal_list.index(i) for i in dist_to_goal_list if i <= self.expand_dis]

        safe_goal_inds = []
        for goal_ind in goal_inds:
            t_node = self.steer(self.node_list[goal_ind], self.goal_node)
            if self.check_collision(t_node, self.obstacle_list):
                safe_goal_inds.append(goal_ind)

        if not safe_goal_inds:
            return None

        min_cost = min([self.node_list[i].cost for i in safe_goal_inds])
        for i in safe_goal_inds:
            if self.node_list[i].cost == min_cost:
                return i


        return None

    def find_near_nodes(self, new_node):
        """
        finds nodes near the new node
        
        """
        
        nnode = len(self.node_list) + 1
        r = self.connect_circle_dist * math.sqrt((math.log(nnode) / nnode))
        # if expand_dist exists, search vertices in a range no more than expand_dist
        if hasattr(self, 'expand_dis'): 
            r = min(r, self.expand_dis)
        dist_list = [(node.x[0] - new_node.x[0]) ** 2 +
                     (node.x[1] - new_node.x[1]) ** 2 +
                     (node.x[2] - new_node.x[2]) ** 2 for node in self.node_list]
        near_inds = [dist_list.index(i) for i in dist_list if i <= r ** 2]
        return near_inds


    def rewire(self, new_node, near_inds):
        
        
        for i in near_inds:
            near_node = self.node_list[i]
            edge_node = self.steer(new_node, near_node)
            if not edge_node:
                continue
            edge_node.cost = self.calc_new_cost(new_node, near_node)

            no_collision = self.check_collision(edge_node, self.obstacle_list)
            improved_cost = near_node.cost > edge_node.cost

            if no_collision and improved_cost:
                self.node_list[i] = edge_node
                self.propagate_cost_to_leaves(new_node)

    def calc_new_cost(self, from_node, to_node):
        """
        calculates cost from node to node
        
        """

        d, _ = self.calc_distance_and_angle(from_node, to_node)
        # print("d:", d)
        return (from_node.cost + d)

    def propagate_cost_to_leaves(self, parent_node):
        """
        gives cost to nodes in tree
        
        """
        
        for node in self.node_list:
            if node.parent == parent_node:
                node.cost = self.calc_new_cost(parent_node, node)
                self.propagate_cost_to_leaves(node)


def main(gx=8.0, gy=4.0):
    print("Start " + __file__)

    # ====Search Path with RRT====
    obstacleList = [
        (2, 0, 2),
        (7, 0, 2),
        (4, 5, 2)
    ]  # [x, y, radius]

    # Set Initial parameters
    rrt_star = RRTStar(start=[0, 2],
              goal=[gx, gy],
              rand_area=[-2, 15],
              rand_angle=[-3, 3],
              vrange=[0, 5, -.5, .5],
              obstacle_list=obstacleList)
    path = rrt_star.planning(animation=show_animation)

    if path is None:
        print("Cannot find path")
    else:
        print("found path!!")

        # Draw final path
        if show_animation:
            rrt_star.draw_graph1()
            plt.plot([x for (x, y) in path], [y for (x, y) in path], '-r')
            plt.grid(True)
            plt.pause(0.01)  # Need for Mac
            plt.show()
        if show_graph:
            rrt_star.draw_graph2()
            plt.show()


if __name__ == '__main__':
    main()
    





