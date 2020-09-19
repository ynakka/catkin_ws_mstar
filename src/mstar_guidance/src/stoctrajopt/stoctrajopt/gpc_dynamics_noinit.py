import numpy as np
from sympy import *

from cloudpickle import dump

# import toolbox_noinit as tb
from gPC_toolbox.fast_project_sde_2_ode import make_deterministic_sym
# from gPC_toolbox.project_sde_2_ode import make_deterministic_sym_noinit
from gPC_toolbox.linearize_gpc_dynamics import linearize_gpc_dynamics_noinit_theano


def main():
    ## -----------------------------------------------------------------
    ## -----------------------3DOF Spacecraft Simulator ----------------
    ## -----------------------------------------------------------------

    # System Parameters
    mass = 10
    inertia = 1.62
    l = 0.2
    b = 0.2

    # Dynamics
    num_states = 6
    x = Matrix([symbols('x'+str(i)) for i in range(0,num_states)])

    u1 = symbols('u1')
    u2 = symbols('u2')
    u3 = symbols('u3')
    u4 = symbols('u4')
    u5 = symbols('u5')
    u6 = symbols('u6')
    u7 = symbols('u7')
    u8 = symbols('u8')

    # Thrusters 
    u = Matrix(8,1,[u1,u2,u3,u4,u5,u6,u7,u8])
 
    # Control Influence 
    mi = 1/mass
    Ili = l/(inertia)
    Ibi = b/(inertia)

    H = Matrix([[-mi,-mi,0,0,mi,mi,0,0],[0,0,-mi,-mi,0,0,mi,mi],[-Ili,Ili,-Ibi,Ibi,-Ili,Ili,-Ibi,Ibi]])

    # Uncertainty In Control
    dyn_var = 0.0001
    sd_matrix = np.diag([np.sqrt(dyn_var),np.sqrt(dyn_var),np.sqrt(dyn_var)])
    mu = zeros(3,1)
    sigma = Matrix(sd_matrix)
    theta = Matrix([symbols('theta'+str(i)) for i in range(0,3)])
    # taylor_cos = series(cos(x[2]), x[2], x0=0, n=6).removeO()
    # taylor_sin = series(sin(x[2]), x[2], x0=0, n=6).removeO()

    # print(taylor_cos)
    # print(taylor_sin)
    taylor_cos = cos(x[2])
    taylor_sin = sin(x[2])

    f = zeros(3,3).row_join(eye(3,3)).col_join(zeros(3,6))*x + zeros(3,3).col_join(Matrix([[taylor_cos, taylor_sin, 0],[-taylor_sin, taylor_cos, 0],[0,0,1]]))*H*u
    g = zeros(3,1).col_join(mu + sigma*theta)

    # uncertainty in initial condition and the dynamics (learned component)
    # Learned component will be added 
    n_uncert = 9
    polynomial_degree = 1

    print(f+g)
    
    dyn_det, dyn_det_file, input_states = make_deterministic_sym(f, g, x, u, theta,n_uncert,polynomial_degree,init_uncertain=False)

    with open('mstar_dyn', 'wb') as fdyn: 
        dump((dyn_det), fdyn)
    print('dynamics saved')

    # print(dyn_det_file)
    # print(input_states)

    with open('mstar_dyn_theano', 'wb') as fdyn_lamb: 
        dump((dyn_det_file), fdyn_lamb)

    # following outputs thano functions
    # option for lambdified printing is available as well see the linearization
    # methods in the gPC_toolbox 
    # 
    [A,B,C] = linearize_gpc_dynamics_noinit_theano(dyn_det, x, u, n_uncert, polynomial_degree,input_states)
    with open('Amstar', 'wb') as fA: 
        dump((A), fA)
    with open('Bmstar', 'wb') as fB: 
        dump((B), fB)    
    with open('Cmstar', 'wb') as fC: 
        dump((C), fC)
    return 1


if __name__ == "__main__":
    main()