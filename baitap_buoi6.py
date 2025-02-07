#49 
diem_tb = [4.8, 6.0, 4.7, 8.6, 6.2, 6.8, 5.6, 5.4, 5.9, 5.1, 7.2, 5.4, 5.9, 5.9, 6.0, 7.9, 4.2, 6.1, 6.3, 4.4, 4.7, 5.9, 5.6, 4.7, 6.4, 6.2, 6.5, 4.6, 5.8, 4.3]
bang_diem = [[7, 10, 9, 8, 7, 10, 10, 8, 9, 8],
               [3, 2, 2, 1, 2, 6, 2, 7, 9, 8]
               ]


# 1. ĐTB của từng học sinh trong lớp:
print("Điểm TB của từng học sinh trong lớp:")
print(diem_tb)


# 2. Học sinh có điểm TB cao nhất.
diem_cao_nhat = max(diem_tb)
vi_tri_cao_nhat = diem_tb.index(diem_cao_nhat) +1

print("\nĐiểm TB cao nhất:", diem_cao_nhat)
print("Của học sinh thứ:", vi_tri_cao_nhat)




if vi_tri_cao_nhat <=10:
    print("Bảng điểm đầy đủ của học sinh:", bang_diem[0])
else:

    print("Bảng điểm đầy đủ của học sinh:", bang_diem[1])
    


# 3. Học sinh có điểm trung bình thấp nhất
diem_thap_nhat = min(diem_tb)
vi_tri_thap_nhat = diem_tb.index(diem_thap_nhat) +1

print("\nĐiểm TB thấp nhất:", diem_thap_nhat)
print("Của học sinh thứ:", vi_tri_thap_nhat)

if vi_tri_thap_nhat<= 10:
     print("Bảng điểm đầy đủ của học sinh:",bang_diem[0])

elif vi_tri_thap_nhat >= 11 and vi_tri_thap_nhat <=20:
    print("Bảng điểm đầy đủ của học sinh:",bang_diem[1])

#50
diem_tb_mon_hoc = [4.73, 4.43, 5.5, 4.83, 4.97, 5.6, 6.23, 7.3, 6.13, 7.97]
bang_diem_day_du = [[7, 7, 8, 7, 8, 6, 10, 10, 6, 8, 10, 8, 9, 8, 8, 5, 10, 8, 7, 8, 7, 9, 9, 8, 7, 7, 10, 8, 9, 7],
                   [3, 3, 5, 3, 10, 9, 1, 9, 8, 3, 1, 6, 0, 7, 10, 8, 5, 2, 7, 7, 1, 1, 6, 1, 6, 3, 0, 2, 2, 1]]


# 1. ĐTB của từng môn học:
print("Điểm TB của từng môn học:")
print(diem_tb_mon_hoc)


# 2. Môn học có điểm TB cao nhất.
diem_cao_nhat = max(diem_tb_mon_hoc)
mon_hoc_cao_nhat = diem_tb_mon_hoc.index(diem_cao_nhat)

print("\nĐiểm TB cao nhất của môn học:", diem_cao_nhat)
print("Môn học thứ", mon_hoc_cao_nhat + 1) # index bắt đầu từ 0 nên cộng thêm 1
print("Bảng điểm đầy đủ của môn học:", bang_diem_day_du[0])  # Giả sử môn học cao nhất luôn là môn đầu


# 3. Môn học có điểm trung bình thấp nhất
diem_thap_nhat = min(diem_tb_mon_hoc)
mon_hoc_thap_nhat = diem_tb_mon_hoc.index(diem_thap_nhat)

print("\nĐiểm TB thấp nhất của môn học:", diem_thap_nhat)
print("Môn học thứ", mon_hoc_thap_nhat + 1)  # index bắt đầu từ 0 nên cộng thêm 1
print("Bảng điểm đầy đủ của môn học:", bang_diem_day_du[1]) # Giả sử môn học thấp nhất luôn là môn thứ hai

#51
import numpy as np

bang_diem_hoc_sinh = [
    [7, 10, 9, 8, 7, 10, 10, 8, 9, 8],
    [5, 1, 0, 10, 4, 7, 1, 8, 1, 7]
    # ... thêm các học sinh khác nếu có
]

bang_diem_mon_hoc = [
    [8, 8, 7, 8, 6, 7, 7, 8, 6, 7, 6, 8, 8, 7, 6, 8, 8, 8, 7, 8, 8, 8, 6, 8, 7, 7, 8],
    [1, 10, 4, 9, 6, 9, 0, 2, 3, 1, 8, 6, 8, 4, 2, 9, 2, 9, 5, 0, 4, 1, 7, 3, 8, 9, 8, 9, 9]
    # ... thêm các môn học khác nếu có
]


def tinh_do_lech(diem):
    return np.std(diem)


# 1. Sinh viên có điểm đồng đều nhất và sinh viên có điểm chênh lệch nhất
do_lech_hoc_sinh = []
for diem in bang_diem_hoc_sinh:
    do_lech_hoc_sinh.append(tinh_do_lech(diem))

hs_dong_deu_nhat = do_lech_hoc_sinh.index(min(do_lech_hoc_sinh))
hs_lech_nhat = do_lech_hoc_sinh.index(max(do_lech_hoc_sinh))


print("Học sinh học đồng đều nhất:", [hs_dong_deu_nhat])
print("Bảng điểm của học sinh học đồng đều:", bang_diem_hoc_sinh[hs_dong_deu_nhat])

print("\nHọc sinh học lệch nhất:", [hs_lech_nhat])
print("Bảng điểm của học sinh học lệch:", bang_diem_hoc_sinh[hs_lech_nhat])



# 2. Môn học có điểm đồng đều nhất và môn học có điểm chênh lệch nhất
do_lech_mon_hoc = []
for diem in bang_diem_mon_hoc:
    do_lech_mon_hoc.append(tinh_do_lech(diem))

mon_dong_deu_nhat = do_lech_mon_hoc.index(min(do_lech_mon_hoc))
mon_lech_nhat = do_lech_mon_hoc.index(max(do_lech_mon_hoc))


print("\nMôn học có điểm đồng đều nhất:", [mon_dong_deu_nhat])
print("Bảng điểm của môn học đồng đều:", bang_diem_mon_hoc[mon_dong_deu_nhat])

print("\nMôn học có điểm lệch nhất:", [mon_lech_nhat])
print("Bảng điểm của môn học lệch:", bang_diem_mon_hoc[mon_lech_nhat])

#56
import numpy as np

# Dữ liệu diện tích (Square Feet) và giá nhà (Price)
dien_tich = [1460, 2108, 1743, 1499, 1864, 2391, 1977, 1610, 1530, 1759, 1821, 2216]
gia_nha = [288700, 309300, 301400, 291100, 302400, 314900, 305400, 297000, 292400, 298200, 304300, 311700]


# Dữ liệu khoảng cách (Distance) và giá nhà (Prices)
khoang_cach = [2.6, 0.8, 1.0, 0.6, 1.5, 2.0, 3.4, 1.2, 3.6, 1.7]
gia_nha_2 = [214, 376, 280, 362, 200, 190, 236, 244, 128, 165]


# 1. Hệ số tương quan giữa diện tích và giá nhà
he_so_tuong_quan_1 = np.corrcoef(dien_tich, gia_nha)[0, 1]
print(f"Hệ số tương quan giữa diện tích và giá nhà: {he_so_tuong_quan_1}")


# 2. Hệ số tương quan giữa khoảng cách và giá nhà
he_so_tuong_quan_2 = np.corrcoef(khoang_cach, gia_nha_2)[0, 1]
print(f"Hệ số tương quan giữa khoảng cách từ trung tâm thành phố và giá nhà: {he_so_tuong_quan_2}")

#61
import numpy as np

# Tạo file Temp.txt (chỉ để demo, bạn có thể thay bằng file của bạn)
with open("Temp.txt", "w") as f:
    f.write("25.65 24.79 24.01 25.06 25.48 24.97\n")
    f.write("25.31 24.21 24.02 24.93 25.16 24.83\n")
    f.write("25.05 23.73 23.89 24.79 24.8 24.55\n")
    # ... thêm dữ liệu khác nếu cần


# Đọc dữ liệu từ file Temp.txt vào biến data_numpy
try:
    data_numpy = np.loadtxt("Temp.txt")
except FileNotFoundError:
    print("File Temp.txt không tồn tại.")
    exit()



# In kích thước, số chiều, kiểu dữ liệu và số phần tử
print(data_numpy)
print("------------------")
print('Kích thước biến:', data_numpy.shape)
print('Số chiều của biến:', data_numpy.ndim)
print('Kiểu dữ liệu của các phần tử:', data_numpy.dtype)
print('Số phần tử:', data_numpy.size)

#62
import numpy as np

# Dữ liệu nhiệt độ (ví dụ)
nhiet_do = np.array([
    [33.45, 21.68, 28.34, 25.21, 31.23],  # Hà Nội
    [32.57, 22.6, 29.12, 26.45, 28.97],   # Vinh
    [29.88, 20.93, 27.34, 24.67, 26.89],   # Đà Nẵng
    [28.68, 24.5, 25.67, 27.12, 26.98],   # Nha Trang
    [31.06, 23.22, 28.54, 25.87, 29.43],   # TP.HCM
    [31.37, 23.99, 27.89, 26.12, 30.12]    # Cà Mau
])

ten_thanh_pho = ["Hà Nội", "Vinh (Nghệ An)", "Đà Nẵng", "Nha Trang", "TP Hồ Chí Minh", "Cà Mau"]


# Yêu cầu 2: Tìm nhiệt độ cao nhất, thấp nhất, trung bình của cả 6 thành phố
max_all = np.max(nhiet_do)
min_all = np.min(nhiet_do)
mean_all = np.mean(nhiet_do)

print("---THỐNG KÊ CHO CẢ 6 THÀNH PHỐ---")
print(f"Nhiệt độ cao nhất: {max_all}")
print(f"Nhiệt độ thấp nhất: {min_all}")
print(f"Nhiệt độ trung bình: {mean_all}")
print("-" * 40)



# Yêu cầu 3: Tìm nhiệt độ cao nhất, thấp nhất, trung bình của từng thành phố
for i in range(len(nhiet_do)):
    max_tp = np.max(nhiet_do[i])
    min_tp = np.min(nhiet_do[i])
    mean_tp = np.mean(nhiet_do[i])

    print(f"{i+1}) {ten_thanh_pho[i]}")
    print(f"Nhiệt độ cao nhất: {max_tp}")
    print(f"Nhiệt độ thấp nhất: {min_tp}")
    print(f"Nhiệt độ trung bình: {mean_tp}")
    print()  # In dòng trống để phân cách giữa các thành phố


#63
import numpy as np

# Dữ liệu nhiệt độ từ câu hỏi trước (ví dụ)
nhiet_do = np.array([
    [33.45, 21.68, 28.34, 25.21, 31.23],  # Hà Nội
    [32.57, 22.6, 29.12, 26.45, 28.97],   # Vinh
    [29.88, 20.93, 27.34, 24.67, 26.89],   # Đà Nẵng
    [28.68, 24.5, 25.67, 27.12, 26.98],   # Nha Trang
    [31.06, 23.22, 28.54, 25.87, 29.43],   # TP.HCM
    [31.37, 23.99, 27.89, 26.12, 30.12]    # Cà Mau
])

# Tạo ma trận data_thongke
so_thanh_pho = nhiet_do.shape[0]
data_thongke = np.zeros((3, so_thanh_pho + 1))  # 3 hàng x 7 cột (6 thành phố + 1 cột chung)

# Tính toán và lưu trữ dữ liệu vào data_thongke
for i in range(so_thanh_pho):
    data_thongke[0, i] = np.max(nhiet_do[i])
    data_thongke[1, i] = np.round(np.mean(nhiet_do[i]), 2)  # Làm tròn đến 2 chữ số thập phân
    data_thongke[2, i] = np.min(nhiet_do[i])

# Tính toán cột thống kê chung
data_thongke[0, -1] = np.max(data_thongke[0, :-1])
data_thongke[1, -1] = np.round(np.mean(data_thongke[1, :-1]), 2)
data_thongke[2, -1] = np.min(data_thongke[2, :-1])



# In ma trận data_thongke
print(data_thongke)
print(type(data_thongke))
print("Kích thước:", data_thongke.shape)

# Lưu ra file thongke.txt
np.savetxt("thongke.txt", data_thongke, fmt="%.2f", delimiter=" ") # Định dạng 2 chữ số thập phân

#66
import numpy as np

# Tạo file Diamonds.txt (chỉ để demo, bạn có thể thay thế bằng file của bạn)
with open("Diamonds.txt", "w") as f:
    f.write("0.34 765\n")
    f.write("0.41 827\n")
    f.write("0.75 3120\n")
    # ... thêm dữ liệu khác nếu cần



# Đọc dữ liệu từ file Diamonds.txt vào biến data_diamond
try:
    data_diamond = np.loadtxt("Diamonds.txt")

except FileNotFoundError:
    print("File Diamonds.txt không tồn tại.")
    exit()


# In kích thước, số chiều, kiểu dữ liệu và số phần tử của data_diamond
print(data_diamond)
print("-" * 30) #Thêm dòng phân cách
print(f"Kích thước biến data_diamond: {data_diamond.shape}")
print(f"Số chiều của biến data_diamond: {data_diamond.ndim}")
print(f"Kiểu dữ liệu của các phần tử: {data_diamond.dtype}")
print(f"Số phần tử: {data_diamond.size}")

#67
import numpy as np

# Dữ liệu từ câu hỏi trước (ví dụ) -- Thay bằng dữ liệu của bạn nếu cần
data_diamond = np.array([
    [0.23, 484],
    [0.31, 942],
    [0.2, 345],
    [1.02, 4459],
    [1.63, 14022],
    [1.14, 4212],
    [2.01, 11925],
    [1.28, 9548],
    # ... thêm dữ liệu khác
    [1.75, 9890] # Đảm bảo có đủ 50 dòng dữ liệu như trong hình
])

# Tách mảng data_diamond thành 2 vector
diamond_size = data_diamond[:, 0]
diamond_price = data_diamond[:, 1]

# In kết quả
print("Vector diamond_size:")
print(diamond_size)


print("\nVector diamond_price:")
print(diamond_price)

#68
import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu từ câu hỏi trước (ví dụ) -- Thay bằng dữ liệu của bạn nếu cần
data_diamond = np.array([
    [0.23, 484],
    [0.31, 942],
    [0.2, 345],
    [1.02, 4459],
    [1.63, 14022],
    [1.14, 4212],
    [2.01, 11925],
    [1.28, 9548],
    # ... thêm dữ liệu khác
    [1.75, 9890] # Đảm bảo có đủ 50 dòng dữ liệu như trong hình
])



diamond_size = data_diamond[:, 0]
diamond_price = data_diamond[:, 1]

# Vẽ biểu đồ thể hiện mối quan hệ giữa kích thước và giá bán kim cương
plt.figure(figsize=(6, 4)) #Điều chỉnh kích thước biểu đồ
plt.scatter(diamond_size, diamond_price)
plt.xlabel("Trọng lượng (Carat)")
plt.ylabel("Giá bán ($)")
plt.title("BIỂU ĐỒ THỂ HIỆN MỐI TƯƠNG QUAN GIỮA TRỌNG LƯỢNG (CARAT) VÀ GIÁ BÁN KIM CƯƠNG ($)")
plt.grid(True) #Thêm lưới


# Xác định hệ số tương quan
he_so_tuong_quan = np.corrcoef(diamond_size, diamond_price)[0, 1]
print(f"Hệ số tương quan giữa trọng lượng và giá bán kim cương: {he_so_tuong_quan}")

plt.show()