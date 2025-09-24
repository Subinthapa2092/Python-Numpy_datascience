#### np.isinf() 10*1000
### python in a program to do or display the Infinite Number 

import numpy as np 

arr = np.array([1,2,np.inf,4,5,-np.inf,6,9,10,np.inf])

print(np.isinf(arr))
cleaned_values = np.nan_to_num(arr,posinf=50,neginf=40)
print(cleaned_values)