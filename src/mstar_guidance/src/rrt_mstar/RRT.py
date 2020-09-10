"""
RRT for ROS implementation
Author: Ellie Cho
Editor: Yashwanth Nakka
"""

import copy
import math
import os
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from Node import Node
from numba import jit
import random

show_animation = True
show_graph = False
max_speed = 5
class RRT:
    
    """
    Class for RRT planning
    """

    def __init__(self, start, goal, obstacle_list, rand_area, rand_angle, vrange,
                 expand_dis=3.0, path_resolution=0.5, goal_sample_rate=5, max_iter=500):
        """
        Setting Parameter
        start:Start Position [x,y]
        goal:Goal Position [x,y]
        obstacleList:obstacle Positions [[x,y,size],...]
        randArea:Random Sampling Area [min,max]
        """
        self.start = Node([start[0], start[1], 0, 0, 0, 0])
        self.end = Node([goal[0], goal[1], 0, 0, 0, 0])
        self.min_rand = rand_area[0]
        self.max_rand = rand_area[1]
        """
        self.min_ang = rand_angle[0]
        self.max_ang = rand_angle[1]
        self.min_vel = vrange[0]
        self.max_vel = vrange[1]
        self.min_rot = vrange[2]
        self.max_rot = vrange[3]
        """
        self.expand_dis = expand_dis
        self.path_resolution = path_resolution
        self.goal_sample_rate = goal_sample_rate
        self.max_iter = max_iter
        self.obstacle_list = obstacle_list
        self.node_list = []
    def planning(self, animation=True):
        """
        rrt path planning
        animation: flag for animation on or off
        """

        self.node_list = [self.start]
        for i in range(self.max_iter):
            rnd_node = self.get_random_node()
            nearest_ind = self.get_nearest_node_index(self.node_list, rnd_node)
            nearest_node = self.node_list[nearest_ind]

            new_node = self.steer(nearest_node, rnd_node, self.expand_dis)
            
            if self.check_collision(new_node, self.obstacle_list):
                self.node_list.append(new_node)
            if animation and i % 5 == 0:
                self.draw_graph1(rnd_node)


            if self.calc_dist_to_goal(self.node_list[-1].x[0], self.node_list[-1].x[1]) <= self.expand_dis:
                final_node = self.steer(self.node_list[-1], self.end, self.expand_dis)
                if self.check_collision(final_node, self.obstacle_list):
                    return self.generate_final_course(len(self.node_list) - 1)

            if animation and i % 5:
                self.draw_graph1(rnd_node)



        return None  # cannot find path
    def draw_graph2(self):
        """
        visualization for theta, dotx, doty, and dottheta
        
        """
        tlist = []
        dxlist = []
        dylist = []
        dtlist = []
        for node in self.node_list:
            tlist.append(node.x[2])
            dxlist.append(node.x[3])
            dylist.append(node.x[4])
            dtlist.append(node.x[5])
        plt.plot(tlist, color = 'blue')
        plt.plot(dxlist, color = 'red')
        plt.plot(dylist, color = 'green')
        plt.plot(dtlist, color = 'orange')





    def draw_graph1(self, rnd=None):
        """
        shows node, tree, and the rnd node
        
        """
        plt.clf()
        # for stopping simulation with the esc key.
        plt.gcf().canvas.mpl_connect('key_release_event',
                                     lambda event: [exit(0) if event.key == 'escape' else None])
        if rnd is not None:
            plt.plot(rnd.x[0], rnd.x[1], "^k")
        for node in self.node_list:
            if node.parent:
                plt.plot(node.path_x[0], node.path_x[1], "-b")

        for (ox, oy, size) in self.obstacle_list:
            self.plot_circle(ox, oy, size)

        plt.plot(self.start.x[0], self.start.x[1], "xk")
        plt.plot(self.end.x[0], self.end.x[1], "xm")
        plt.axis("equal")
        plt.axis([-2, 15, -2, 15])
        plt.grid(True)
        plt.pause(0.01)


    def steer(self, from_node, to_node, extend_length=float("inf")):
        """
        returns the new_node in which to add to the node_list
        
        """

        new_node = Node(from_node.x.copy())
        d, theta = self.calc_distance_and_angle(new_node, to_node)

        new_node.path_x.append([new_node.x[0]])
        new_node.path_x.append([new_node.x[1]])
        new_node.path_x.append([new_node.x[2]])
        new_node.path_x.append([new_node.x[3]])
        new_node.path_x.append([new_node.x[4]])
        new_node.path_x.append([new_node.x[5]])

        if extend_length > d:
            extend_length = d
        n = extend_length / self.path_resolution
        n_expand = int(np.floor(n))
        for _ in range(n_expand):
            new_node.x[0] += self.path_resolution * np.cos(theta)
            new_node.x[1] += self.path_resolution * np.sin(theta)
            new_node.x[2] += (0.1) * self.path_resolution * np.sin(theta) 
            new_node.x[3] = random.uniform(0, max_speed)
            new_node.x[4] = random.uniform(0,max_speed)
            new_node.x[5] = random.uniform(0, max_speed)
            new_node.path_x[0].append(new_node.x[0])
            new_node.path_x[1].append(new_node.x[1])
            new_node.path_x[2].append(new_node.x[2])
            new_node.path_x[3].append(new_node.x[3])
            new_node.path_x[4].append(new_node.x[4])
            new_node.path_x[5].append(new_node.x[5])

        d, _ = self.calc_distance_and_angle(new_node, to_node)

        if d <= self.path_resolution:
            new_node.path_x[0].append(to_node.x[0])
            new_node.path_x[1].append(to_node.x[1])
            new_node.path_x[2].append(to_node.x[2])
            new_node.path_x[3].append(to_node.x[3])
            new_node.path_x[4].append(to_node.x[4])
            new_node.path_x[5].append(to_node.x[5])

        new_node.parent = from_node
        return new_node

    def generate_final_course(self, goal_ind):
        """
        generates the final path from start to goal
        
        """
        # do full state
        path = [[self.end.x[0], self.end.x[1], self.end.x[2], self.end.x[3], self.end.x[4], self.end.x[5]]]
        node = self.node_list[goal_ind]
        while node.parent is not None:
            path.append([node.x[0], node.x[1], node.x[2], node.x[3], node.x[4], node.x[5]])
            node = node.parent
        path.append([node.x[0], node.x[1], node.x[2], node.x[3], node.x[4], node.x[5]])

        return np.array(path)

    @jit
    def calc_dist_to_goal(self, x, y): 
        """
        calculates the distance from a node to the goal node
        
        """
        dx = x - self.end.x[0]
        dy = y - self.end.x[1]
        array = [dx, dy]
        return np.linalg.norm(array)

    def get_random_node(self):
        """
        returns a random node within parameters

        """
        if random.randint(0, 100) > self.goal_sample_rate:
            rnd = Node([random.uniform(self.min_rand, self.max_rand),
                            random.uniform(self.min_rand, self.max_rand),
                            random.uniform(-3, 3),
                            random.uniform(-1, max_speed),
                            random.uniform(-1, max_speed),
                            random.uniform(-1, max_speed)])

        else:  # goal point sampling
            rnd = Node([self.end.x[0], self.end.x[1], self.end.x[2], 0, 0, 0])
        return rnd

    

    @staticmethod
    def plot_circle(x, y, size, color="gray"):  # pragma: no cover
        """
        sub-function for draw_graph1, and plots a circle
        
        """
        deg = list(range(0, 360, 5))
        deg.append(0)
        xl = [x + size * np.cos(np.deg2rad(d)) for d in deg]
        yl = [y + size * np.sin(np.deg2rad(d)) for d in deg]
        plt.plot(xl, yl, color)

    @staticmethod
    def get_nearest_node_index(node_list, rnd_node):
        """
        gives the index of the nearest node to the random node
        
        """
        dlist = [(node.x[0] - rnd_node.x[0]) ** 2 + (node.x[1] - rnd_node.x[1])
                 ** 2 + (node.x[2] - rnd_node.x[2]) ** 2 for node in node_list]
        minind = dlist.index(min(dlist))

        return minind

    @staticmethod
    def check_collision(node, obstacleList):
        """
        checks for collisions
        
        """


        if node is None:
            return False

        for (ox, oy, size) in obstacleList:
            dx_list = [ox - x for x in node.path_x[0]]
            dy_list = [oy - y for y in node.path_x[1]]
            d_list = [dx * dx + dy * dy for (dx, dy) in zip(dx_list, dy_list)]

            if min(d_list) <= size ** 2:
                return False  # collision

        return True  # safe
    
 
    @staticmethod
    def calc_distance_and_angle(from_node, to_node):
        """
        returns the distance and angle between the nodes
        
        """
        dx = to_node.x[0] - from_node.x[0]
        dy = to_node.x[1] - from_node.x[1]
        dtheta = to_node.x[2] - from_node.x[2]
        array = [dx, dy, dtheta]
        d = np.linalg.norm(array)
        theta = np.arctan2(dy, dx) + dtheta
        return d, theta




def main(gx=8.0, gy=4.0):
    print("start " + __file__)

    # ====Search Path with RRT====
    obstacleList = [
        (2, 0, 2),
        (7, 0, 2),
        (4, 5, 2)
    ]  # [x, y, radius]
    # Set Initial parameters
    rrt = RRT(start=[0, 2],
              goal=[gx, gy],
              rand_area=[-2, 15],
              rand_angle=[-3, 3],
              vrange=[-1, 1, -.5, .5],
              obstacle_list=obstacleList)
    path = rrt.planning()
    if path is None:
        print("Cannot find path")
    else:
        print("found path!!")
        # Draw final path

        if show_animation:
            rrt.draw_graph1()
            plt.plot([x for (x, y, theta, dotx, doty, dottheta) in path], [y for (x, y, theta, dotx, doty, dottheta) in path], '-r')
            plt.grid(True)
            plt.pause(0.01)  # Need for Mac
            plt.show()

        if show_graph:
            rrt.draw_graph2()
            plt.show()

if __name__ == '__main__':
    main()

