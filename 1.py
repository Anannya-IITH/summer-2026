import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[0, 1],[1, 0]])
C= A*B
D= A@B
E=A.dot(B)
print("A:",A,"\n","B:", B,"\n","C:", C,"\n","D:", D,"\n","E:", E)
