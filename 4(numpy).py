import numpy as np
rg=np.random.default_rng(1)
a=np.ones((2,3), dtype=np.int_)
b=rg.random((2,3)) 
a*=3
print(a)
b+=a
print(b)
c=rg.uniform(low=0.0, high=10.0, size=(2,3))
d=rg.integers(low=1, high=9, size=(2,3))
c+=a
print(c)
d*=a
print(d)
# rg.random: gives random floats from 0.0-1.0 only, cuz it is the default
# rg.uniform: allows custom range to generate floats
# rg.integers: allows custom range, to generate only integers