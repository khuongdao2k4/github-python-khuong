#5
import numpy as np

# Phương thức a.reshape(m,n)
vector_a = np.array([5, 7, 2, 9, 10, 15, 2, 9, 2, 17, 28, 16], dtype=np.int16)
print(vector_a)
print('Số phần tử của vector:', vector_a.size)
print('--------------------')

# Chuyển đổi vector về matrix (n x m)
# Lưu ý: matrix.size = vector.size
matrix_a = vector_a.reshape((3, 4))
print('Reshape về matrix: 3 x 4')
print(matrix_a)
print('Số phần tử của matrix_a:', matrix_a.size)
print('--------------------')

print('Reshape về matrix: 2 x 6')
matrix_b = vector_a.reshape((2, 6))
print(matrix_b)
print('Số phần tử của matrix_b:', matrix_b.size)

#7
import numpy as np

# Chuyển đổi từ Matrix --> Vector
a1_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Matrix: \n', a1_2d)

print('--------------------')
print('a) ravel by row (default order=\'C\')')
print(a1_2d.ravel())

print('\nb) ravel by column (order=\'F\')')
print(a1_2d.ravel(order='F'))

#9
import numpy as np

# Example 1
x = np.arange(0, 6)
print(x)

# Tách vector x thành 2 vector
# có số phần tử bằng nhau
x1, x2 = np.split(x, 2)
print(x1, x2)

# Example 2
x = np.arange(1, 10)
print(x)

# Tách vector x thành 3 vector
# tại các vị trí 2 và 6
x1, x2, x3 = np.split(x, [2, 6])
print(x1, x2, x3)

#11
import numpy as np

# Example 1
x = np.arange(0, 6)
print(x)

# Tách vector x thành 2 vector
# có số phần tử bằng nhau
x1, x2 = np.split(x, 2)
print(x1, x2)

# Example 2
x = np.arange(1, 10)
print(x)

# Tách vector x thành 3 vector
# tại các vị trí 2 và 6
x1, x2, x3 = np.split(x, [2, 6])
print(x1, x2, x3)


#16
import numpy as np

x = np.arange(8)
print("x =", x)
print('---')

# Các phép toán đã giới thiệu trong buổi 01
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print(" -x =", -x)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)
print("x % 2 =", x % 2)
print("x ^ 3 =", x**3)


print('---')
# Sử dụng các phương thức của NumPy
print("x + 5 =", np.add(x, 5))
print("x - 5 =", np.subtract(x, 5))
print("-x =", np.negative(x))
print("x * 2 =", np.multiply(x, 2))
print("x / 2 =", np.divide(x, 2))
print("x // 2 =", np.floor_divide(x, 2))
print("x % 2 =", np.mod(x, 2))
print("x ^ 3 =", np.power(x, 3))

#17
import numpy as np

# --- Example 1: Absolute values ---
x = np.array([-2, -1, 0, 1, 2])
print(x)
print('---')
print(np.abs(x))
print(np.absolute(x))


# --- Example 2: Trigonometric functions ---
theta = np.linspace(0, np.pi, 3)
print("theta =", theta)
print('---')
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))

#19
import numpy as np

# --- Example 1: Absolute values ---
x = np.array([-2, -1, 0, 1, 2])
print(x)
print('---')
print(np.abs(x))
print(np.absolute(x))


# --- Example 2: Trigonometric functions ---
theta = np.linspace(0, np.pi, 3)
print("theta =", theta)
print('---')
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))

#20
import numpy as np

arr = np.array([20.89999, 67.89899, 54.43409])
print(arr)
print('---')

#1) Làm tròn tới 1 số sau dấu ,
print(np.around(arr, 1))

#2) Làm tròn tới 2 số sau dấu ,
print(np.around(arr, 2))

#3) Làm tròn xuống số nguyên gần nhất
print(np.floor(arr))

#4) Làm tròn lên số nguyên gần nhất
print(np.ceil(arr))

#23
import numpy as np

#Sắp xếp các phần tử trong một vector
a = np.random.randint(1, 33, 15)

print('Vector ban đầu:\n', a)
print('---')

#Sắp xếp vector a tăng dần
a_sort = np.sort(a)


#Sắp xếp vector a giảm dần:
#1) Lật vector a_sort để sắp xếp giảm dần
b_sort = np.flip(a_sort)

#2) sử dụng -np.sort(-x)
b_sort = -np.sort(-a)


print('Vector sắp xếp tăng dần: \n', a_sort)
print('Vector sắp xếp giảm dần: \n', b_sort)

#25
import numpy as np

A = np.array([
    [8, 27, 2, 8, 3, 26],
    [7, 16, 19, 23, 29, 21],
    [14, 10, 1, 3, 20, 5],
    [29, 11, 19, 12, 17, 29],
    [4, 14, 10, 4, 23, 4]
])

print("Ma trận A:")
print(A)


# a) Sắp xếp theo hàng axis=0
a_sort1 = np.sort(A, axis=0)
print('Ma trận 1:\n', a_sort1)


# b) Sắp xếp theo cột axis=1 | Default
a_sort2 = np.sort(A, axis=1)
print('Ma trận 2:\n', a_sort2)


# c) Chuyển thành vector và sắp xếp các phần tử tăng dần theo hàng
v_sort = np.sort(A, axis=None)
print('Vector: \n', v_sort)


#Sắp xếp tất cả các phần tử theo thứ tự tăng dần theo hàng
a_sort3 = np.sort(A, axis=None).reshape(A.shape[0], A.shape[1])
print('Ma trận 3:\n', a_sort3)

#28
import numpy as np

x = np.array([17, 2, 11, 1, 9, 15, 1, 3, 8, 1, 12, 13, 5])

#1) Tìm kiếm các phần tử có giá trị ==1
t1 = np.where(x==1)
print(t1)
print('1. Số phần tử thỏa mãn điều kiện = 1: ', t1[0].size)
print('---')


#2) Tìm kiếm các phần tử có giá trị >10
t2 = np.where(x>10)
print(t2)
print('2. Số phần tử thỏa mãn điều kiện>10: ', t2[0].size)
print('---')


#Tìm kiếm các phần tử có giá trị [5,12)
t3 = np.where((x>=5) & (x<12))
print(t3)
print('3.Số phần tử thỏa mãn điều kiện [5,10): ', t3[0].size)

#29
import numpy as np

#Tìm kiếm trên ma trận
arr = np.array([(1, 2, 3, 4, 5, 4, 4),
               (7, 3, 4, 8, 9, 6, 7)])

#Tìm kiếm phần tử > 4
x = np.where(arr > 4)

print('Ma trận A: \n',arr)
print('---')
print(x)
print('Số phần tử thỏa mãn điều kiện > 4:', x[0].size)