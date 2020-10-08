import numpy as np
from math import atan2
'''
Mind :
t11 = t23 = t14
t21 = -t13 = t24
'''


def read_xyz():
    result = []
    x = input("Enter x : ")
    result.append(float(x))
    y = input("Enter y : ")
    result.append(float(y))
    z = input("Enter z : ")
    result.append(float(z))
    return result

def calculus_qi(t, epsilon=1):
    result = []
    if(t[0][0] == 0 and t[1][0] == 0):
        q1 = atan2((epsilon*t[0][3])/(np.sqrt(t[0][3]**2+t[1][3]**2)),((-1)*epsilon*t[1][3])/(np.sqrt(t[0][3]**2+t[1][3]**2)))
    else :     
        q1 = atan2((epsilon*t[0][0])/(np.sqrt(t[0][0]**2+t[1][0]**2)),((-1)*epsilon*t[1][1])/(np.sqrt(t[0][0]**2+t[1][0]**2)))
    result.append(q1)
    q2 = (-1) * t[0][3] * np.sin(q1) + t[1][3] * np.cos(q1)
    result.append(q2)
    q3 = atan2(t[0][0]*np.sin(q1)-t[1][0]*np.cos(q1),t[2][1])
    result.append(q3)
    return result

def test():
    m = np.array([[ 0.,  0.,  1.,  0.], [ 0., -1.,  0.,  2.], [ 1.,  0.,  0.,  2.],[ 0.,  0.,  0.,  1.]])
    q = calculus_qi(m,epsilon=-1)
    print(q)
    return

test()