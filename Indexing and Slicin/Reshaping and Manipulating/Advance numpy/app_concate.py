##### Python in a program to do the Other Process's 

import numpy  as np 
### Append is used for the adding the element at the end's 

arr = np.array([10,20,30,40])
#### (arr(variable,value))
result = np.append(arr,[30])
print(result)
#### python in a program to do the concentrating two array: 

arr1 = np.array([[2,3,4,5],[5,6,8,9]])
arr2 = np.array([[5,6,7,8],[2,3,4,5]])
result = np.concatenate((arr1,arr2),axis =1)
### axis 0 > vertical stacking
### axis 1 > horizontal stacking
print(result)