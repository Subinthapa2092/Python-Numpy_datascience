#### Python in a program to do the brocasting calculation process 

import numpy as np 
#### Creating the Calculation: 
arr = np.array([10,20,30,40,50])
discount = 10 
### Calculation: Just the Formula for it's
result = arr - (arr*discount/100)
### Displaying the Result 
print(result)