import math
import matplotlib.pyplot as plt
import numpy as np

t = float(input("Enter time(s):"))

def gibbs(t):

    v = np.linspace(0.4,5,100)
    g_1 = -8*t*np.log(3*v-1)/3
    g_2 = 8*t/(9*v-3)
    g_3 = -6/v
    g = g_1+g_2+g_3
    p_1 = 8*t/(3*v-1)
    p_2 = -3/v**2
    p = p_1 + p_2
    plt.plot(p,g)
    plt.xlabel("Reduced pressure")
    plt.ylabel("Gibbs reduced")
    est_p = 0.3823
    plt.plot([est_p,est_p],[-5.8,-6.8], "k--")
    plt.axis([-0.5,2,-5,-7])
    plt.suptitle("Reduced Gibbs v Pressure at t = 0.8")
    plt.show()
    
gibbs(t)
