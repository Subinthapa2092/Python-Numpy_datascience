#### python in a program to to do the Broadcasting
## Mathematical Operations: 
# import numpy as np 

# arr = np.array([90,180,270])
prices = [100,200,300,600,900.50]

discount = 10 ## 10% after the discount price's 

final_prices = []

for i in prices: 
    final_price = i - (i*discount/100)
    final_prices.append(final_price)
print(final_prices)
### Broadcasting is a numpy way where different shape we perform the operation without using the loop's 
### without needed the for loops and program will be easy and fast : 

import numpy as np

prices = np.array([100,200,300,400])
discount = 10 

final_prices1 = prices -(prices*discount/100)
print(final_prices1)
### Matching Dimension: 

### Expanding Single Element

### Incompatible Shapes