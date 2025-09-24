##### Python in a program to do the Numpy program error if incompatible shape 

import numpy as np 

arr1 = np.array([[1,2,3],[4,5,6]])
arr3 = arr1.reshape(1,6)
print(arr3)
arr2 = np.array([1,2])
result = arr3+arr2 
print(result)