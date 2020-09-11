#!/usr/bin/env python3

import numpy as np
import math as mt  
import random

"""
ao - rrt ??
no optimization 
control sampling and propagation 

"""

def f_dyn(x,control,mass,inertia,moment_arm):
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
    state_new = state_old + f_dyn(state_old,control,mass,inertia,moment_arm)*dt
    return state_new

def distance_to_goal(node,goal_state):
    node = node.reshape(6)
    goal_state = goal_state.reshape(6)
    state_norm_l2 = np.linalg.norm(node-goal_state)
    return state_norm_l2

def check_state_bounds(node,state_min,state_max):
    if (node < state_min).any() or (node > state_max).any():
        return False
    else:
        return True

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
    propagation_steps = 2,iters = 100000,cost_max = 1e6):


    return xsol, usol, tvec 
    




