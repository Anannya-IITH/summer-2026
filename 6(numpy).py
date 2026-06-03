import numpy as np
rg=np.random.default_rng(1)
a= np.floor(10*rg.random((3,3)))
print(a)
b= np.floor(10* rg.random((3,3)))
print(b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
#vstack vertically puts the matrices together, shape in this example becomes 6,2
#hstack horizontally puts the matrices together, side by side, shape in this example becomes 3,4
print(np.hsplit(a,3))
print(np.vsplit(a,3))