import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    y = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*y)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    y = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*y)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    y = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*y)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    a1 = NAND(x1, x2)
    a2 = OR(x1, x2)
    y = AND(a1, a2)
    return y
