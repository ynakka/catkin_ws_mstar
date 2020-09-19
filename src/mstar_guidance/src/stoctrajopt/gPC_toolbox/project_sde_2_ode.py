#!/usr/bin/env python3

import numpy as np
from sympy import *
from scipy.special import comb
from scipy.linalg import sqrtm
from itertools import combinations

from gPC_toolbox.UnivariateGaussHermiteQuadrature import UnivariateGaussHermiteQuadrature
from gPC_toolbox.GaussHermitePC import GaussHermitePC
from gPC_toolbox.density import gaussian_density
from gPC_toolbox.numerical_integration import integrate_gauss

from cloudpickle import dump, load

def make_deterministic_sym_noinit(f, g, mu, sigma, x, u, theta, num_uncertainty, p):
    """
    Converts stochasitic dynamics
    xdot = f(x,u) + g(x,u, theta)
    to deterministic approximation, with certain bounds

    # Uses SYmbolic Integration

    Parametersyp
    ----------
    f : sympy expression in x and u
        the initial deterministic component
    g : sympy expression in x, u, and theta
        the stochastic component
    mu : sympy constant/number
        the mean of theta
    sigma : sympy constant/number
        the variance of theta
    x : sympy symbol
        the state
    u : sympy symbol
        the control
    theta : sympy symbol
        the normally distributed noise
    
    p : order of the polynomial expansion (user design choice)

    num_uncertainty: total uncertainty = num_states+num_uncertainparam_dyn
    
    Returns
    -------
    sympy expression in x and u
        the deterministic dynamics

    """
    n_states = x.shape[0]
    n_uncert = num_uncertainty
    #===============================================================================#
    # If only one uncertain parameter in the system 
    # this is used in the CDC paper only, preliminary example
    if n_uncert==1:
        xi = symbols('xi')
        
        g = g.subs([(theta,mu[0]+sqrt(sigma[0])*xi)])
        
        Hp = Matrix(GaussHermitePC(n_uncert,p))

        # Number of the the Generalized Polynomial Chaos - Polynomials

        l = Hp.shape[0]
        
        # Generating the Symbolic Polynomial Chaos Expansion with Coefficients
        xct = zeros(n_states,1)
        for i in range(0,n_states):
            xc_vals = [symbols('x'+str(i)+str(j)) for j in range(0,l)]
            xct_dummy = Matrix(xc_vals)
            xct[i] = xct_dummy.T*Hp
        # print(xct)
        # Substituting in the Dynamics 
        for i in range(n_states):
            f = f.subs({x[i]:xct[i]})
            g = g.subs({x[i]:xct[i]})

        # Dynamics Interms of the coefficients and the germ $\xi$
        dyn = (f+g) 
        # Kronecker Product

        Phi = Matrix(np.kron(np.identity(n_states),Hp.T))

        left = Phi.T*Phi
        right = Phi.T*dyn

        for xi_i in xi:
            left_int = integrate(gaussian_density(xi_i)*left_int, (xi_i,-oo,oo))
            right_int = integrate(gaussian_density(xi_i)*right_int, (xi_i,-oo,oo))
            #print(xi_i)

        dyn_det =  left_int.inv()*right_int 

        return Matrix(dyn_det)
#================================================================================#
    # For more than one uncertain parameter in the dynamics
    # For Research Problems
    else:

        xi_symbols = [symbols('xi'+str(i)) for i in range(1,n_uncert-n_states+1)]
        xi =  Matrix(xi_symbols)
        #print('xi symbols')
        #print(xi)
        #Express theta_i in terms of unit gaussian xi_i
        theta_subs= zeros(1,n_uncert-n_states)
        for i in range(n_uncert-n_states):
            theta_subs[i] = mu[i] + sqrt(sigma[i])*xi[i]
        #print(theta_subs)
        for j in range(n_uncert-n_states):
            g = g.subs({theta[j]:theta_subs[j]})

        #rescaled Hermite polynomials
        Hp = GaussHermitePC(n_uncert-n_states,p)
        #rint(Hp)

        #expansions of states using the Hermite polynomials
        ## X in the paper

        l = Hp.shape[0]

        # Generating the Symbolic Polynomial Chaos Expansion with Coefficients
        xct = zeros(n_states,1)
        for i in range(0,n_states):
            xc_vals = [symbols('x'+str(i)+str(j)) for j in range(0,l)]
            xct_dummy = Matrix(xc_vals)
            xct[i] = xct_dummy.T*Hp
            #print(xc_vals)

        for i in range(n_states):
            f = f.subs({x[i]:xct[i]})
            g = g.subs({x[i]:xct[i]})

        # Dynamics Interms of the coefficients and the germ $\xi$
        dyn = (f+g) 
        # Kronecker Product

        Phi = Matrix(np.kron(np.identity(n_states),Hp.T))

        left = Phi.T*Phi
        right = Phi.T*dyn

        left_int = left
        right_int = right

        print('Working on computing projections.\n')

        left_dummy = left.shape[0]

        for numl in range(0,left_dummy):
            for xi_i in xi:
                left_int[numl,:] = integrate(gaussian_density(xi_i)*left_int[numl,:], (xi_i,-oo,oo))
                print(xi_i)
            print(numl)
        
        print('Finished computing the integrals on left hand side. \n')

        right_dummy = right.shape[0]

        for numr in range(0,right_dummy):
            for xi_i in xi:
                right_int[numr] = integrate(gaussian_density(xi_i)*right_int[numr], (xi_i,-oo,oo))
                print(xi_i)
            print(numr)
        # print("LEFT")
        # print(N(left_int,5))
        # print("RIGHT")
        # print(right_int)
        # quit()
        print('Computing the projected dynamics\n')
        dyn_det =  left_int.inv()*right_int
    
        return Matrix(dyn_det)



def make_deterministic_sym(f, g, mu, sigma, x, u, theta, num_uncertainty, p):
    """
    Converts stochasitic dynamics
    xdot = f(x,u) + g(x,u, theta)
    to deterministic approximation, with certain bounds

    # Uses SYmbolic Integration

    Parametersyp
    ----------
    f : sympy expression in x and u
        the initial deterministic component
    g : sympy expression in x, u, and theta
        the stochastic component
    mu : sympy constant/number
        the mean of theta
    sigma : sympy constant/number
        the variance of theta
    x : sympy symbol
        the state
    u : sympy symbol
        the control
    theta : sympy symbol
        the normally distributed noise
    
    p : order of the polynomial expansion (user design choice)

    num_uncertainty: total uncertainty = num_states+num_uncertainparam_dyn
    
    Returns
    -------
    sympy expression in x and u
        the deterministic dynamics

    """
    n_states = x.shape[0]
    n_uncert = num_uncertainty
#===============================================================================#
    xi_symbols = [symbols('xi'+str(i)) for i in range(1,n_uncert+1)]
    xi =  Matrix(xi_symbols)
    #print('xi symbols')
    #print(xi)
    #Express theta_i in terms of unit gaussian xi_i
    theta_subs= zeros(1,n_uncert-n_states)
    for i in range(n_uncert-n_states):
        theta_subs[i] = mu[i] + sqrt(sigma[i])*xi[i]
    #print(theta_subs)
    for j in range(n_uncert-n_states):
        g = g.subs({theta[j]:theta_subs[j]})

    #rescaled Hermite polynomials
    Hp = GaussHermitePC(n_uncert,p)
    print(Hp)

    #expansions of states using the Hermite polynomials
    ## X in the paper

    l = Hp.shape[0]

    # Generating the Symbolic Polynomial Chaos Expansion with Coefficients
    xct = zeros(n_states,1)
    for i in range(0,n_states):
        xc_vals = [symbols('x'+str(i)+str(j)) for j in range(0,l)]
        xct_dummy = Matrix(xc_vals)
        xct[i] = xct_dummy.T*Hp
        #print(xc_vals)

    for i in range(n_states):
        f = f.subs({x[i]:xct[i]})
        g = g.subs({x[i]:xct[i]})

    # Dynamics Interms of the coefficients and the germ $\xi$
    
    dyn = (f+g) 
    
    # print(dyn)
    # Kronecker Product

    Phi = Matrix(np.kron(np.identity(n_states),Hp.T))


    left = Phi.T*Phi
    right = Phi.T*dyn

    left_int = left
    right_int = right

    # print(right)

    print('Working on computing projections.\n')

    left_dummy = left.shape[0]
    [weight,node] = UnivariateGaussHermiteQuadrature(10)

    for numl in range(0,left_dummy):
        for xi_i in xi:
            # left_int[numl,:] = integrate(gaussian_density(xi_i)*left_int[numl,:], (xi_i,-oo,oo))
            left_int[numl,:] = integrate_gauss(weight,node,left_int[numl,:],xi_i)

        #print(xi_i)
        print(numl)
    
    print('Finished computing the integrals on left hand side. \n')

    right_dummy = right.shape[0]

    for numr in range(0,right_dummy):
        for xi_i in xi:
            # right_int[numr] = integrate(gaussian_density(xi_i)*right_int[numr], (xi_i,-oo,oo))
            right_int[numr,:] = integrate_gauss(weight,node,right_int[numr,:],xi_i)
            print(xi_i)
        print(numr)

    # print("LEFT")
    # print(N(left_int,5))
    # print("RIGHT")
    # print(right_int)
    # quit()
    print('Computing the projected dynamics\n')
    dyn_det =  left_int.inv()*right_int

    xc_vals_dummy = zeros(l,n_states)
    for i in range(0,n_states):
        xc_vals_dummy[:,i] = Matrix([symbols('x'+str(i)+str(j)) for j in range(0,l)])

    states = xc_vals_dummy.T.reshape(n_states*l,1)

    # print(states)

    print('Lambdifying the file.')

    dyn_det_file = lambdify((states),dyn_det,'numpy')

    # print(dyn_det_file)    

    return Matrix(dyn_det), dyn_det_file