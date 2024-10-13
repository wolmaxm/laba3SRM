import numpy as np
a = np.random.rand(10,10)* 100
max1= np.max(a, axis=0)
min1= np.min(a, axis=0)
max2= np.max(a, axis=1)
min2= np.min(a, axis=1)
print(max1)
print(min1)
print(max2)
print(min2)
