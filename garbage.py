import time
import numpy as np
time.sleep(5)
data = np.loadtxt("sample.csv", dtype=int)
x = np.random.random((500,500))
print(x*x)
print(data)
