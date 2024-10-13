import numpy as np
a = np.array(np.linspace(1.0, 100.0, 100))
b = np.reshape(a, (10, 10))
row = np.array2string(b, separator=', ')
print(row)
