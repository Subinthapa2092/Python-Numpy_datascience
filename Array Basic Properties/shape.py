#### python in a program to look the Shape of the python's 

import numpy as np 

arr_2d = np.array([[1.2,2.6],
                  [5.0,7.2],[2,5]])
# ### Result and the Imp of the arr_2d 
# print(arr_2d.shape) ## Row's and the Columns 
# print(arr_2d.size) ### Size of the array 
# print(arr_2d.ndim) ### No. of the Dimension
# print(arr_2d.dtype) ##3 Type of the Array 
# result = arr_2d.astype(float)
print(arr_2d.ravel()) ### ravel change the 2d or nd into 1d 
print(arr_2d.reshape(2,3)) ### Reshape change the shape of the Array 
print(arr_2d.T) ### Transpose the array 
print(arr_2d.itemsize) ### Size of One Element in bytes 
print(arr_2d.nbytes)