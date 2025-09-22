#### Python in a program to do the Remove or delete in the pythons

import numpy as np 

### np.delete(array,index,axis = None) will delete the number 
### flattern array 
### Single Dimension
arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr)
result = np.delete(arr,5)
print(result)
### Double Dimension 

arr1 = np.array([[1,2,3],[5,6,7]])
result = np.delete(arr1,0,axis = 0)
print(result)