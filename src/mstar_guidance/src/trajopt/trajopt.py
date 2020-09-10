#!/usr/bin/env python3

import numpy as np
from cloudpickle import dump, load

import os 
import os.path

import sys
np.set_printoptions(threshold=sys.maxsize)

# dependencies 
import cvxpy as cp 

cwd = os.getcwd()
# load linearized system matrices 
# /home/yashwanth/Desktop/catkin_ws_mstar_guidance/src/mstar_guidance/src/trajopt

Al = open('/home/yashwanth/Desktop/catkin_ws_mstar_guidance/src/mstar_guidance/src/trajopt/Amstar_det', 'rb')
As = load(Al)
Al.close()

Bl = open('/home/yashwanth/Desktop/catkin_ws_mstar_guidance/src/mstar_guidance/src/trajopt/Bmstar_det', 'rb')
Bs = load(Bl)
Bl.close()

Cl = open('/home/yashwanth/Desktop/catkin_ws_mstar_guidance/src/mstar_guidance/src/trajopt/Cmstar_det', 'rb')
Cs = load(Cl)
Cl.close()


# @jit
def sys_A(X,U):
    return As(X,U).round(5)


# @jit
def sys_B(X,U):
    return Bs(X,U).round(5)

# @jit
def sys_C(X,U,num_states):
    return Cs(X,U).reshape((num_states)).round(5)

# @jit
def collision_constraint_2d(radius,obstacle_state,Xprev,num_states):
    mean = Xprev.reshape((num_states,1))
    G = np.zeros((num_states,num_states)) # matrix to  pulling out position 
    G[0,0] = 1
    G[1,1] = 1

    mean_position = (np.mat(G)*np.mat(mean)).reshape((num_states)) 
    collision_dist = obstacle_state.reshape((num_states)) - mean_position
    
    a = collision_dist.reshape((num_states,1))
    b =  np.mat(-a.reshape((1,num_states)))*np.mat(obstacle_state.reshape((num_states,1))) + radius*np.linalg.norm(collision_dist,2)
    return np.array(a,dtype=float), np.array(b,dtype=float) 


def traj_opt(time_param,system_param,initial_state,terminial_state,control_cost,\
    control_limits,obstacle_information,nominal_trajectory,scp_param):
    
    ## time parameters 
    if os.path.isdir('data_det') == False:
        os.mkdir('data_det')

    t_init = time_param['time_init'] #time_param[0] # 0 # sec
    t_final = time_param['time_fin'] #5 # sec
    T = int(time_param['time_steps']) # total steps  
    tsteps = np.linspace(t_init,t_final,T) # time vector
    dt = tsteps[1]-tsteps[0] # time step

    # sytem parameters related to stochastic dynamics
    
    num_states = int(system_param['num_states']) 
    num_control = int(system_param['num_control'])

    Xinit = initial_state
    Xfin = terminial_state
     

    U_max = control_limits['u_max']
    U_min = control_limits['u_min']

    print('Control limits:')
    print('u max = ',U_max)
    print('u min = ',U_min)

 
    # Obstacle Information 
    # state and size loaded as a list in obstacle_information
    num_obstacles = len(obstacle_information)
    obstacle_radius = 0.7
    obstacle_state = obstacle_information
        
    # assign if a nominal trajectory is provided
    Xprev = np.linspace(Xinit,Xfin,int(T))
    Uprev = 0.01*np.ones([int(T-1), num_control])

    if nominal_trajectory[0] == True:
        Xprev = nominal_trajectory[1]
        Uprev = nominal_trajectory[2]
    else:
        Xprev = np.linspace(Xinit,Xfin,int(T))
        Uprev = 0.0001*np.ones([int(T-1), num_control])

    # X - gpc states, U - Control Input
    X = cp.Variable((T,num_states))
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
        constraint = []
        constraint.append(X[0] == Xinit.reshape((num_states)))
        constraint.append(cp.norm(X[T-1]-Xfin.reshape((num_states)))<= delta)
        
        # Obstacles
        for t in range(T-1):
            a = []
            b = []
            # TBD: check obstacles in range 
            for jj in range(num_obstacles):
                # obstacle linearization
                a1, b1 = collision_constraint_2d(obstacle_radius,obstacle_state[jj],Xprev[t,:], num_states)
                a.append(a1)
                b.append(b1)
            # collision constraint
            for jj in range(num_obstacles):
                constraint.append(a[jj]@X[t]+np.reshape(b[jj],1) <=0)
        
        # dynamics 
        for t in range(T-1):
            Aa = sys_A(Xprev[t,:].reshape((num_states)),Uprev[t,:].reshape((num_control)))
            Ba = sys_B(Xprev[t,:].reshape((num_states)),Uprev[t,:].reshape((num_control)))
            Ca = sys_C(Xprev[t,:].reshape((num_states)),Uprev[t,:].reshape((num_control)),num_states)
            constraint.append(X[t+1]==X[t]+dt*(Aa@X[t] + Ba@U[t] +Ca))

        # State trust region 
        for t in range(T):
            constraint.append(cp.norm(X[t,:] - Xprev[t,:].reshape((num_states))) <= trust)
            
        # control constraints
        for t in range(T-1):
            constraint.append(U[t]<=U_max*np.ones(num_control))
            constraint.append(U[t]>=U_min*np.ones(num_control))

            # control trust region 
            constraint.append(cp.norm(U[t,:] - Uprev[t,:].reshape((num_control))) <= trust)


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
            result = problem.solve(solver=cp.GUROBI,verbose=True)
        except:
            trust = trust*alpha
            print('Exception Occured, Increasing Trust to:',trust)
            continue

        Xv = np.around(X.value,decimals = 5)
        Uv = np.around(U.value,decimals = 5)

        err = np.linalg.norm(Xv-Xprev,axis=1)
        error =  np.amax(err)

        print("Optimal Value:%.3f Iteration:%d Trust: %f Error:%f"%(problem.value,iterat,trust,error))
        # print("Slack Value delta: %.3f" %(delta.value))
        print("Fuel cost:%.3f" %(cost.value))
        Xprev = Xv
        Uprev = Uv

        iterat = iterat +1
        trust = trust*beta

        namex = 'X'+str(iterat) + '.npy'
        nameu = 'U'+str(iterat) + '.npy'
        
        np.save(os.path.join('data_det', namex),Xv)
        np.save(os.path.join('data_det', nameu),Uv)
    
    # np.save('Xnom.npy',Xv)
    # np.save('Unom.npy',Uv)
    # print(Uv)
    return Xv, Uv 

# def simulation_trajopt():
    
#     time_param = {'time_init' : 0.0,'time_fin' : 50,'time_steps' : 100}
#     system_param = {'num_states': 6,'num_control':8,'num_uncert':7,'polynomial_degree': 1}

#     xinit_m = np.array([[0],[0],[0],[0],[0],[0]])   # = init_term_condition[0] #np.array([[0],[0],[0],[0],[0],[0]])
#     xinit_var = np.array([[0.0],[0.0],[0.00],[0.00],[0.00],[0.00]])  # = init_term_condition[1] #np.array([[0.0],[0.0],[0.00],[0.00],[0.0],[0.0]])
#     xfin_m = np.array([[1],[0],[0],[0],[0],[0]])    # = init_term_condition[0] #np.array([[0],[0],[0],[0],[0],[0]])
#     xfin_var = np.array([[0.0],[0.0],[0.00],[0.00],[0.00],[0.00]])  # = init_term_condition[1] #np.array([[0.0],[0.0],[0.00],[0.00],[0.0],[0.0]])
    
#     init_term_condition = []
#     init_term_condition.append(xinit_m) 
#     init_term_condition.append(xinit_var)
#     init_term_condition.append(xfin_m)
#     init_term_condition.append(xfin_var) 
    
#     # obstacle information 
#     # num_obstacles = obstacle_information[0]
#     # obstacles = obstacle_information[1]

#     # obstacle radius ----> # obstacles[jj,0]
#     # obstacle state -----> # obstacles[jj,1]
#     # risk of collision ----> # obstacles[jj,3]

#     num_obstacles = 0
#     obstacle_state = [np.array([[3],[-0.2],[0],[0]]),np.array([[7],[0.2],[0],[0]])]
#     obstacle_information = [num_obstacles,np.array([0.2,0.2]),obstacle_state,np.array([0.01,0.01])]

#     ##-- nominal trajectory 

#     Xnom = np.load('Xnom.npy')
#     Unom = np.load('Unom.npy')
    
#     nominal_trajectory = [True, Xnom, Unom]

#     ##-- SCP parameters 

#     scp_param = {'error_tolerance': 0.001, 'trust': 20000, 'beta': 0.9, 'alpha' :1.2 , 'iter_max' : 10 ,'slack' : True}

#     ##-------- Control Limits------------------

#     control_limits = {'u_max':0.45,'u_min':0}

#     ##-----------------Control Cost---------------------

#     control_cost = 'L1'
#     # control_cost = 'sum_squares'
#     # control_cost = 'inf'
    
#     traj_opt(time_param,system_param, init_term_condition, control_cost,\
#         control_limits, obstacle_information, nominal_trajectory, scp_param)

#     return print('Done! Move to Plotting and Analysis.')

if __name__ == "__main__":
    pass
