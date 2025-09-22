####3 Python in a program to do the 
"""
   np.insert(array, index, value, asix = None)
   array - original array 
   index = 
   value =
   axis =  
   axis =0,row = wise
   1 column wise
""" 

import numpy as np 
# arr_d = np.array([10,20,30,40,50])

# result = np.insert(arr_d,2,100)
# print(result)
arr_d1 = np.array([[10,30],[40,40]])
print(arr_d1)
result1 = np.insert(arr_d1,2,[5,6],axis = None) ### axis = 1 is the colunms wise and the axis = 0 is the row wise 
print(result1)
### 