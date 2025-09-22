##### Python in a program to do the For loop's work 

### With the Default Values: 
### np.zeros(value) [3] fir id, [3,3] 2d 
import numpy as np 
### For the defualt Creation of Zero's Values : 
zero_values = np.zeros((5,2))
print(zero_values)
### For the Defualt Creation of one's Values: 
### For 0 values
eyes_value = np.eye(5) ### Used for making the Identity Matrix
print(eyes_value)
#### Python in   aprogram 
ones_array = np.ones((2,3)) ### Used for making the values row and columns ones
print(ones_array)

filledarray = np.full((2,3),7)
print(filledarray)