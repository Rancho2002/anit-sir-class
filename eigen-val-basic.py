# import numpy library
import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,8]])

# importing linalg function from scipy
from scipy import linalg

# Compute the determinant of a matrix
print(linalg.det(A))


# Compute pivoted LU decomposition of a matrix

P, L, U = linalg.lu(A)
print(P)
print(L)
print(U)
# print LU decomposition
print(np.dot(L,U))

# Solving eigen_values, eigen_vectors
eigen_values, eigen_vectors = linalg.eig(A)
print(eigen_values)
print(eigen_vectors)

# Solving systems of linear equations 

v = np.array([[2],[3],[5]])
print(v)
s = linalg.solve(A,v)
print(s)

#Sparse Linear Algebra
# import necessary modules
from scipy import sparse
# Row-based linked list sparse matrix
A = sparse.lil_matrix((1000, 1000))
print(A)

A[0,:100] = np.random.rand(100)
A[1,100:200] = A[0,:100]
A.setdiag(np.random.rand(1000))
print(A)


#Linear Algebra for Sparse Matrices

from scipy.sparse import linalg

# Convert this matrix to Compressed Sparse Row format.
A.tocsr()

A = A.tocsr()
b = np.random.rand(1000)
ans = linalg.spsolve(A, b)
# it will print ans array of 1000 size
print(ans)




