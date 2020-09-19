import  autograd.numpy as np
from autograd import grad, jacobian

import math
# @jit
def mstar_dyn(x,control):
    mass = 10 
    inertia = 1.62 
    moment_arm = 0.2
    # x = np.array(x.reshape(6),dtype=np.float32)
    control = np.array(control.reshape((8,1)))

    H = np.array([[-1,-1,0,0,1,1,0,0],[0,0,-1,-1,0,0,1,1],[-1,1,-1,1,-1,1,-1,1]])

    l =moment_arm
    physical_parameter = np.array([[1/mass,0,0],[0,1/mass,0],[0,0,l/inertia]])

    u = (physical_parameter@H@control).reshape((3))
    
    rotate = np.array([[np.cos(x[2]),np.sin(x[2]),0],[-np.sin(x[2]),np.cos(x[2]),0],[0,0,1]])
    pos = x[3:6]
    # print(pos)
    # print(pos)
    vel = rotate@u[0:3].reshape((3))
    return np.concatenate((pos,vel))

# @jit(nopython=True)
def euler_step(state_old,control,dt):
    state_new = state_old + mstar_dyn(state_old,control)*dt
    return state_new

def partialFx(mstar_dyn):
    return jacobian(mstar_dyn,0)

def partialFu(mstar_dyn):
    return jacobian(mstar_dyn,1)

if __name__ == "__main__":

    x = np.array([1,1,1,0,0,0])
    control = np.array([1,1,1,1,1,1,1,1])
    dt = 0.5
    # constructA = jit(jacfwd(euler_step, 0))
    print(euler_step(x,control,dt))