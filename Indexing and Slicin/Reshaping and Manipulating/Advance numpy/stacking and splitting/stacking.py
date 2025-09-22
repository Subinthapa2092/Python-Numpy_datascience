#### i will do the stacking and spliting in this code: 
### Vertically 
### Horizontally 
## vstack() row wise 
##hstack() column wise 
import numpy as np 

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
result1 = np.hstack(((arr1,arr2))) ### 1 dimension work
result2 = np.vstack(((arr1,arr2)))### 2 dimension  work 
print(result1)
print(result2)