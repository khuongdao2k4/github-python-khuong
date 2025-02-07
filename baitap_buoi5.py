#35
import numpy as np

# Định nghĩa cấp ma trận (n x n)
n = 12

# Tạo ma trận vuông cấp n với các phần tử ngẫu nhiên từ 0 đến 100
ma_tran = np.random.randint(0, 101, size=(n, n))

# In ma trận
print(ma_tran)

# In thông tin về ma trận
print("Kiểu dữ liệu của phần tử trong ma trận:", ma_tran.dtype)
print("Kích thước của mảng ma trận:", ma_tran.shape)
print("Số phần tử của mảng ma trận:", ma_tran.size)
print("Số chiều của mảng ma trận:", ma_tran.ndim)

#36
import numpy as np

n = 12  # Cấp của ma trận (n x n)
ma_tran = np.random.randint(0, 101, size=(n, n)) # Tạo lại ma trận nếu cần

# v_chinh: bao gồm các phần tử nằm trên đường chéo chính của ma trận.
v_chinh = np.diag(ma_tran)
print("Vector các phần tử nằm trên đường chéo chính:")
print(v_chinh)

# V_phu: bao gồm các phần tử nằm trên đường chéo phụ của ma trận
V_phu = np.diag(np.fliplr(ma_tran)) # Đảo ngược ma trận theo chiều ngang trước khi lấy đường chéo
print("\nVector các phần tử nằm trên đường chéo phụ:")
print(V_phu) 

#37
import numpy as np

# Giả sử ma trận từ Yêu cầu 1 đã được tạo và lưu trong biến 'ma_tran'
n = 12
ma_tran = np.random.randint(0, 101, size=(n, n)) # Tạo ma trận nếu cần

# Nhập giá trị x từ người dùng
x = int(input("Nhập vào giá trị x (0-100): "))

# Đếm số phần tử bằng x
so_phan_tu_bang_x = np.count_nonzero(ma_tran == x)

# Đếm số phần tử nhỏ hơn x
so_phan_tu_nho_hon_x = np.count_nonzero(ma_tran < x)

# Đếm số phần tử lớn hơn x
so_phan_tu_lon_hon_x = np.count_nonzero(ma_tran > x)

# In kết quả
print("1. Số phần tử có giá trị bằng x trong ma trận:", so_phan_tu_bang_x)
print("2. Số phần tử nhỏ hơn giá trị x trong ma trận:", so_phan_tu_nho_hon_x)
print("3. Số phần tử lớn hơn giá trị x trong ma trận:", so_phan_tu_lon_hon_x)