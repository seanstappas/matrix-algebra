## Miscellaneous Test Runs. Press F5 to run.

from MatrixClass import *

print("Here is the matrix M:")
M = Matrix( [ [2,5,7], [8,5,2] ] )
M.prettyprint()

print()

print("Here is the matrix B:")
B = Matrix( [ [1,6,3], [2,4,2] ] )
B.prettyprint()

print()

print("M + B:")
(M + B).prettyprint()

print()

print("M - B:")
(M - B).prettyprint()

print()

print("The matrix B appended to M:")
A = Matrix( [ [1,6,3], [2,1,4] ] )
M.append(A)
M.prettyprint()

print()

print("Here is the matrix A:")
A = Matrix( [ [1,6,4], [2,1,5], [4,1,7] ] )
A.prettyprint()

print()

print("A**3:")
(A**3).prettyprint()

print()

print("M * A:")
M = Matrix( [ [2,5,7], [1,3,6] ] )
(M * A).prettyprint()

print()

print("Here is the identity matrix of size 3 (Call I):")
I = identity(3)
I.prettyprint()

print()

print("M * I:")
(M * I).prettyprint()

print()

print("5 * M:")
(5 * M).prettyprint()

print()

print("The transpose of M:")
M.getTrans().prettyprint()

print()

print("The determinant of A:")
print(A.det)

print()

print("The inverse of A:")
A.getInverse().prettyprint()

print()

print("M in row echelon form:")
M.rowEchelon()
M.prettyprint()

print()

print("M in reduced row echelon form:")
M = Matrix( [ [2,5,7], [8,5,2] ] )
M.reduce()
M.prettyprint()

print()

print("The cofactor matrix of A:")
A = Matrix( [ [1,6,4], [2,1,5], [4,1,7] ] )
A.cofactors().prettyprint()


