print("SHERIN MATHEW")
print("21MCA039")
import numpy as np
np.random.seed(42)
A = np.random.randint(0, 10, size=(2, 2))
B = np.random.randint(0, 10, size=(2, 3))
C = np.random.randint(0, 10, size=(3, 3))
print("Matrix A:\n{}\n".format(A))
print("Matrix B:\n{}\n".format(B))
print("Matrix C:\n{}\n".format(C))
D = np.matmul(np.matmul(A, B), C)
print("Result of multiplication in the order (AB)C:\n\n{}\n".format(D))