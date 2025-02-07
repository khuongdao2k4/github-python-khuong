#Vidu 40:
import numpy as np

# Assume diem_2a is a NumPy array containing student scores.
# For demonstration, let's create a sample array:
diem_2a = np.array([
    [9, 10],
    [10, 0],
    [10, 3]
])

# 1) Find and print the highest and lowest score for the class.
print('Điểm cao nhất của lớp:', diem_2a.max())
print('Điểm thấp nhất của lớp:', diem_2a.min())

print("-" * 30)

# 2) List the highest and lowest scores for each subject (row).
print("#2) Liệt kê điểm cao nhất và thấp nhất theo môn học")
for i in range(diem_2a.shape[0]):
    print('Môn', i, ': Điểm Max:', diem_2a[i,:].max(),
          ' -- Điểm Min:', diem_2a[i,:].min())
    
print("-" * 30)

# 3) List the highest and lowest scores for each student (column).
print("#3) Liệt kê điểm cao nhất và thấp nhất của mỗi học sinh")
for i in range(diem_2a.shape[1]):
    print('Học sinh', i, ': Điểm Max:', diem_2a[:,i].max(),
          ' -- Điểm Min:', diem_2a[:,i].min())
    
#Vidu41: 
import numpy as np

diem_2a = np.array([
    [5, 7, 9, 10, 6, 8, 4, 6, 8, 3],
    [3, 8, 7, 5, 10, 9, 7, 4, 5, 8],
    [10, 9, 4, 5, 8, 7, 6, 10, 4, 9],
    [7, 8, 6, 9, 10, 5, 8, 9, 4, 10],
    [7, 5, 9, 6, 8, 10, 7, 5, 8, 4],
    [6, 10, 9, 7, 8, 4, 5, 6, 9, 4],
    [8, 4, 6, 7, 9, 10, 5, 6, 7, 8],
    [3, 5, 6, 7, 8, 9, 10, 7, 5, 4],
    [9, 4, 8, 6, 7, 5, 10, 3, 9, 10],
    [4, 6, 8, 9, 5, 7, 10, 3, 9, 2]
])


# 1) Calculate and print the sum of all scores in the class
print('Tổng tất cả các điểm trong lớp 2A:', diem_2a.sum())
print('--------------------')

# 2) Calculate and print the total score for each student (sum of scores across all subjects)
print('#Tính tổng điểm của từng học sinh:')
for i in range(diem_2a.shape[1]):
    print('Tổng điểm các môn của học sinh', i, ':', diem_2a[:, i].sum())

#Vidu 43:
import numpy as np

# Assume diem_2a is a NumPy array containing student scores.
# For demonstration, let's create a sample array (you should replace this with your actual data)
diem_2a = np.array([
    [5, 7, 9],
    [3, 8, 7],
    [10, 9, 4],
    [7, 8, 6],
    [7, 5, 9],
    [6, 10, 9],
    [8, 4, 6],
    [3, 5, 6],
    [9, 4, 8],
    [4, 6, 8]
])

# 1) Calculate and print the mean score for the entire class
print('Điểm trung bình của cả lớp 2A:', diem_2a.mean())
print('--------------------')

# 2) Calculate and print the mean score for each student using Method 1
print('#Tính điểm trung bình của các học sinh trong lớp:')
print('#CÁCH 1:')
for i in range(diem_2a.shape[1]):
    print('Điểm trung bình của học sinh', i, ':', diem_2a[:, i].mean())

print('--------------------')

# 3) Calculate and print the mean score for each student using Method 2
print('#Tính điểm trung bình của các học sinh trong lớp:')
print('#CÁCH 2:')
mean_2a = diem_2a.mean(axis=0) # axis=0 means mean over each column
# axis = 0: theo hàng, axis = 1: theo cột
for i in range(mean_2a.size):
    print('Điểm trung bình của học sinh', i, ':', mean_2a[i])
    

#Vidu 44:
import numpy as np

# Sample data arrays (you can replace these with your actual data)
data_arrays = [
    np.array([3, 5, 3, 10, 9, 1, 9, 8, 3, 1, 6, 0, 7, 10, 8]),
    np.array([9, 1, 1, 8, 4, 7, 3, 7, 1, 10])
]

for a in data_arrays:
    print('Mảng a ban đầu:\n', a)
    print('Số phần tử trong mảng a:', a.size)

    a_sorted = np.sort(a)
    print('Mảng a đã sắp xếp:\n', a_sorted)
    print('Giá trị trung bình mean:', np.mean(a))
    print('Giá trị trung vị median:', np.median(a))
    print('--------------------') 

#Vidu 45:
import numpy as np
from scipy import stats as sp

# Assume diem_2a is a NumPy array containing student scores.
# For demonstration, let's create a sample array (you should replace this with your actual data)
diem_2a = np.array([
    [1, 1, 9, 6, 4, 5, 9, 8, 8, 8],
    [1, 1, 9, 6, 4, 5, 9, 8, 8, 8],
    [9, 9, 10, 9, 5, 6, 9, 9, 5, 9],
    [6, 6, 5, 6, 6, 5, 6, 6, 5, 6],
    [4, 4, 4, 4, 4, 4, 4, 4, 7, 4],
    [5, 5, 5, 5, 5, 5, 5, 5, 6, 5],
    [9, 9, 9, 9, 9, 9, 9, 9, 10, 9],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
])

# Calculate and print the mode for each subject (row)
for i in range(diem_2a.shape[0]):
    a = sp.mode(diem_2a[i, :])
    print('Môn', i, ': Điểm xuất hiện nhiều nhất:', a[0],' số lần:', a[1])
print(type(a))


#Vidu 46:
import numpy as np

# Assume diem_2a is a NumPy array containing student scores.
# For demonstration, let's create a sample array (you should replace this with your actual data)
diem_2a = np.array([
    [1, 9, 3, 6, 4, 7, 9, 1, 2, 7, 9],
    [2, 6, 4, 5, 8, 9, 7, 4, 8, 9, 1],
    [3, 5, 1, 8, 9, 2, 7, 8, 5, 9, 1],
    [4, 2, 1, 5, 9, 3, 4, 5, 3, 4, 2],
    [5, 7, 8, 4, 6, 1, 8, 9, 2, 3, 7],
    [9, 3, 2, 7, 8, 5, 6, 1, 4, 9, 8],
    [4, 8, 7, 6, 9, 2, 10, 1, 3, 5, 2],
    [7, 9, 1, 5, 3, 4, 7, 8, 6, 2, 1],
    [2, 6, 7, 8, 4, 9, 5, 1, 3, 2, 6],
    [9, 2, 5, 4, 1, 8, 6, 7, 9, 1, 8],
    [7, 8, 4, 5, 9, 2, 1, 6, 3, 7, 8],
])

# Calculate and print the range for each student (column)
for i in range(diem_2a.shape[1]):
    student_range = diem_2a[:, i].max() - diem_2a[:, i].min()
    print('Độ chênh điểm của học sinh', i, ':', student_range)


#Vidu 47:

import numpy as np

# Sample data arrays
a = np.array([10, 1, 1, 9, 12, 1, 9, 12, 10])
b = np.array([7, 7, 8, 7, 7, 7, 7])

# Calculate and print statistics for array 'a'
print('Phần tử của mảng a:', a)
print('Giá trị trung bình:', a.mean())
print('Độ lệch chuẩn:', a.std())

print('--------------------')

# Calculate and print statistics for array 'b'
print('Phần tử của mảng b:', b)
print('Giá trị trung bình:', b.mean())
print('Độ lệch chuẩn:', b.std())

#Vidu 53:
import numpy as np

# Sample data arrays
a = np.array([10, 1, 1, 9, 12, 1, 9, 12, 10])
b = np.array([7, 7, 8, 7, 7, 7, 7])

# Calculate and print statistics for array 'a'
print('Phần tử của mảng a:', a)
print('Giá trị trung bình:', a.mean())
print('Độ lệch chuẩn:', a.std())

print('--------------------')

# Calculate and print statistics for array 'b'
print('Phần tử của mảng b:', b)
print('Giá trị trung bình:', b.mean())
print('Độ lệch chuẩn:', b.std())