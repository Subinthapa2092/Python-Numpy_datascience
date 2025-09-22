import numpy as np 

"""
reshape(rows, columns) for specify new shape
if dimensions match 
Reshaping does not create copy it creates view 
Flatting Array : ravel() and flatten()
When you want to coverst multi dimension to one dimension array: 
"""
arr = np.array([[20,30,40,50,90,100],[20,30,40,90,70,80]])
result = arr.ravel()
result1 = arr.flatten()
print(result1)
print(result)
# result = arr.reshape(3,2)
# print(result)