##### Python in a program to Start the Numpy: 

import numpy as np 
### 1 dimension Array
# ar_1d = np.array([10,20,30,40,50])
# print(ar_1d)
# #### 2 dimension Array 
# ar_2d = np.array([[1,2,3,4],
#                   [2,3,4,5],
#                   [3,4,5,6]]
#                   )
# print(ar_2d)
#### Multi Dimension Array 
### Maxtrix 
# matrix  = np.array([[2,4,6],
#                    [7,8,9]]
#                    )
# print(type(matrix))

'''
[1,3,4] ### Rows and Columns 

'''

### Creating arrays From the Python lists 
### np.array([ele1,ele2,ele3])

# num1 = [[2,3,5,7],[5,8,9,0]]
name = [["Subin Thapa",18,"Dhading"],["Ramesh",20,"World"]]
result = np.array(name)
print(type(result))
print(type(name))
print(result)
# print(type(num1))
# print(type(result))
# print(type(num1))
