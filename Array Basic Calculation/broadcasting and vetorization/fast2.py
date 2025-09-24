#### 
import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([30,40,50])

result = arr1*arr2  
print(result)
#### Summary of the BroadCasting and Vectorization: 
### Broadcasting: smaller array to big array expands with 1d to 2d 
#### Speed is faster then loops 
### Vectorization is faster then loop 
### 100x faster then loop  and matrix operation's 