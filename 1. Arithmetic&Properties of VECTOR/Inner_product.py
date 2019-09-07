import numpy as np

# case 1: 1-D array as an input to np.dot
# elements of vectors a and b
a1, a2, b1, b2 = 1, 2, 3, 4

# initialize vectors a and b by a1~b2
a = np.array([a1, a2])
b = np.array([b1, b2])

# calculate the dot product for input vectors
dot_prod = np.dot(a, b)

# if both input vectors are 1-D arrays, then the function 'np.dot()' returns the inner product of input vectors
print('1-D Arrays as an input to np.dot')
print(
    'Dot product of vectors a = [a1, a2] = [{},{}] and b = [b1, b2] = [{}, {}] is {}\n'.format(a1, a2, b1, b2, dot_prod))

# case 2: 2-D array(matrix) as an input to np.dot
# define row vectors for matrix a and b whose size is 2x2
row_vecs = np.resize(np.arange(1, 9), (4, 2))

# initialize matrix a and b by row vectors
a = np.array([row_vecs[0], row_vecs[1]])
b = np.array([row_vecs[2], row_vecs[3]])

# calculate the dot product for input matrix
dot_prod = np.dot(a, b)

# if both inputs are 2-D array, then the function 'np.dot()' perform the matrix multiplication(also called matrix product) which is identical to np.matmul()
print('2-D Arrays(Matrix) as an input to np.dot')
print(
    'Dot product of Matrix a = [a1, a2] = [{},{}] and b = [b1, b2] = [{}, {}] is {}'.format(row_vecs[0], row_vecs[1],
                                                                                            row_vecs[2], row_vecs[3],
                                                                                            dot_prod))
