#13
import numpy as np

a = np.array([1, 2, 5, 7, 0, 8])

print(a)
print("Data type of variable a:", type(a))
print("Data type of elements in array a:", a.dtype)
print("Size of array a:", a.shape)
print("Number of elements in array a:", a.size)
print("Number of dimensions of array a:", a.ndim)

#14
import numpy as np

b = np.array([(4, 5, 6.0), (1, 2, 3.5)])

print(b)
print("Data type of variable b:", type(b))
print("Data type of elements in array b:", b.dtype)
print("Size of array b:", b.shape)
print("Number of elements in array b:", b.size)
print("Number of dimensions of array b:", b.ndim)

#15
import numpy as np

c = np.array([[[2, 4, 0, 6], [4, 7, 5, 6]],
              [[0, 3, 2, 1], [9, 4, 5, 6]],
              [[5, 8, 6, 4], [1, 4, 6, 8]]])  # 3D array (3D)

print(c)
print("First element of array c:", c[0, 0, 0])
print("Data type of elements in array c:", c.dtype)
print("Size of array c:", c.shape)
print("Number of elements in array c:", c.size)
print("Number of dimensions of array c:", c.ndim)

#18
# Phương thức zeros: Tạo ma trận 0 kích thước 5 hàng x 3 cột
import numpy as np

array_zeros = np.zeros((5, 3))

print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:", array_zeros.dtype)
print("Kích thước của mảng array_zeros:", array_zeros.shape)
print("Số phần tử của mảng array_zeros:", array_zeros.size)
print("Số chiều của mảng array_zeros:", array_zeros.ndim)

#15
import numpy as np

c = np.array([[[2, 4, 0, 6], [4, 7, 5, 6]],
              [[0, 3, 2, 1], [9, 4, 5, 6]],
              [[5, 8, 6, 4], [1, 4, 6, 8]]])  # 3D array (3D)

print(c)
print("First element of array c:", c[0, 0, 0])
print("Data type of elements in array c:", c.dtype)
print("Size of array c:", c.shape)
print("Number of elements in array c:", c.size)
print("Number of dimensions of array c:", c.ndim)

#18
# Phương thức zeros: Tạo ma trận 0 kích thước 5 hàng x 3 cột
import numpy as np

array_zeros = np.zeros((5, 3))

print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:", array_zeros.dtype)
print("Kích thước của mảng array_zeros:", array_zeros.shape)
print("Số phần tử của mảng array_zeros:", array_zeros.size)
print("Số chiều của mảng array_zeros:", array_zeros.ndim)

# Phương thức Ones: Tạo ma trận 1 kích thước 3 hàng x 5 cột
import numpy as np

array_one = np.ones((3, 5), dtype=np.int)

print(array_one)
print("Kiểu dữ liệu trong mảng array_one:", array_one.dtype)
print("Kích thước của mảng array_one:", array_one.shape)
print("Số phần tử của mảng array_one:", array_one.size)
print("Số chiều của mảng array_one:", array_one.ndim)

#19
#Phương thức eye: Tạo ma trận đơn vị cấp 5
import numpy as np

array_eye = np.eye(5)

print(array_eye)
print("Kiểu dữ liệu của phần tử trong mảng array_eye:", array_eye.dtype)
print("Kích thước của mảng array_eye:", array_eye.shape)
print("Số phần tử của mảng array_eye:", array_eye.size)
print("Số chiều của mảng array_eye:", array_eye.ndim)

#20
#Phương thức random: Tạo một ma trận (7x5) các phần tử ngẫu nhiên [0, 1)
import numpy as np

array_random = np.random.random((7, 5))

print(array_random)
print("Kiểu dữ liệu của phần tử trong mảng array_random:", array_random.dtype)
print("Kích thước của mảng array_random:", array_random.shape)
print("Số phần tử của mảng array_random:", array_random.size)
print("Số chiều của mảng array_random:", array_random.ndim)

#21
import numpy as np

# Tạo vector 6 số nguyên ngẫu nhiên từ 10 đến 29
vector_ngau_nhien = np.random.randint(low=10, high=30, size=6)
print("Vector ngẫu nhiên:", vector_ngau_nhien)


# Tạo ma trận 2x3 số nguyên ngẫu nhiên từ 1 đến 10
ma_tran_ngau_nhien = np.random.randint(low=1, high=11, size=(2, 3)) # Lưu ý high=11 vì 11 không được bao gồm
print("\nMa trận ngẫu nhiên:")
print(ma_tran_ngau_nhien)


# Một ví dụ khác: tạo một số nguyên ngẫu nhiên từ 0 đến 99 (high mặc định là None)
so_ngau_nhien = np.random.randint(100)
print("\nSố ngẫu nhiên (0-99):", so_ngau_nhien)


# Tạo ma trận 3x4 với kiểu dữ liệu uint8
ma_tran_uint8 = np.random.randint(0, 256, size=(3, 4), dtype=np.uint8)  # 0-255 vì uint8
print("\nMa trận uint8:")
print(ma_tran_uint8)

#21
#Phương thức arange(a, b, steps):
#Tạo vector:
# Phần tử đầu tiên = a,
# kết thúc <b,
# mỗi phần tử cách nhau một khoảng = steps
d = np.arange(1, 15, 2)
print("Vector d:", d)
print("Số phần tử của vector d:", d.size)

print('---------------------')

#Phương thức linspace(a, b, num)
#Tạo vector:
# Phần tử đầu tiên = a,
# Phần tử kết thúc = b,
#Số phần tử của ma trận = num
f = np.linspace(1, 15, 11)
print("Vector f:", f)
print("Số phần tử của vector f:", f.size)

#25
import numpy as np

#Đọc dữ liệu từ file Diem_2A.txt
path = 'Data_Excercise/Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
print("Kích thước của mảng diem_2a:", diem_2a.shape)
print("Số phần tử của mảng diem_2a:", diem_2a.size)
print("Số chiều của mảng diem_2a:", diem_2a.ndim)

#28
import numpy as np

# a.astype(kiểu mới) : Chuyển đổi kiểu dữ liệu của các phần tử
a_float = np.linspace(0, 15, 11)
print(a_float)
print('Kiểu Dữ liệu: ', a_float.dtype)
print('----------------------------------')


#Chuyển từ kiểu float --> int
a_int = a_float.astype(np.int16)
print(a_int)
print('Dữ liệu sau khi chuyển: ', a_int.dtype)

#Chuyển từ kiểu float --> int
a_str = a_int.astype(np.str_)
print(a_str)
print('Dữ liệu sau khi chuyển: ', a_str.dtype)

#Chuyển từ kiểu float --> boolean
a_bol = a_int.astype(np.bool_)
print(a_bol)
print('Dữ liệu sau khi chuyển: ', a_bol.dtype)

#31
import numpy as np

# Truy cập tới một phần tử của Vector: a[index]
# Note: index phần tử đầu tiên 0
#       index phần tử cuối cùng -1
a = np.array([3, 5, 3, 10, 9, 1, 9, 8, 3, 1])

print('các phần tử của Vector a:\n', a)
print('------------------------')
print('phần tử đầu tiên:', a[0])
print('phần tử thứ 3:', a[3])
print('phần tử cuối cùng:', a[-1])



# Truy cập tới nhiều phần tử của Vector: a[index1:index2]
print('các phần tử của Vector a:\n', a)
print('----------------------------')
print('3 Phần tử đầu tiên:', a[:3])
print('Từ phần tử thứ 5 tới hết:', a[5:])
print('Từ phần tử 2 đến phần tử <6 của vector:', a[2:6])

#32
#Truy cập tới 1 phần tử của ma trận (2D): a[index_row, index_col]
print('Điểm môn học đầu tiên, của học sinh đầu tiên:', diem_2a[0, 0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[1, 3])
print('Điểm môn cuối cùng, của học sinh cuối cùng:', diem_2a[-1, -1])
print('---------------------------------------------')
print('Bảng điểm lớp 2A:\n', diem_2a)

#33
#Truy cập tới nhiều phần tử trong ma trận: a[index_row1:index_row2, index_col1:index_col2]
#Lấy điểm tất cả các môn (tất cả các hàng) của học sinh 5:
diem_hs5 = diem_2a[: , 5]
print("Điểm các môn của học sinh 5:", diem_hs5)

#Lấy điểm môn học cuối cùng của tất cả học sinh (tất cả các cột)
diem_mon = diem_2a[-1 , :]
print("Điểm môn học cuối cùng của tất cả học sinh: \n", diem_mon)

#Lấy điểm 5 môn học đầu tiên của 10 học sinh đầu tiên
diem5_hs10 = diem_2a[:5 , :10]
print("Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp:\n", diem5_hs10)