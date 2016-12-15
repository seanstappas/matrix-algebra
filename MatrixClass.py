## The Matrix Class and its helper functions
## Created by Sean Stappas and George Theophanous
## 12/05/14

class Matrix(object):
    """ The Matrix object """

    def __init__(self, list_of_lists):
        """ To initialize, the user must give a 2D list of lists, which is normalized """
        self.matrix = normalize(list_of_lists) # Helper normalize function, defined at end.

    def __add__(self, other):
        """ Addition of matrices """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print("Cannot add matrices of different size!")
            
        else:
            return Matrix([ [self.matrix[j][i] + other.matrix[j][i] for i in range(len(self.matrix[0]))] \
                            for j in range(len(self.matrix))])

    def __sub__(self, other):
        """ Subtraction of matrices """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print("Cannot subtract matrices of different size!")
        else:    
            return Matrix([ [self.matrix[j][i] - other.matrix[j][i] for i in range(len(self.matrix[0]))] \
                            for j in range(len(self.matrix))])
    
    def __mul__(self, other):
        """ Multiplication of matrices """
        ## This was a tricky implementation and took some time to get from paper to code, but it ended up working nicely.

        if len(self.matrix[0]) != len(other.matrix):
            print("Cannot multiply those matrices!")

        else:
            finalList = []
            for i in range(len(self.matrix)): # Rows of self matrix
                
                subList = []
                for j in range(len(other.matrix[0])): # Columns of other matrix
                    res = 0
                    for k in range(len(self.matrix[0])): # Columns of self matrix
                        res += self.matrix[i][k] * other.matrix[k][j]
                    subList.append(res)    # Creating the sublists
                finalList.append(subList)  # Creating the final 2D list
            return Matrix(finalList)       # Creating a matrix object out of that 2D list

    def __pow__(self, power):
        """ Raising a matrix to a power """
        if len(self.matrix) != len(self.matrix[0]):
            print("The matrix must be square to raise it to a power!")
        else:
            res = identity(len(self.matrix)) # Assigning res to the identity matrix, instead of the usual integer 1 for this type of
                                             # loop, since we're multiplying matrices and not integers.
            for i in range(power):
                res *= self       # Calling the __mul__ method repeatedly
            return res

    def __rmul__(self, other):
        """ This is essentially scalar multiplication where 'other' is a scalar.
The scalar must be placed in front (to the left) of the matrix when multiplying, however."""
        return Matrix([ [ other * self.matrix[j][i] for i in range(len(self.matrix[0])) ] \
                     for j in range(len(self.matrix)) ])
    
    def __repr__(self):
        """ The string representation of the matrix as a list of lists """
        return str(self.matrix)
    
    def prettyprint(self):
        """  Pretty prints the matrix, with the brackets removed """
        for row in self.matrix:
            for el in row:
                print("%10.1f" % el, end = "") # Some precision is lost for the sake of aesthetics
            print()

    def trans(self):
        """ Transposes the matrix in place, modifying the original matrix. """
        self.matrix = [ [self.matrix[r][c] for r in range(len(self.matrix))] for c in range(len(self.matrix[0]))]
    
    def getTrans(self):
        """ Returns the transpose of the matrix without changing the original matrix """
        return Matrix([ [self.matrix[r][c] for r in range(len(self.matrix))] for c in range(len(self.matrix[0]))])
    
    def subMatrix(self, row = -1, column = -1):
        """ Returns a submatrix of a, with a specified row and/or column removed. Default: nothing removed """
        column_indices = list( range( len(self.matrix[0]) ) ) # list of column indices
        row_indices = list( range( len(self.matrix) ) )       # list of row indices
        if column >= 0: column_indices.remove(column)  # removes the given column index from the list of column indices
        if row >= 0: row_indices.remove(row)           # removes the given row index from the list of row indices
        return Matrix([ [ self.matrix[j][i] for i in column_indices ] for j in row_indices ]) # Creates a new matrix with the column and
                                                                                              # row removed

    def cofactors(self):
        """ Returns a copy of the cofactor matrix """
        return Matrix([ [ (-1)**(i+j) * self.subMatrix(j,i).det for i in range(len(self.matrix[0])) ] \
                        for j in range(len(self.matrix)) ]) # Easy translation from mathematical definition

    def inverse(self):
        """ Inverses the matrix in place, modifying the original matrix. """
        if self.isInvertible:
            self.matrix = ( (1/self.det)*(self.cofactors().getTrans()) ).matrix # Easy translation from mathematical definition
        else:
            print("That matrix isn't invertible")

    def getInverse(self):
        """ Returns the inverse of the matrix without changing the original matrix """
        if self.isInvertible:
            return (1/self.det)*(self.cofactors().getTrans())
        print("That matrix isn't invertible")
    
    def rowEchelon(self):
        """ Reduces the matrix to row echelon form """
        ### Algorithm inspired from wikipedia article on Gaussian Elimination:
        ### http://en.wikipedia.org/wiki/Gaussian_elimination#Pseudocode
        
        for k in range(len(self.matrix)):
            for i in range(k, len(self.matrix) ):
                if abs(self.matrix[i][k]) == max( abs(self.matrix[i][k]) for i in range(k, len(self.matrix)) ):
                    i_max = i  # This is the 'pivot' for column k
            
            swapRows(self.matrix, k, i_max)
            for i in range(k + 1, len(self.matrix) ):        # For all rows below pivot
                for j in range(k + 1, len(self.matrix[0]) ): # For all remaining elements in current row
                    self.matrix[i][j] -= self.matrix[k][j]*( self.matrix[i][k] / self.matrix[k][k] )
                self.matrix[i][k] = 0                        # Fill lower triangular matrix with zeros

    def reduce(self):
        """ Reduces the matrix to reduced row echelon form """
        self.rowEchelon()
        for i in range(len(self.matrix) - 1, -1, -1):  # Works backwards from the last row up
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != 0:      # if the number is a leading coefficient...
                    listDivide(self.matrix[i], self.matrix[i][j]) # Helper global listDivide function. This divides
                                                                  # every element of the row by the leading coefficient,
                                                                  # turning the leading coefficient into a 1
                    for k in range(i):
                        rowAdd(self.matrix,k, i, -self.matrix[k][j]) # This subtracts a corresponding multiple of the row from
                                                                     # all the other rows, as should be done when reducing a
                                                                     # matrix
                    break # The break allows the function to ONLY look at the leading coefficient, and not the
                          # rest of the numbers in the row.

    def append(self, other):
        """ Appends a matrix 'other' to the right of a matrix 'self' """
        for i in range(len(self.matrix)):
            self.matrix[i] += other.matrix[i] # Python's built-in list addition helps here

    @property
    def isInvertible(self):
        """ Returns True if the matrix is invertible """
        return len(self.matrix) == len(self.matrix[0]) and self.det != 0
    
    @property
    def det(self):
        """ Returns the determinant of the matrix """
        res = 0
        if len(self.matrix) != len(self.matrix[0]):  # Making sure the matrix is square
            print("Can only take the determinant of a square matrix!")
            return
        
        if len(self.matrix) == 1:
            return self.matrix[0][0] # The determinant of a matrix of one element is just that element. This is needed for
                                     # computing the cofactor matrix for a 2x2 matrix.
                                     
        if len(self.matrix) == 2:    # Base case of the recursion (for a 2x2 matrix)
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        
        for i in range(len(self.matrix[0])-1): # Expanding along the first row
            res += ((-1)**i) * self.matrix[0][i] * self.subMatrix(0,i).det # Recursion here, as well as a helper function!
            
        return res

## Some global helper functions:

def identity(n):
        """ Returns the identity matrix of size n """
        return Matrix([ [ int(i==j) for i in range(n) ] for j in range(n) ])
    

def normalize(a):
    """ Normalizes a 2D list 'a', if there is an inconsistent number of elements
for every row """
    rows = len(a)                                   # The number of rows
    columns = max([len(a[i]) for i in range(rows)]) # The maximum of columns
    for i in range(rows):
        while len(a[i]) != columns:
            a[i].append(0) # Adds a zero at every position where there is an element missing in the matrix
    return a

def listDivide(lst, n):
    """ Divides each element of a list by n """
    for i in range(len(lst)):
        lst[i] /= n

def listAdd(lst, n):
    """ Add n to each element of a list """
    for i in range(len(lst)):
        lst[i] += n

def swapRows(lst, row1, row2):
    """ Swaps two rows in a 2D list (or two elements in a list)"""
    lst[row1], lst[row2] = lst[row2], lst[row1]

def rowAdd(lst, row1, row2, multiple):
    """ Adds a multiple of row2 to row1 in a 2D list """
    for i in range(len(lst[row1])):
        lst[row1][i] += multiple*lst[row2][i]

