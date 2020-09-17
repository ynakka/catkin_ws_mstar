#!/usr/bin/env python3

import numpy as np
import math as mt  
import random
import hnswlib

import matplotlib.pyplot as plt
import csv
"""
ao - rrt ??
no optimization 
control sampling and propagation 

"""

def mstar_dyn(x,control,mass,inertia,moment_arm):
    x = x.reshape(6)
    control = control.reshape((8,1))

    H = np.array([[-1,-1,0,0,1,1,0,0],[0,0,-1,-1,0,0,1,1],[-1,1,-1,1,-1,1,-1,1]])

    l =moment_arm
    physical_parameter = np.array([[1/mass,0,0],[0,1/mass,0],[0,0,l/inertia]])

    dxdt = np.zeros(6)
    u = (physical_parameter@H@control).reshape((3))
    dxdt[0] = x[3]
    dxdt[1] = x[4]
    dxdt[2] = x[5]
    dxdt[3] = mt.cos(x[2])*u[0] + mt.sin(x[2])*u[1]
    dxdt[4] = -mt.sin(x[2])*u[0] + mt.cos(x[2])*u[1]
    dxdt[5] = u[2]
    return dxdt


def euler_step(state_old,control,dt,mass,inertia,moment_arm):
    state_new = state_old + mstar_dyn(state_old,control,mass,inertia,moment_arm)*dt
    return state_new

def distance_to_goal(node,goal_state):
    node = node.reshape(6)
    goal_state = goal_state.reshape(6)
    state_norm_l2 = np.linalg.norm(node-goal_state)
    return state_norm_l2

def check_state_bounds(node,state_min,state_max):
    if (node < state_min).any() or (node > state_max).any():
        return True
    else:
        return False

def collision_checking(node,obstacle_list,num_obstacles):    
    for i in range(num_obstacles):
        pos = node[0:2]
        obstaclepos = obstacle_list[i][0][0:2]
        if np.linalg.norm(pos-obstaclepos) <= obstacle_list[i][1]:
            return True
    return False


def sample_state(state_min,state_max):
    node_sample = np.random.uniform(state_min,state_max)    
    return node_sample

def sample_control(num_control,Umin,Umax):
    control_sample = np.random.uniform(Umin,Umax,num_control)
    return control_sample

def rrt_ao_mstar(state_init,state_goal,dt,\
    obstacle_list,state_min,state_max,Umin,Umax,mass,inertia,moment_arm,\
    propagation_steps = 4,iters = 100000,cost_limit = 1e6,trials=10,top_k=100):

    """
    This is taken from Wolfgangs Code.

    """
    sample_goal_iter = 50
    parents = -np.ones((iters,),dtype=np.int)
    states = np.zeros((iters,6),dtype=np.float32)
    states_temp = np.zeros((iters,propagation_steps+1,6),dtype=np.float32) # includes the parent node
    actions = np.zeros((iters,8),dtype=np.float32)
    timesteps = np.zeros((iters,),dtype=np.int)
    cost = np.zeros((iters,),dtype=np.float32)
    
    expand_attempts = np.zeros((iters,),dtype=np.int)
    expand_successes = np.zeros((iters,),dtype=np.int)

    num_obstacles = len(obstacle_list)
    # begin trial
    
    for trail in range(trials):
        states[0] = state_init
        i = 1
        attempt = 0
        best_distance = 1e6
        best_i = 0
        best_cost = cost_limit

        index = hnswlib.Index(space='l2', dim=6)
        # ef_construction - controls index search speed/build speed tradeoff
        #
        # M - is tightly connected with internal dimensionality of the data. Strongly affects memory consumption (~M)
        # Higher M leads to higher accuracy/run_time at fixed ef/efConstruction
        index.init_index(max_elements=iters, ef_construction=100, M=16)

        # Controlling the recall by setting ef:
        # higher ef leads to better accuracy, but slower search
        index.set_ef(100)
        index.add_items(states[0])

        sol_x = None
        sol_u = None

        while attempt < iters:
            attempt +=1
            print(attempt)
            # randomly sample a state
            if attempt % sample_goal_iter == 0:
                idx = best_i
                # x = state_goal
            else:
                x = sample_state(state_min,state_max)
                ids, distances = index.knn_query(x, k=min(top_k,i))
                # idx = ids[0,np.random.randint(0, ids.shape[1])]
                idx = ids[0,0]
            
            u = sample_control(8,Umin,Umax)
            cost[i] = cost[idx] + np.linalg.norm(u)
            if cost[i] > cost_limit:
                continue

            timesteps[i] = timesteps[idx] + propagation_steps

            # forward propagate
            states_temp[i,0] = states[idx]
            all_states_valid = True

            for k in range(1,propagation_steps+1):
            # propagate
                # states_temp[i,k] = robot.step(torch.from_numpy(states_temp[i,k-1]), torch.from_numpy(u), data_neighbors_next_i, dt).detach().numpy()
                states_temp[i,k] = euler_step(states_temp[i,k-1],u,dt,mass,inertia,moment_arm)
            # validity check
                if check_state_bounds(states_temp[i,k],state_min,state_max) or collision_checking(states_temp[i,k],obstacle_list,num_obstacles):
                # if not state_valid(robot, states_temp[i,k], data_neighbors_next_i) or not:
                    all_states_valid = False
                    # print('all states valid:',all_states_valid)
                    break
            
            if not all_states_valid:
                continue

            # update data structures
            parents[i] = idx
            states[i] = states_temp[i,-1]
            actions[i] = u

            expand_successes[idx] += 1

            index.add_items(states[i:i+1])

            # dist = np.linalg.norm(states[i,0:3] - xf[0:3])
            dist = np.linalg.norm(states[i,0:2] - state_goal[0:2])

            # find best solution to goal
            if best_distance > dist:
                best_distance = dist
            #   print(dist)
                best_i = i
            # print("best distance: ", best_distance, best_i, attempt)

            i+=1
            # print('increased the step')
            # print('best distance :', best_distance)
            if best_distance < 0.1:
                print('reached goal')
                idx = best_i
                best_cost = cost[idx]
                cost_limit = 0.9 * cost[idx]

                sol_x = []
                sol_u = []
                while idx > 0:
                    for k in reversed(range(1, propagation_steps+1)):
                        sol_x.append(states_temp[idx,k])
                        sol_u.append(actions[idx])
                        idx = parents[idx]
                sol_x.append(states[0])
                sol_x.reverse()
                sol_u.reverse()

                sol_npx = np.array(sol_x)
                sol_npu = np.array(sol_u)

                return sol_npx, sol_npu

    # return sol_x, sol_u
    
if __name__ == "__main__":
    state_init = np.zeros(6)
    state_goal = np.array([1,1,0,0,0,0])

    dt = 0.5
    state_min = np.array([0,0,-mt.pi,-1,-1,-10])
    state_max = np.array([1,1,mt.pi,1,1,10])

    Umin = 0
    Umax = 0.45

    mass = 10 
    inertia = 1.6
    moment_arm = 0.2

    obstacle_list = []
    # obstacle state and distance between the robot and the obstacle
    obstacle1 = [np.array([0.5,0.5,0,0,0,0]),0.2]
    obstacle_list.append(obstacle1)
    obstacle2 = [np.array([0.7,0.3,0,0,0,0]),0.2]
    obstacle_list.append(obstacle2)
    # obstacle3 = [np.array([3,3,0,0,0,0]),1]
    # obstacle_list.append(obstacle3)

    solx, solu = rrt_ao_mstar(state_init,state_goal,dt,\
    obstacle_list,state_min,state_max,Umin,Umax,mass,inertia,moment_arm,\
    propagation_steps = 2,iters = 100000,cost_limit = 1e6,trials=10,top_k=100)

    # print(len(solx))
    # print(len(solu))

    # print(np.shape(np.array(solx)))

    # print(np.shape(np.array(solu)))

    # print(solx)
    # print(np.array(solx))


        