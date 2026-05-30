import numpy as np
a=np.arange(10)**3
print(a)
print(a[2])
print(a[2:6])
a[0:6:2]=1000
print(a)
# if only 1 number in brackets in np.arange, that means one-dimension, 
# starting from zero till the number, the number excluded
# similarly, if written as np.arange(x).reshape(y,z): it indicates x=y*z, 
# it is a 2 dimensional array, and its shape is y*z