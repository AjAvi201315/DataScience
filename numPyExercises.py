import numpy as np
# 2. How to create a 1D array
arr = np.arange(10)
print(arr)
#3. How to create a boolean array?
bool_arr = np.full((3, 3), True, dtype=bool)
# or use np.ones((3,3), dtype=bool)
print(bool_arr)
#4. How to extract items that satisfy a given condition from 1D array?
mod_one = arr[arr % 2 == 1]
print(mod_one)
#5. How to replace items that satisfy a condition with another value in numpy array?
neg_arr = arr[arr % 2 == 1] = -1
print(neg_arr)