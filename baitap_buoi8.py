#48
import numpy as np

vector_weight = [96, 87, 110, 104, 61, 104, 92, 111, 90, 103, 81, 80, 101, 51,
                79, 107, 110, 129, 145, 139, 110, 149, 97, 139, 67, 64, 95, 62,
                159, 152, 121, 52, 65, 131, 153, 132, 114, 80, 152, 81, 120, 108,
                56, 118, 126, 76, 122, 111, 72, 152, 135, 54, 110, 105, 116, 89,
                92, 127, 70, 88, 54, 143, 54, 83, 135, 158, 96, 59, 82, 136, 51,
                117, 80, 75, 100, 154, 104, 90, 122, 51, 75, 140, 105, 118, 123,
                50, 141, 117, 104, 140, 154, 96, 111, 61, 119, 156, 69, 139, 69, 50]

weight_matrix = np.array(vector_weight).reshape(10, 10)

print(weight_matrix)

#49
import numpy as np

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
weight = np.array(vector_weigth).reshape(10, 10)


# Yêu cầu 3.2: Check if inverse exists and calculate if it does
try:
    inverse_weight = np.linalg.inv(weight)
    print("Ma trận nghịch đảo của weight:\n", inverse_weight)
except np.linalg.LinAlgError:
    print("Ma trận weight không khả nghịch (không có ma trận nghịch đảo).")

# Yêu cầu 3.3: Get diagonal, calculate trace

# a) Đường chéo chính
vector_diagonal = np.diag(weight)
print("\nĐường chéo chính của ma trận weight:\n", vector_diagonal)

# b) Trace
trace_weight = np.trace(weight)
print("\nTrace của ma trận weight:", trace_weight)

#50
import numpy as np

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
weight = np.array(vector_weigth).reshape(10, 10)

# Ma trận đường chéo trên (không bao gồm đường chéo chính)
upper_triangular = np.triu(weight, k=1)  # k=1 to exclude the main diagonal
print("Ma trận đường chéo trên:\n", upper_triangular)
print("Phần tử max:", upper_triangular.max())


# Ma trận đường chéo dưới (không bao gồm đường chéo chính)
lower_triangular = np.tril(weight, k=-1)  # k=-1 to exclude the main diagonal
print("\nMa trận đường chéo dưới:\n", lower_triangular)
print("Phần tử max:", lower_triangular.max())

#57
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

# So sánh
comparison = height == weight
print("So sánh:\n", comparison)

# Cộng
addition = height + weight
print("\nCộng:\n", addition)

# Trừ
subtraction = height - weight
print("\nTrừ:\n", subtraction)

# Nhân (element-wise)
multiplication = height * weight
print("\nNhân:\n", multiplication)

#63
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


# Calculate inverse and rank of Height
try:
    height_inv = np.linalg.inv(height).T  # .T transposes for display as shown
    height_rank = np.linalg.matrix_rank(height)
    print("Ma trận nghịch đảo height.T:\n", height_inv)
    print("Hạng của ma trận height:", height_rank)
except np.linalg.LinAlgError:
    print("Ma trận height không khả nghịch.")



# Calculate inverse and rank of Weight
try:
    weight_inv = np.linalg.inv(weight).T  # .T transposes for display as shown
    weight_rank = np.linalg.matrix_rank(weight)
    print("\nMa trận nghịch đảo weight.T:\n", weight_inv)
    print("Hạng của ma trận weight:", weight_rank)
except np.linalg.LinAlgError:
    print("\nMa trận weight không khả nghịch.")

#64
import numpy as np

# Question 1
matrix1 = np.array([[1, 2, 3],
                   [2, 2, 2],
                   [3, 3, 3]])
rank1 = np.linalg.matrix_rank(matrix1)
print(f"Rank of matrix 1: {rank1}")  # Answer: 2 (C)


# Question 2:
matrix2 = np.array([[1, 2, 3],
                   [3, 4, 5],
                   [4, 5, 6]])
det2 = np.linalg.det(matrix2)
rank2 = np.linalg.matrix_rank(matrix2)
print(f"Determinant of matrix 2: {det2}")
print(f"Rank of matrix 2: {rank2}")  # Answer: Less than or equal to 3 because det()=0 (C)


# Question 3
matrix3 = np.array([[10, 10, 10, 10, 10],
                   [10, 10, 10, 10, 10],
                   [10, 10, 10, 10, 10],
                   [10, 10, 10, 10, 10]])

rank3 = np.linalg.matrix_rank(matrix3)
print(f"Rank of matrix 3: {rank3}")  # Answer: 1 (D)