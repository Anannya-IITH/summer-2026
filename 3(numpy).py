import numpy as np
from numpy import pi
a=np.arange(5,15,)
print(a)
b=np.linspace(2,4,9)
print(b)
x=np.linspace(0,2*pi,12)
c=np.sin(x)
print(c)
#np.arange(x,y,z): means from x till y (y excluded), leaving a gap of z
#np.linspace(x,y,z): means from x till y (y excluded), dividing the range into z parts