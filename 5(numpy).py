import numpy as np
rg=np.random.default_rng(1)
a=np.floor(10 * rg.random((3,8)))
print(a)
print(a.ravel())
print(a.reshape(4,6))
print(a.T)
a.resize((2,12))
print(a)
#floor puts the highest value below which the integers can be chosen at random
#ravel flattens the array
#reshape changes the shape of the array
#T gives the transpose of the matrix/array