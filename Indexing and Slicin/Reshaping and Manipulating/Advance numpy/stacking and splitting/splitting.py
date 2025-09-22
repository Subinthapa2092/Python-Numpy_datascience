#### 
import numpy as np 

"""
np.split() it split into the equal 
np.hsplit() horizontal
np.vsplit() vertical 
"""

arr = np.array([[1,2,3,4,5,7],[5,6,7,8,9,10]])

# print(np.split(arr,3))
# print(np.hsplit(arr,3))
print(np.hsplit(arr,2))