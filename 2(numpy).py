import numpy as np
a=np.arange(10)**3
print(a)
print(a[2])
print(a[2:6])
a[0:6:2]=1000
print(a)