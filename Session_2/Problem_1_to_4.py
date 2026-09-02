import numpy as np

# %% Solution 1 #
# Numpy Array containing numbers from 1 to 10
arr = np.array([])
for i in range(1, 11, 1):
    arr = np.append(arr, i)
# Finding Mean #
mean_arr = np.mean(arr)
print(mean_arr)
# Finding Maximum #
max_arr = np.max(arr)
print(max_arr)
# Finding Minimum #
min_arr = np.min(arr)
print(min_arr)

# %% Solution 2 #
arr = np.array([10, 20, 30, 40, 50])
# Accessing the third element #
third_ele = arr[3]
print(third_ele)
# Get the first three elements #
for i in range(0,3,1):
    print(arr[i])
# Replace 30 with 35 #
arr[np.isin(arr,30)] = 35
print(arr)

# %% Solution 3 #
arr = np.arange(1,10).reshape(3,3)
# Calculate Shape #
print(arr.shape)
# Sum of all elements #
print(np.sum(arr))
# Sum of each row #
row_1 = np.sum(arr, axis=1)
print('Row 1 =',row_1[0])
print('Row 2 =',row_1[1])
print('Row 3 =',row_1[2])

# %% Solution 4 #
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Element 5 from array #
index = int(input("Enter index for access:"))
row = index // arr.shape[1]
col = index % arr.shape[1]
print(arr[row,col])
# Last column #
last = []
last_col = [row[-1] for row in arr]
for i in last_col:
    last.append(int(i))
print(last)
# Second Column #
sec_row = arr[1]
print(sec_row)
