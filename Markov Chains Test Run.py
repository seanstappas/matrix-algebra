from MatrixClass import *

print("A study was conducted in a large wooded area, where there are two lakes.  Each year, 20% of beavers from lake 1 migrate to lake 2 and 10% migrate from lake 2 to lake 1.")
print("This system can be represented in a 2x2 P matrix, where the [i][j] entries represent a beaver going from lake(or state)[j] to lake(or state)[i] in one year.")
P1=[[8/10, 1/10],[2/10, 9/10]]
P=Matrix(P1)
print()
print("The matrix P here is")
P.prettyprint()
print("At the start of the study, 30% of baevers are in lake 1 and 70% in lake 2. This is the original state vector Vo")
V=[[0.30],[0.70]]
Vo=Matrix(V)
Vo.prettyprint()
print("By conducting the operation P x Vo, we may see the spread of beavers among the lakes after one year:")
res1= P * Vo
res1.prettyprint()
print("To find P^k, the change on a long term, we will use eigan values. lambda is an eigan value of matrix P if it solves the system PV=lambdaV for a matrix v.")
print("Thus, we obtain (P-lambda*Identity matrix)*V=0.")
print("Doing this allowed us to get eigan values lambda1=1.0 and lambda2=0.7.")
print("substituting the value lambda1 into the formula gives us a system to solve:")
system=P+((-1)*identity(2))
system.prettyprint()
print("Setting it equal to 0 and multiplying the first row by -5:")
system=system*Matrix([[-5,1],[-5,1]])
system.prettyprint()
print("Then cancelling the rows out gives")
system=system+Matrix([[0.0,0.0],[0.5,-0.1]])
system.prettyprint()
print("With this, we may see that v2=t and v1=0.5v2=0.5t, so the eigan vector corresponding to the eigan value lambda2=1 is")
eigan=[[1/2],[1/1]]
eigan_vector=Matrix(eigan)
eigan_vector.prettyprint()
print("Repeating this entire process (repalcing lambda into the formula) again but with lambda2=0.7:")
print("P-lambda1*identitymatrix=")
system2=P+((-0.7)*identity(2))
system2.prettyprint()
print("row 2 minus row 1")
system2=system2*Matrix([[1,0],[-2,1]])
system2.prettyprint()
print("v2=t, and v1=-v2=-t, so eigan vector 2 is")
eigan=[[-1],[1]]
eigan_vector2=Matrix(eigan)
eigan_vector2.prettyprint()
print("placing them side by side, we obtain the eigan matrix")
eigan=[[1/2,-1],[1,1]]
eigan_matrix=Matrix(eigan)
eigan_matrix.prettyprint()
print("now consider A=eigan matrix, so (A^(-1))*(P)*(A)=:")
D1=eigan_matrix.getInverse()
D2=D1*P
D3=D2*eigan_matrix
Diagonalised_matrix=D3
Diagonalised_matrix.prettyprint()
