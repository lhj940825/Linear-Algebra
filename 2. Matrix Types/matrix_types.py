import numpy as np

# 1. square matrix is a type of matrix whose number of rows and cols are the same (n=m)
# in below example matrix 'M' has an order of 3 which denotes the size of matrix.
#       1  2  3
# M = [ 2  3  4 ]
#       3  4  5

square_M = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print("1. The Square Matrix M=\n{}".format(square_M))

# 2. symmetric matrix is a type matrix where the elements in top-right triangle of the matrix are identical to its bottom-left triangle.
#       1  2  3                       1  2  3                         1
# M = [ 2  3  5 ], top-right of M = [    3  5 ], bottom-left of M = [ 2  3   ]
#       3  5  4                             4                         3  5  4

symmetric_M = np.array([[1, 2, 3], [2, 3, 5], [3, 5, 4]])
print("2. The Symmetric Matrix M=\n{}".format(square_M))

# 3. triangular matrix is a type of square matrix that has all values in the upper-right or lower-left of the matrix with the remaining elements filled with zero values.
#       1  2  3             1  0  0
# M = [ 0  3  5 ], or M = [ 2  3  0 ]
#       0  0  4             3  5  4

M = np.array([[1, 2, 3], [2, 3, 5], [3, 5, 4]])

# np.triu is the function calculating the upper-triangular matrix of given parameter matrix and np.tril works the same to get the lower-trigular matrix
triangular_upper_M = np.triu(M)
triangular_lower_M = np.tril(M)
print("3. The Upper Triangular Matrix of M=\n{} and \nLower Triangular Matrix of M=\n{}".format(triangular_upper_M,
                                                                                                triangular_lower_M))

# 4. diagonal matrix is a type of matrix whose diagonal elements have values whereas the other elements are zero.
#       1  0  0
# D = [ 0  3  4 ]
#       0  0  5
# in vector form, it is written as D=(d11, d22, d33)

# np.diag() extracts a diagonal elements(vector) if given parameter is a matrix and creates a diagonal matrix when a dianogal vector is give.
diagonal_elements = np.diag(M)
diagonal_D = np.diag(diagonal_elements)
print("4. The Diagonal Elements of M=\n{} and \n The Diagonal Matrix =\n{}".format(diagonal_elements, diagonal_D))


# 5. identity matrix is a type of matrix where only its diagonal elements have values of '1'. It is often noted as 'I', and also called the 'unit matrix'
#       1  0  0
# I = [ 0  1  0 ]
#       0  0  1

# matrix size
m_size = 3

identity_matrix= np.identity(m_size)
print("5. The Identity Matrix I=\n{}".format(identity_matrix))

# 6. An orthogonal matrix is a type of square matrix whose columns and rows are orthogonal unit vectors.
# product(Q^T, Q) = product(Q . Q^T) = I

Q = np.array([[-1,0],[0,1]])
V = np.transpose(Q)
print("6. An Orthogonal Matrix Q = \n{} and its transposed matrix V = \n{}\n and since Q is orthogonal matrix, product of Q and V is identity matrix=\n{}".format(Q,V,np.matmul(Q,V)))
