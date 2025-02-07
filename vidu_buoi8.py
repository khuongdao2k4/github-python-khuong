#39
import numpy as np

a = np.array([(1, 3, 1, 4),
              (3, 9, 5, 15),
              (0, 2, 1, 1),
              (0, 4, 2, 3)])

print('Ma trận a: \n', a)
det_a = np.linalg.det(a)
print('det(a) = ', det_a)

b = np.array([(1, 2, 3, 4),
              (-2, -1, 4, 1),
              (3, -4, -5, 6),
              (1, 2, 3, 4)])
print('Ma trận b:\n', b)
det_b = np.linalg.det(b)
print('det(b) = ', det_b)

#42
import numpy as np

A = np.array([
    [60, 84, 47, 28, 10, 48, 83, 43],
    [59, 82, 30, 52, 70, 56, 77, 91],
    [6, 15, 21, 64, 89, 31, 69, 1],
    [20, 50, 6, 10, 96, 54, 51, 89],
    [16, 56, 62, 23, 3, 77, 4],
    [73, 71, 70, 80, 70, 90, 58],
    [7, 48, 78, 26, 99, 91, 21],
    [4, 35, 57, 31, 3, 73, 14],
    [89, 73, 27, 32, 83, 71, 55],
    [95, 15, 67, 75, 86, 36, 96, 72]
])


# Lấy các phần tử nằm trên đường chéo chính 
# của ma trận a 1 phần tử
d_A1 = A.diagonal(1)
print(d_A1)

# Lấy các phần tử trên đường chéo chính của
# ma trận vuông A
d_A = A.diagonal()
print(d_A)


# Lấy các phần tử nằm dưới đường chéo chính
# của ma trận a 4 phần tử
d_A1 = A.diagonal(-4)
print(d_A1)

#44
import numpy as np

A = np.array([
    [60, 84, 47, 28, 10, 48, 83, 43],
    [59, 82, 30, 52, 70, 56, 77, 91],
    [6, 15, 21, 64, 89, 31, 69, 1],
    [20, 50, 6, 10, 96, 54, 51, 89],
    [16, 56, 62, 23, 3, 77, 4],
    [73, 71, 70, 80, 70, 90, 58],
    [7, 48, 78, 26, 99, 91, 21],
    [4, 35, 57, 31, 3, 73, 14],
    [89, 73, 27, 32, 83, 71, 55],
    [95, 15, 67, 75, 86, 36, 96, 72]
])


# Tạo ma trận là các phần tử trên đường chéo chính
# của ma trận vuông A cách đường chéo chính
# về phía trên 2 đường
d_A1 = np.triu(A, 2)
print(d_A1)



#Tạo ma trận là các phần tử trên đường chéo chính
# của ma trận vuông A cách đường chéo chính
# về phía dưới 3 đường
d_A1 = np.triu(A, -3)
print(d_A1)

#45
import numpy as np

# Example matrix (you can change this)
A = np.array([
    [3, -1, -2],
    [3, 2, -3],
    [1, 2, 0]
])


# Method 1: Using the trace() method
trace_A = A.trace()
print('Trace of Matrix A:', trace_A)



# Method 2: Summing diagonal elements
trace_A = A.diagonal().sum()
print('Trace of Matrix A:', trace_A)

#53
import numpy as np

a = np.array([
    [9, 4, 19, 1, 18],
    [15, 11, 1, 9, 14],
    [17, 8, 4, 10, 13]
])

b = np.array([
    [6, 4, 9, 12, 4],
    [3, 6, 11, 14, 10],
    [1, 6, 5, 12, 2]
])


# Method 1: Using np.equal()
equal_ab = np.equal(a, b)
print(equal_ab)



# Method 2: Using the == operator (equivalent to np.equal)
equal_ab = a == b
print(equal_ab)

#54
import numpy as np

a = np.array([
    [9, 4, 19, 1, 18],
    [15, 11, 1, 9, 14],
    [17, 8, 4, 10, 13]
])

b = np.array([
    [6, 4, 9, 12, 4],
    [3, 6, 11, 14, 10],
    [1, 6, 5, 12, 2]
])


# Addition of two matrices

# Method 1: Using np.add()
sum_ab = np.add(a, b)
print(sum_ab)

# Method 2: Using the + operator (equivalent to np.add)
sum_ab = a + b
print(sum_ab)


# Subtraction of two matrices

# Method 1: Using np.subtract()
sub_ab = np.subtract(a, b)
print(sub_ab)


# Method 2: Using the - operator (equivalent to np.subtract)
sub_ab = a - b
print(sub_ab)

#55
import numpy as np

# Example matrices (ensure dimensions are compatible for multiplication)
a = np.array([
    [9, 4, 19, 1, 18],
    [15, 11, 1, 9, 14],
    [17, 8, 4, 10, 13]
])

c = np.array([
    [13, 8, 9, 13],
    [17, 11, 4, 3],
    [13, 7, 2, 18],
    [12, 1, 7, 2],
    [1, 13, 6, 4]
])


# Matrix multiplication

# Method 1: Using np.dot() or @ operator
multi_ac = np.dot(a, c)  # or multi_ac = a @ c
print(multi_ac)

# Example with vectors (1D arrays):
vector_a = np.random.randint(1, 20, 10)
vector_b = np.random.randint(1, 20, 10)

# Vector multiplication (dot product)
vector_ab = vector_a @ vector_b # or vector_ab = np.dot(vector_a, vector_b)

print("Vector a:\n", vector_a)
print("Vector b:\n", vector_b)
print("Tích của hai vector:\n", vector_ab)

#61
import numpy as np

vector_height = [174, 189, 185, 195, 149, 189, 147, 154, 174, 169,
                 195, 159, 192, 155, 191, 153, 157, 140, 144, 172,
                 157, 153, 169, 185, 172, 151, 190, 187, 163, 179,
                 153, 178, 195, 160, 157, 189, 197, 144, 171, 185,
                 175, 149, 157, 161, 182, 185, 188, 181, 161, 140,
                 168, 176, 163, 172, 196, 187, 172, 178, 164, 143,
                 191, 141, 193, 190, 175, 179, 172, 168, 164, 194,
                 153, 178, 141, 180, 185, 197, 165, 168, 176, 181,
                 164, 166, 190, 186, 168, 198, 175, 145, 159, 185,
                 178, 183, 194, 177, 197, 170, 142, 160, 195, 190]

vector_weigth = [96, 87, 110, 104, 61, 104, 92, 111, 90, 103,
                 81, 80, 101, 51, 79, 107, 110, 129, 145, 139,
                 110, 149, 97, 139, 67, 64, 95, 62, 159, 152,
                 121, 52, 65, 131, 153, 132, 114, 80, 152, 81,
                 120, 108, 56, 118, 126, 76, 122, 111, 72, 152,
                 135, 54, 110, 105, 116, 89, 92, 127, 70, 88,
                 54, 143, 54, 83, 135, 158, 96, 59, 82, 136,
                 51, 117, 80, 75, 100, 154, 104, 90, 122, 51,
                 75, 140, 105, 118, 123, 50, 141, 117, 104, 140,
                 154, 96, 111, 61, 119, 156, 69, 139, 69, 50]


height = np.array(vector_height).reshape(10, 10)
weight = np.array(vector_weigth).reshape(10, 10)


# So sánh hai ma trận
comparison = height == weight
print("So sánh:\n", comparison)

# Cộng hai ma trận
addition = height + weight
print("\nCộng:\n", addition)

# Trừ hai ma trận
subtraction = height - weight
print("\nTrừ:\n", subtraction)

# Nhân hai ma trận
multiplication = height * weight  # Element-wise multiplication
# Or for dot product: multiplication = np.dot(height, weight) 
print("\nNhân:\n", multiplication)