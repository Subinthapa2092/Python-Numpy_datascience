##### Python in a program to do the Indexing and  Slicing in the python : 

### Single Line:  is used for the single row
### Slicing where doubble line start, stop, step,
### Fancing indexing, Boolean masking
### fancy indexing is the selecting multiple elements at once 
import numpy as np 

#### Fancy Array in the Python : 
arr = np.array([10,20,30,40,50,60])

print(arr[[0,2,4]])
#### Boolean Masking in the Python -: 
### Condition Gives the result such as True andFalse 
result = arr[arr>25]
print(result)