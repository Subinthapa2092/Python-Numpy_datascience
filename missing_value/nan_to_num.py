#### Python in a program to do the Handle Missing Values Work's 

import numpy as np 

arr = np.array([1,2,3,np.nan,4,5,6,np.nan,np.nan])
cleaned_value = np.nan_to_num(arr)
print(cleaned_value)