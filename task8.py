import numpy as np

a = np.array(np.linspace(1.0 , 100.0, 100))

b= a.reshape(100, 1)
print(b.shape)
print(b)