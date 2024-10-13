import numpy as np
a = np.array([-10,-20,-30,-45,-63,1,2,3,4,5,6])
sum= np.sum(a[a < 0 ])
print(sum)