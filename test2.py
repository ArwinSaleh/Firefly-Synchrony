# This function randomly samples initial values in the domain and returns whether the solution converged

# Inputs:
# f             change in theta (d_theta)
# g             change in omega (d_omega)
# tol           when step size is lower than tolerance, the solution is said to converge
# h             size of the time step
# max_iter      maximum number of steps Runge-Kutta will perform before giving up
# max_laps      maximum number of laps the solution can do before giving up
# fixed_t       vector of fixed points of theta
# fixed_o       vector of fixed points of omega
# n             number of dimensions

# theta         initial theta vector
# omega         initial omega vector

# Outputs:
# converges     true if it nodes restabilizes, false otherwise

import numpy as np

def kuramoto_rk4_wss(f,g,tol_ss,tol_step,h,max_iter,max_laps,fixed_o,fixed_t,n):
    def layer1(theta,omega):
        lap = np.zeros(n, dtype = int)
        converges = False
        i = 0
        tau = 2 * np.pi

        while(i < max_iter): # perform RK4 with constant time step
            p_omega = omega
            p_theta = theta
            T1 = h*f(omega)
            O1 = h*g(theta,omega)
            T2 = h*f(omega + O1/2)
            O2 = h*g(theta + T1/2,omega + O1/2)
            T3 = h*f(omega + O2/2)
            O3 = h*g(theta + T2/2,omega + O2/2)
            T4 = h*f(omega + O3)
            O4 = h*g(theta + T3,omega + O3)

            theta = theta + (T1 + 2*T2 + 2*T3 + T4)/6 # take theta time step

            mask2 = np.array(np.where(np.logical_or(theta > tau, theta < 0))) # find which nodes left [0, 2pi]
            lap[mask2] = lap[mask2] + 1 # increment the mask
            theta[mask2] = np.mod(theta[mask2], tau) # take the modulus

            omega = omega + (O1 + 2*O2 + 2*O3 + O4)/6

            if(max_laps in lap): # if any generator rotates this many times it probably won't converge
                break
            elif(np.any(omega > 12)): # if any of the generators is rotating this fast, it probably won't converge
                break
            elif(np.linalg.norm(omega) < tol_ss and # assert the nodes are sufficiently close to the equilibrium
               np.linalg.norm(omega - p_omega) < tol_step and # assert change in omega is small
               np.linalg.norm(theta - p_theta) < tol_step): # assert change in theta is small
                converges = True
                break
            i = i + 1
        return converges
    return layer1

