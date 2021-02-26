import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import quad

T = 0.8

def reduced_p(t):
    v = np.linspace(0.4,5,100)
    p1 = 8*t/(3*v-1)
    p2 = 3/v**2
    p = p1 - p2
    plt.axis([0.4,5,-2,10])
    plt.suptitle('Isotherm p-v for t=0.8')
    plt.xlabel('Reduced Volume')
    plt.ylabel('Reduced Pressure')
    plt.plot(v,p) #plot isotherm
    est_p = 0.36
    plt.plot([0.4,10],[est_p,est_p],'r--') #plot estimate vapor pressure
    plt.show()

def pressure(v): #lambda function to pass in
    p1 = 8*T/(3*v-1)
    p2 = 3/v**2
    p = p1 - p2
    return p
    
def solver(v_coeff): #[2.4,-8.4,9,-3]
    """
    Parameter: type(v_coeff) == 'List'
    List holding coefficients of homogenous polynomials. E.g for instance 2.4v^3-8.4v^2+9v-3:
    v_coeff = [2.4,-8.4,9,-3]
    """
    root_array = np.roots(v_coeff)
    root_array.sort()
    return root_array
    
def interval_area(t,p_v): #0.95 & trial vapor pressure
    v = np.linspace(0.4,5,100)
    p1 = 8*t/(3*v-1)
    p2 = 3/v**2
    p = p1 - p2
    root = solver([1.08,-6.76,9,-3])
    """
    A represents Error Area(LHS) which is the area under the line bounded by the isotherm
    C represents the area(RHS) under the isotherm bounded by the line
    """
    A, B = (root[1] - root[0]) * p_v - quad(pressure,  root[0], root[1]) #returns area and uncertainty
    C, D = quad(pressure, root[1], root[2]) - (root[2] - root[1]) * p_v #returns area and uncertainty
    print(A,C)

    
