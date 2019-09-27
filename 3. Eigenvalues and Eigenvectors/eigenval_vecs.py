import numpy as np

# Given matrix to find its eigenvalues and eigenvectors
matrix_A = np.array([[2, 4], [3, 7]])

# the function 'np.linalg.eig()' takes an matrix as an input and returns the eigenvalues and eigenvectors of given matrix
eig_vals, eig_vecs = np.linalg.eig(matrix_A)

print('The given matrix A:{}\n'.format(matrix_A))
print('Eigenvalues of the matrix A:{}'.format(eig_vals))
print('Eigenvectors of the matrix A:{}\n'.format(eig_vecs))


# diagonal matrix whose diagonal entries are the eigenvalues of A
diag_eig_vals = np.diag(eig_vals)

# inverse matrix of the matrix consisting its columns by eigenvectors
inv_eig_vecs = np.linalg.inv(eig_vecs)


print('The reconstructed matrix A by the eigendecomposition:{}'.format(np.dot(eig_vecs, np.dot(diag_eig_vals, inv_eig_vecs))))

