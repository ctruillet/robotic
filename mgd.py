import numpy as np

'''
Mind :
In numpy, trigonometric functions take radians as arguments
'''

def read_q_list():
    result = []
    for i in range(3):
        qi = input("Enter q" + str(i+1) + " : ")
        result.append(float(qi))
    return result


def t03_calculus(q_list, m):

    #q list
    q1 = q_list[0]
    q2 = q_list[1]
    q3 = q_list[2]

    #cos(q)
    c1 = np.cos(q1)
    c3 = np.cos(q3)

    #sin(q)
    s1 = np.sin(q1)
    s3 = np.sin(q3)

    #fill T03 : left -> right | top -> bottom
    result = np.zeros((4,4))

    result[0][0] = s3 * s1
    result[0][1] = s1 * c3
    result[0][2] = c1
    result[0][3] = (-1) * s1 * q2

    result[1][0] = (-1) * s3 * c1
    result[1][1] = (-1) * c1 * c3
    result[1][2] = s1
    result[1][3] = c1 * q2

    result[2][0] = c3
    result[2][1] = (-1) * s3
    result[2][3] = m

    result[3][3] = 1
    
    return result

def t04_calculus(q_list, m):
    t03 = t03_calculus(q_list, m)
    t34 = np.genfromtxt('t34.txt',delimiter=' ',encoding="utf8")
    return np.matmul(t03, t34)

def extract_xyz(t):
    result = []
    x = t[0][3]
    y = t[1][3]
    z = t[2][3]
    result.append(x)
    result.append(y)
    result.append(z)
    return result

def multiple_q_list():
    return

def test():
    l = read_q_list()
    m = input("Enter m : ")
    test = t04_calculus(l, float(m))
    print(test, "\n")
    xyz = extract_xyz(test)
    print(xyz)

test()