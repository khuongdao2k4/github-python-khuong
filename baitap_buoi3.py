#Bai 1
def greeting(hoten, namsinh):
    print('Hello,', hoten,',',namsinh)

greeting('Khuong', 2004)

#Bai 2
def rabbit_count():
    try:
        # Nhập số tháng từ người dùng
        month = int(input("Nhập số tháng (số nguyên không âm): "))

        if month < 0:
            raise ValueError("Số tháng phải là số nguyên không âm.")

        # Số thỏ ban đầu
        rabbits = 2

        # Tính số lượng thỏ
        for _ in range(month):
            rabbits *= 2

        # Xuất kết quả
        print(f"Số lượng thỏ sau {month} tháng là: {rabbits}")

    except ValueError as e:
        print(f"Lỗi: {e}. Vui lòng nhập số nguyên không âm.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {e}")

rabbit_count(5)

#Bai 3
def count_mark(score_list):
    
    total_students = len(score_list)  # Tổng số sinh viên
    repeat_students = score_list.count('F')  # Số sinh viên học lại (điểm F)
    
    return repeat_students, total_students

# Ví dụ bảng điểm
score_list = ['C', 'B', 'D', 'A', 'F', 'B', 'F', 'B', 'C', 'A', 'D', 'F', 'D', 'F', 'B']

# Gọi hàm và in kết quả
repeat_students, total_students = count_mark(score_list)
print(f"Tổng số học sinh trong lớp: {total_students}")
print(f"Số học sinh phải học lại (điểm F): {repeat_students}")

#Bai 4
def show_bmi(chieu_cao_m, can_nang_kg):
    """
    Tính toán và diễn giải chỉ số khối cơ thể (BMI).

    Args:
        chieu_cao_m: Chiều cao tính bằng mét (float).
        can_nang_kg: Cân nặng tính bằng kilôgam (float).

    Returns:
        Một chuỗi biểu thị chỉ số BMI và diễn giải tương ứng.
        Trả về None nếu đầu vào không hợp lệ.
    """

    if chieu_cao_m <= 0 or can_nang_kg <= 0:
        print("Đầu vào không hợp lệ. Chiều cao và cân nặng phải là số dương.")
        return None

    bmi = can_nang_kg / (chieu_cao_m ** 2)

    if bmi < 18.5:
        ket_qua = f"BMI của bạn là {bmi:.2f}. Bạn đang thiếu cân."
    elif 18.5 <= bmi <= 24.9:
        ket_qua = f"BMI của bạn là {bmi:.2f}. Cân nặng của bạn bình thường."
    elif 25 <= bmi <= 29.9:
        ket_qua = f"BMI của bạn là {bmi:.2f}. Bạn đang thừa cân."
    else:
        ket_qua = f"BMI của bạn là {bmi:.2f}. Bạn đang béo phì."


    return ket_qua




# Ví dụ sử dụng
chieu_cao = float(input("Nhập chiều cao của bạn (mét): "))
can_nang = float(input("Nhập cân nặng của bạn (kilôgam): "))

bmi_info = show_bmi(chieu_cao, can_nang)

if bmi_info:
    print(bmi_info)

#Bai 5
def cal_point(diem_he_10):
    """
    Tính điểm trung bình hệ 10 và hệ 4 từ danh sách điểm hệ 10.

    Args:
        diem_he_10: Danh sách điểm hệ 10 của một học sinh.

    Returns:
        Một tuple chứa điểm trung bình hệ 10 và điểm trung bình hệ 4.
    """

    tong_diem = sum(diem_he_10)
    dtb_he_10 = tong_diem / len(diem_he_10)

    diem_chu = []
    diem_he_4 = []
    for diem in diem_he_10:
        if 9 <= diem <= 10:
            diem_chu.append("A*")
            diem_he_4.append(4.0)
        elif 8.5 <= diem <= 8.9:
            diem_chu.append("A")
            diem_he_4.append(3.7)
        elif 8 <= diem <= 8.4:
            diem_chu.append("B*")
            diem_he_4.append(3.5)
        elif 7 <= diem <= 7.9:
            diem_chu.append("B")
            diem_he_4.append(3.0)
        elif 6.5 <= diem <= 6.9:
            diem_chu.append("C*")
            diem_he_4.append(2.5)
        elif 5.5 <= diem <= 6.4:
            diem_chu.append("C")
            diem_he_4.append(2.0)
        elif 5 <= diem <= 5.4:
            diem_chu.append("D*")
            diem_he_4.append(1.5)
        elif 4 <= diem <= 4.9:
            diem_chu.append("D")
            diem_he_4.append(1.0)
        elif diem < 4:
            diem_chu.append("F")
            diem_he_4.append(0)


    dtb_he_4 = sum(diem_he_4) / len(diem_he_4)



    return dtb_he_10, dtb_he_4, diem_chu


# Ví dụ
diem_he_10 = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
dtb_10, dtb_4, diem_chu = cal_point(diem_he_10)
print(f"Điểm hệ 10: {diem_he_10}")
print(f"Điểm chữ tương ứng: {diem_chu}")
print(f"DTB hệ 10: {dtb_10}")
print(f"DTB hệ 4: {dtb_4}")

#Bai 6
def list_prime(n):
    """
    Trả về danh sách các số nguyên tố từ 2 đến n.

    Args:
        n: Giới hạn trên của khoảng tìm kiếm.

    Returns:
        Danh sách các số nguyên tố.
    """

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes

# Ví dụ
n = int(input("Nhập một số nguyên dương n:"))
danh_sach_nguyen_to = list_prime(n)
print(danh_sach_nguyen_to)