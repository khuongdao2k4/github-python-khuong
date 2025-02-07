print("Xin chào! Mình là ĐÀO MINH KHƯƠNG")
print("Lớp DCCNTT 13.10.11")

#Bài 1: Chia kẹo.
# Nhập số kẹo và số học sinh
so_keo = int(input("Nhập số kẹo của cô: "))
so_hoc_sinh = int(input("Nhập số học sinh trong lớp: "))

# Tính toán
if so_hoc_sinh == 0:
    print("Không thể chia kẹo vì không có học sinh!")
else:
    if so_keo < so_hoc_sinh:
        print("Không thể chia đều vì số kẹo nhỏ hơn số học sinh!")
    else:
        so_keo_moi_hoc_sinh = so_keo // so_hoc_sinh
        so_keo_con_lai = so_keo % so_hoc_sinh

        # Kết quả
        print(f"Mỗi học sinh được nhận: {so_keo_moi_hoc_sinh} cái kẹo")
        print(f"Số kẹo còn lại: {so_keo_con_lai}")


#Bài 2: Tính Tuổi 
from datetime import datetime

# Họ tên và năm sinh đã được xác định
ho_ten = "Mai Phương Thúy"  # Tên đã được xác định
nam_sinh = 2000  # Năm sinh đã được xác định

# Tính tuổi
nam_hien_tai = datetime.now().year
tuoi = nam_hien_tai - nam_sinh

# Hiển thị kết quả
print(f"Chào bạn {ho_ten}, bạn {tuoi} tuổi.")

#Bài 3: Cho biết số thỏ trong rừng
# Đặt giá trị cho so_thang là 3 theo yêu cầu
so_thang = 3
# Tính số lượng thỏ
so_tho = 2 ** so_thang 

# Hiển thị kết quả
print(f"Trong rừng có: {so_tho} con thỏ")

#Bài 4: Chuỗi văn bản 
# Đoạn văn
doan_van = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

# 1. Số ký tự trong đoạn văn
so_ky_tu = len(doan_van)
print(f"Số ký tự có trong đoạn văn: {so_ky_tu}")

# 2. Kiểm tra từ có xuất hiện hay không (không phân biệt hoa thường)
tim_ho_chi_minh = "hồ chí minh" in doan_van.lower()
tim_non_song = "non sông" in doan_van.lower()
print(f"Có chứa 'hồ chí minh': {tim_ho_chi_minh}")
print(f"Có chứa 'non sông': {tim_non_song}")

# 3. Tách đoạn văn thành các câu bằng dấu '.'
cac_cau = doan_van.split('.')
print(f"Các câu trong đoạn văn: {cac_cau}")

# 4. Kiểm tra có ký tự nào khác chữ và số hay không
ky_tu_dac_biet = any(not char.isalnum() and not char.isspace() for char in doan_van)
print(f"Có ký tự nào khác chữ và số: {ky_tu_dac_biet}")

# 5. Thay thế 'Việt Nam' bằng 'VIỆT NAM'
doan_van_thay_the = doan_van.replace('Việt Nam', 'VIỆT NAM')
print(f"Đoạn văn sau khi thay thế: {doan_van_thay_the}")

#Bài 5: Thống kê điểm Học Viên
# Danh sách điểm thi môn "Python for Analysis" của lớp AIV_EVNICT
diem_thi = ['A', 'B', 'C', 'A', 'F', 'D', 'B', 'A', 'F', 'C', 'B', 'D', 'F', 'A', 'C']

# 1) Số sinh viên trong lớp
so_sinh_vien = len(diem_thi)
print(f"Số sinh viên trong lớp: {so_sinh_vien}")

# 2) Số sinh viên phải học lại môn này (điểm F)
so_sinh_vien_hoc_lai = diem_thi.count('F')
print(f"Số sinh viên phải học lại môn này: {so_sinh_vien_hoc_lai}")

# 3) Số sinh viên có điểm từ B trở lên (B, A)
so_sinh_vien_b_or_up = sum(1 for diem in diem_thi if diem in ['A', 'B'])
print(f"Số sinh viên có điểm từ B trở lên: {so_sinh_vien_b_or_up}")

# 4) Tạo bảng điểm mới sau khi loại bỏ điểm của sinh viên đầu tiên và cuối cùng
diem_thi_moi = diem_thi[1:-1]  # Loại bỏ sinh viên đầu tiên và cuối cùng
print(f"Bảng điểm mới sau khi loại bỏ sinh viên đầu tiên và cuối cùng: {diem_thi_moi}")
#tôi là khương
