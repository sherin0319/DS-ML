print("SHERIN MATHEW")
print("21MCA039")

import numpy as np

A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
#B = np.array([ [3, 2, 1], [1, 2, 3], [1, 2, 3] ])

arrA = np.multiply(A,A)
print("The multiply od matrix is :")
print(arrA)

arrB = np.power(A, 3)
print("The power of each matrix is :")
print(arrB)

arrC = np.identity(3)
print("The identity matrix is :")
print(arrC)

arrD = np.power(A,3)
print("Power of each element of matrix is : ")
print(arrD)

arrE=np.power(A,2)
print("Element wise power os the matrix is :")
print(arrE)