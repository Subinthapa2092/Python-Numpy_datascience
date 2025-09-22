#### python in a program --:--: 
'''
array[index]# 1d array
array[row,column]## 2d array
'''
import numpy as np 

arr = np.array([10,20,30,40,50])
### Display the result
print(arr[0])
print(arr[-1])
#### Slicing in the python: 
print(arr[-1:-5:1])
print(arr[::2])