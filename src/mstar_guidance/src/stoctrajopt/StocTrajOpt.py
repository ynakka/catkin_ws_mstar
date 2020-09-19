#!/usr/bin/env python3

import numpy as np
import scipy as sp
from sympy import *
from scipy.special import comb
from scipy.linalg import sqrtm
from itertools import combinations
from cloudpickle import dump, load
# import matplotlib.pyplot as plt

import os.path

import sys
np.set_printoptions(threshold=sys.maxsize)

# dependencies 
import cvxpy as cp 
from numba import jit

import warnings 
warnings.filterwarnings('ignore') 
# from numba import jit
## Des-SOC toolbox v0 -- not used anymore
# dates used 11/11/2019---5/30/2020
# import toolbox_noinit as tb   # no uncertainty in intial conditions 
# import GaussHermitePC as GaussHermitePC

## Des-SOC toolbox v1
# used since 6/6/2020
from gPC_toolbox.initial_conditions import initial_conditions_noinit
from gPC_toolbox.cost_function import l2_cost_function_noinit
from gPC_toolbox.chance_constraints import linear_chance_constraint_matrices_noinit, linear_chance_constraint_noinit, obstacle_variance_gpc_assignment
from gPC_toolbox.GaussHermitePC import GaussHermitePC

from gPC_toolbox.collision_constraint import collision_constraint_2d_noinit
from gPC_toolbox.project_gpc_2_statespace import meangpc_fullstate_noinit


# load linearized system matrices 
Al = open('Amstar', 'rb')
As = load(Al)
Al.close()

Bl = open('Bmstar', 'rb')
Bs = load(Bl)
Bl.close()

Cl = open('Cmstar', 'rb')
Cs = load(Cl)
Cl.close()

# @jit
def sys_A(states,num_gpcstates):
    return np.array(As(*states)).reshape((num_gpcstates,num_gpcstates)).round(5)

# @jit
def sys_B(states,num_gpcstates,num_control):
    return np.array(Bs(*states)).reshape((num_gpcstates,num_control)).round(5)

# @jit
def sys_C(states,num_gpcstates):
    return np.array(Cs(*states)).reshape((num_gpcstates)).round(5)

def distance_to_obstacle(obstacle_state,X,num_states,num_gpcpoly):
    x = meangpc_fullstate_noinit(X,num_states,num_gpcpoly)
    if np.linalg.norm(obstacle_state[0:2]-x[0:2]) <= 2:
        return True
    else:
        return False

def stoc_traj_opt_noinit(time_param,system_param,initial_state,terminal_state,control_cost,state_cost,\
    control_limits,obstacle_list,nominal_trajectory,scp_param, stochastic_obstacle, project = True):
    x_sol = []
    u_sol = []    
    ## time parameters 
    if os.path.isdir('data') == False:
        os.mkdir('data')

    dt = time_param['dt']
    T = int(time_param['time_steps'])
    # t_init = time_param['time_init'] #time_param[0] # 0 # sec
    # t_final = time_param['time_fin'] #5 # sec
    # T = int(time_param['time_steps']) # total steps  
    # tsteps = np.linspace(t_init,t_final,T) # time vector
    # dt = tsteps[1]-tsteps[0] # time step

    # sytem parameters related to stochastic dynamics
    
    num_states = int(system_param['num_states']) 
    num_control = int(system_param['num_control']) 
    num_uncert = int(system_param['num_uncert']) 
    polynomial_degree = int(system_param['polynomial_degree'])
    # no. of projected states
    Hp = Matrix(GaussHermitePC(num_uncert-num_states,polynomial_degree))
    num_gpcpoly = Hp.shape[0]
    num_gpcstates = int(num_gpcpoly*num_states) 
    num_obstacles = int(len(obstacle_list))

    # Obstacle Information 
    # state and size loaded as a list in obstacle_information
    obstacle_risk = 0.05

    if stochastic_obstacle[0] == True:
        obstacle_gpc_state = []
        for i in range(num_obstacles):
            dummy_obs_state = obstacle_variance_gpc_assignment(stochastic_obstacle[1][i],num_states,num_uncert,num_gpcstates)
            obstacle_gpc_state.append(dummy_obs_state)
        
    ## Linearized matrices need to be loaded already 
    # symbolic states for projected states 
    # x = Matrix([symbols('x'+str(i)) for i in range(0,num_states)])

    if os.path.isfile(os.path.join('data', 'Xinit.npy')) == False or project == True:
        print('Projecting Initial Conditions.')
        xinit_m = initial_state #np.array([[0],[0],[0],[0],[0],[0]])
        Xinit = initial_conditions_noinit(xinit_m,num_gpcpoly)
        np.save(os.path.join('data', 'Xinit.npy'),np.round(Xinit,decimals = 4))
    else: 
        print('Loading Initial Conditions')
        Xinit = np.load(os.path.join('data', 'Xinit.npy'))

    if os.path.isfile(os.path.join('data', 'Xfin.npy')) == False or project == True:
        print('Projecting Terminal Conditions.')
        xfin_m = terminal_state#np.array([[1],[1],[0],[0],[0],[0]])
        Xfin = initial_conditions_noinit(xfin_m,num_gpcpoly)
        np.save(os.path.join('data', 'Xfin.npy'),np.round(Xfin,decimals = 4))
    else: 
        print('Loading Terminal Conditions')
        Xfin = np.load(os.path.join('data', 'Xfin.npy'))

    
    if os.path.isfile(os.path.join('data', 'Qgpc.npy')) == False:
        print('Projecting Cost Function.')
        # Quadratic Cost Function 
        Q = state_cost[0]
        Qgpc = l2_cost_function_noinit(Q,num_states,num_uncert,polynomial_degree)
        np.save(os.path.join('data', 'Qgpc.npy'),np.round(Qgpc,decimals = 4))
    else: 
        print('Loading Cost Function.')
        Qgpc = np.load(os.path.join('data', 'Qgpc.npy'))
    
    if os.path.isfile(os.path.join('data', 'Qfgpc.npy')) == False:
        print('Projecting Terminal Cost.')
        # Quadratic Cost Function 
        Qf = state_cost[1] # terminal cost
        c_term = state_cost[2]['c_term']
        epsilon_term = state_cost[2]['epsilon_term']
        Qfgpc = l2_cost_function_noinit(Qf,num_states,num_uncert,polynomial_degree)
        np.save(os.path.join('data', 'Qfgpc.npy'),np.round(Qfgpc,decimals = 4))
    else: 
        print('Loading Terminal Cost Function.')
        c_term = state_cost[2]['c_term']
        epsilon_term = state_cost[2]['epsilon_term']
        Qfgpc = np.load(os.path.join('data', 'Qfgpc.npy'))

    U_max = control_limits['u_max']
    U_min = control_limits['u_min']

    print('Control limits:')
    print('u max = ',U_max)
    print('u min = ',U_min)

    print('# gpc polynomials :' + str(num_gpcpoly))
    print('# gpc states :' + str(num_gpcstates))
    
    # obstacle radius ----> # obstacles[jj,0]
    # obstacle state -----> # obstacles[jj,1]
    # risk of collision ----> # obstacles[jj,3]

    ##  Linear Chance Contraint Matrices to be used for stochastic collision checking.
    M, N  = linear_chance_constraint_matrices_noinit(num_states,num_uncert,polynomial_degree)
    
    # ## sigma for obstacle
    # sigma_obs = []
    # for i in range(num_obstacles):
    #     sigma_dummy = sigma_var_gpc_obs
    #     sigma_obs.append(sigma_dummy)
    ## Read the nominal trajectory from the input data

    # assign the nominal trajectory to the gPC coordinates
    # 
    # initialize 

    # assign if a nominal trajectory is provided
    Xprev = np.linspace(Xinit,Xfin,int(T))
    # Uprev = 0.1*np.ones([int(T-1), num_control])

    if nominal_trajectory[0] == True:
        x_nominal = nominal_trajectory[1]
        # print(x_nominal)
        u_nominal = nominal_trajectory[2]
        for i in range(num_states):
            print(i)
            Xprev[:,int(i*num_gpcpoly)] = x_nominal[:,i].reshape((T,1))
        Uprev = u_nominal
    else:
        Xprev = np.linspace(Xinit,Xfin,int(T))
        Uprev = 0.0001*np.ones([int(T-1), num_control])

    x_sol.append(Xprev)
    u_sol.append(Uprev)

    # X - gpc states 
    # U - Control Input
    X = cp.Variable((T,num_gpcstates))
    U = cp.Variable((T-1,num_control))
    delta = cp.Variable(1)

    ## SCP Parameters 

    error_tolerance = scp_param['error_tolerance']
    trust = scp_param['trust']
    beta =  scp_param['beta']
    alpha = scp_param['alpha']
    iter_max = scp_param['iter_max']

    error = 1
    iterat = 1

    print('Starting SCP for Trajectory!')


    while iterat<=iter_max and error>= error_tolerance:
        ## Constraints For Optimization
        
        constraint = [X[0] == Xinit.reshape((num_gpcstates))]
                
        # Expectation terminal constraint
        for oo in range(num_states):
            constraint.append(X[T-1,oo*num_gpcpoly]==Xfin[oo*num_gpcpoly])
            # print(Xfin[oo*num_gpcpoly])
        # #-------------------- Terminal Quadratic Constraint -----------
        # This has to be set very carefully
        constraint.append(cp.norm(X[T-1]-Xfin.reshape((num_gpcstates)))<= delta)
        
        # Obstacles
        for t in range(T-1):
            a = []
            b = []
            a_hat = []
            sigma_hat = []

            # TBD: check obstacles in range
            for jj in range(num_obstacles):
                if distance_to_obstacle(obstacle_list[jj][0],Xprev[t,:],num_states,num_gpcpoly):# obstacle linearization
                    a1, b1 = collision_constraint_2d_noinit(obstacle_list[jj][1],obstacle_list[jj][0],Xprev[t,:], num_states, num_uncert, polynomial_degree )
                    a.append(a1)
                    b.append(b1)
                    a_hat1, sigma_hat1 = linear_chance_constraint_noinit(a1,M,N,obstacle_risk,num_gpcpoly,num_states,num_uncert,polynomial_degree)
                    a_hat.append(a_hat1)
                    sigma_hat.append(sigma_hat1)
            # collision constraint
                    if stochastic_obstacle[0] == True:
                        constraint.append(cp.SOC(-a_hat[jj]@X[t]-np.reshape(b[jj],1),sigma_hat[jj]@X[t] + sigma_hat[jj]@obstacle_gpc_state[jj]))
                    else:
                        constraint.append(cp.SOC(-a_hat[jj]@X[t]-np.reshape(b[jj],1),sigma_hat[jj]@X[t]))

        # dynamics 
        for t in range(T-1):
            input_states = np.concatenate((Xprev[t,:].reshape((num_gpcstates)),Uprev[t,:].reshape((num_control)),np.array([dt])))
            Aa = sys_A(input_states,num_gpcstates)
            Ba = sys_B(input_states,num_gpcstates,num_control)
            Ca = sys_C(input_states,num_gpcstates)

            constraint.append(X[t+1]==X[t]+ Aa@X[t] + Ba@U[t] +Ca)

        # State trust region 
        for t in range(T):
            constraint.append(cp.norm(X[t,:] - Xprev[t,:].reshape((num_gpcstates))) <= trust)
            
        # control constraints
        for t in range(T-1):
            constraint.append(U[t]<=U_max*np.ones(num_control))
            constraint.append(U[t]>=U_min*np.ones(num_control))

            # control trust region 
            constraint.append(cp.norm(U[t,:] - Uprev[t,:].reshape((num_control))) <= delta)


        if control_cost == 'sum_squares':
            cost = cp.sum_squares(U)*dt

        if control_cost == 'L1':
            cost = 0
            for t in range(T-1):
                cost += cp.norm1(U[t])*dt 

        if control_cost == 'inf':
            cost = 0
            for t in range(T-1):
                cost = cp.norm(U[t],"inf")
       
        problem = cp.Problem(cp.Minimize(cost + 1e3*delta),constraint)
        
        try:
            print("Solving now!")
            result = problem.solve(solver= cp.ECOS, verbose=True)
        except:
            trust = trust*alpha
            print('Exception Occured, Increasing Trust to:',trust)
            continue

        # if result is None or result > 1e9 or result==False:
        #     trust = trust*alpha
        #     print('Exception Occured, Increasing Trust to:',trust)
        #     continue

        Xv = np.around(X.value,decimals = 5)
        Uv = np.around(U.value,decimals = 5)

        # print('Slack Value delta =', delta.value)
        # print('Fuel cost =', cost.value)
        
        err= np.zeros(T-1)
        for t in range(T-1):
            err[t] = np.linalg.norm(Xv[t,:]-Xprev[t,:])

        error =  np.amax(err)

        print("Optimal Value:%.3f Iteration:%d Trust: %f Error:%f"%(problem.value,iterat,trust,error))
        # print("Slack Value delta: %.3f" %(delta.value))
        print("Fuel cost:%.3f" %(cost.value))
        Xprev = Xv
        Uprev = Uv

        x_sol.append(Xprev)
        u_sol.append(Uprev)

        iterat = iterat +1
        trust = trust*beta

        namex = 'X'+str(iterat) + '.npy'
        nameu = 'U'+str(iterat) + '.npy'
        
        np.save(os.path.join('data', namex),Xv)
        np.save(os.path.join('data', nameu),Uv)
    
    # np.save('Xnom.npy',Xv)
    # np.save('Unom.npy',Uv)
    # print(Uv)
    return Xv, Uv
if __name__ == "__main__":

    import time

    x = np.ones(24)
    dt = np.array([0.5])
    u = np.ones(8)
    num_gpc = 24
    num_control = 8

    state = np.concatenate((x,u,dt))

    start = time.time()
    xx = sys_A(state,num_gpc)
    print(time.time()-start)
    start = time.time()
    yy = As(*state)
    print(time.time()-start)




