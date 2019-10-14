
import pprint # In order to print matrices prettier
import scipy as sc
import scipy.linalg # Linear Algebra Library contained in Scipy


matrix_A = sc.array([[7,4],[3,5]]) # given matrix A
P, L, U = scipy.linalg.lu(matrix_A) # returns the result of LU decomposition to the variables P, L, and U

print("Original matrix A:")
pprint.pprint(matrix_A)

# implies a pivoting(reordering) rows(or columns) in case it is needed
print("Pivoting matrix P:")
pprint.pprint(P)

# lower-triangular matrix of A
print("L:")
pprint.pprint(L)

# upper-triangular matrix of A
print("U:")
pprint.pprint(U)