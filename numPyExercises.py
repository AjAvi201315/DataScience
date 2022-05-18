import numpy as np
read = "I read the first X (X>=25) exersises"
print(read)
# 2. How to create a 1D array
arr = np.arange(10)
print(arr)
# 3. How to create a boolean array?
bool_arr = np.full((3, 3), True, dtype=bool)
# or use np.ones((3,3), dtype=bool)
print(bool_arr)
# 4. How to extract items that satisfy a given condition from 1D array?
mod_one = arr[arr % 2 == 1]
print(mod_one)
# 5. How to replace items that satisfy a condition with another value in numpy array?
neg_arr = arr[arr % 2 == 1] = -1
print(neg_arr)
# 6. How to replace items that satisfy a condition without affecting the original array?
neg_arr2 = np.where(arr % 2 == 1, -1, arr)
print(neg_arr2)
# 7. How to reshape an array?
arr = np.arange(10)
reshape_arr = arr.reshape(2, -1)
print(reshape_arr)
# 8. How to stack two arrays vertically?
arr_one = np.repeat(1, 10).reshape(2, -1)
reshape_arr_v1 = np.concatenate([reshape_arr, arr_one], axis=0)
print(reshape_arr_v1)
reshape_arr_v2 = np.vstack([reshape_arr, arr_one])
print(reshape_arr_v2)
reshape_arr_v3 = np.r_[reshape_arr, arr_one]
print(reshape_arr_v3)
# 9. How to stack two arrays horizontally?
reshape_arr_h1 = np.concatenate([reshape_arr, arr_one], axis=1)
print(reshape_arr_h1)
reshape_arr_h2 = np.hstack([reshape_arr, arr_one])
print(reshape_arr_h2)
reshape_arr_h3 = np.c_[reshape_arr, arr_one]
print(reshape_arr_h3)
# 10. How to generate custom sequences in numpy without hardcoding?
arr2 = np.array([1, 2, 3])
arr_seq = np.r_[np.repeat(arr2, 3), np.tile(arr2, 3)]
print(arr_seq)
# 11. How to get the common items between two python numpy arrays?
a_arr = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b_arr = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
arr_inter = np.intersect1d(a_arr, b_arr)
print(arr_inter)
# 12. How to remove from one array those items that exist in another?
a_arr = np.array([1, 2, 3, 4, 5])
b_arr = np.array([5, 6, 7, 8, 9])
arr_diff = np.setdiff1d(a_arr, b_arr)
print(arr_diff)
# 13. How to get the positions where elements of two arrays match?
a_arr = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b_arr = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
arr_index_match = np.where(a_arr == b_arr)
print(arr_index_match)
# 14. How to extract all numbers between a given range from a numpy array?
a_arr = np.array([2, 6, 1, 9, 10, 3, 27])
a_num1 = np.where((a_arr >= 5) & (a_arr <= 10))
print(a_arr[a_num1])
a_num2 = np.where(np.logical_and(a_arr >= 5, a_arr <= 10))
print(a_arr[a_num2])
a_num3 = a_arr[(a_arr >= 5) & (a_arr <= 10)]
print(a_num3)
# 15. How to make a python function that handles scalars to work on numpy arrays?
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])
a_arr = np.array([5, 7, 9, 8, 6, 4, 5])
b_arr = np.array([6, 3, 4, 8, 9, 7, 1])
pair_arr = pair_max(a_arr, b_arr)
print(pair_arr)
# 16. How to swap two columns in a 2d numpy array?
arr = np.arange(9).reshape(3, 3)
arr_swap = arr[:, [1, 0, 2]]
print(arr_swap)
# 17. How to swap two rows in a 2d numpy array?
arr = np.arange(9).reshape(3, 3)
arr_swap2 = arr[[1, 0, 2], :]
print(arr_swap2)
# 18. How to reverse the rows of a 2D array?
arr = np.arange(9).reshape(3, 3)
arr_reverse = arr[::-1]
print(arr_reverse)
# 19. How to reverse the columns of a 2D array?
arr = np.arange(9).reshape(3, 3)
arr_reverse2 = arr[:, ::-1]
print(arr_reverse2)
# 20. How to create a 2D array containing random floats between 5 and 10?
arr = np.arange(9).reshape(3, 3)
arr_rand1 = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
print(arr_rand1)
arr_rand2 = np.random.uniform(5, 10, size=(5, 3))
print(arr_rand2)
# 21. How to print only 3 decimal places in python numpy array?
rand_arr = np.random.random((5, 3))
#rand_arr = np.random.random([5, 3])
# Limit to 3 decimal places
np.set_printoptions(precision=3)
arr_limit = rand_arr[:4]
#print('arr_limit')
print(arr_limit)
# 22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
np.set_printoptions(suppress=True, precision=6)
print(rand_arr)
# 23. How to limit the number of items printed in output of numpy array?
arr = np.arange(15)
np.set_printoptions(threshold=6)
print(arr)
# 24. How to print the full numpy array without truncating
np.set_printoptions(threshold=6)
arr = np.arange(15)
np.set_printoptions(threshold=np.nan)
print(arr)
# 25. How to import a dataset with numbers and texts keeping the text intact in python numpy?
# url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# iris_small = iris[:3]
# print(iris_small)