import time
import numpy as np

def foo():
    time.sleep(5)
    return np.loadtxt("input.csv", dtype=int)

def bar():
    x = np.random.random((500,500))
    return x*x
