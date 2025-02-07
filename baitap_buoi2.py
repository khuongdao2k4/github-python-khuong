#Bai6: Nhập chữ cái Hoa
str = input("Nhập chữ cái (Hoa) bất kỳ: ")
phu = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R" , "S", "T", "V", "W" , "X", "Y", "Z"]
nguyen = ["U", "E", "O", "A", "I"]
if str in nguyen:
    print("Đây là nguyên âm!")
else:
    print("Đây là phụ âm!")



#Bai7: Tính chỉ số BMI
hight = input("Nhập chiều cao: ")
weight = input("Nhập cân nặng: ")
bmi = weight / (hight*hight)
print(f"Chỉ số BMI{bmi}")



#Bai8: Xác định mùa trong năm
namsinh = input("Nhập tháng sinh: ")
xuan = ["1", "2", "3"]
ha = ["4", "5", "6"]
thu = ["7", "8", "9"]
dong = ["10", "11", "12"]
if namsinh in xuan:
    print("Bạn sinh vào mùa Xuân")
elif namsinh in ha:
    print("Bạn sinh vào mùa Hạ")
elif namsinh in thu:
    print("Bạn sinh vào mùa Thu")
elif namsinh in dong:
    print("Bạn sinh vào mùa Đông")
else:
    print("Vui lòng nhập tháng sinh từ 1-12")



#Bai9: Hiển thị bảng cửu chương
giatri = input("Nhập bảng cửu chương bạn muốn in: ")
print(f"Bảng cửu chương {giatri}: ")
for x in range(1, 11):
    print(f"{giatri} x {x} = {giatri * x}")
    
#Bai10: Tính điểm học tập
diem = [9.0, 8.9, 7.8]
diem_chu = []
for i in diem:
    if 9.0 < i <= 10:
        diem_chu.append("A+")
    elif 8.5 < i <= 8.9:
        diem_chu.append("A")
    elif 8.0 < i <=8.4:
        diem_chu.append("B+")
    elif 7.5 < i <= 7.9:
        diem_chu.append("B")
    elif 7.0<i<=7.4:
        diem_chu.append("C+")
    elif 6.5<i<=6.9:
        diem_chu.append("C")
    elif 6.0<i<=6.4:
        diem_chu.append("C")
    elif 6.5<i<=6.9:
        diem_chu.append("C")
print(diem_chu)



#Bai11: Kiểm tra số nguyên tố
def is_prime(n):
    # Kiểm tra nếu số nhỏ hơn 2
    if n < 2:
        return False
    
    # Kiểm tra các ước từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Nhập số tự nhiên từ người dùng
try:
    number = int(input("Nhập một số tự nhiên: "))
    if number < 0:
        print("Vui lòng nhập một số tự nhiên không âm.")
    elif is_prime(number):
        print(f"{number} là số nguyên tố.")
    else:
        print(f"{number} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")



# Bài 12: Hiển thị số NT từ 2 Tới N
def is_prime(num):
    # Hàm kiểm tra số nguyên tố
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_up_to_n(n):
    # Hàm lấy danh sách các số nguyên tố từ 2 đến n
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

# Nhập số N từ người dùng
try:
    N = int(input("Nhập số tự nhiên N: "))
    if N < 2:
        print("Không có số nguyên tố nào trong khoảng này.")
    else:
        prime_list = primes_up_to_n(N)
        print(f"Các số nguyên tố từ 2 tới {N} là: {prime_list}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")



#Bài 13: Chuyển N sang nhị phân:
def decimal_to_binary(n):
    # Hàm chuyển đổi số thập phân sang nhị phân
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Nhập số tự nhiên N từ người dùng
try:
    N = int(input("Nhập số tự nhiên N (N > 0): "))
    if N <= 0:
        print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
    else:
        binary_representation = decimal_to_binary(N)
        print(f"Số {N} trong hệ nhị phân là: {binary_representation}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")



#Bài 14:Tìm max - min - mean
# Khởi tạo danh sách chiều cao (dữ liệu mẫu)
student_heights = [1.65, 1.70, 1.80, 1.55, 1.60, 1.75, 1.68, 1.72]

# 1. Chiều cao cao nhất và thấp nhất
max_height = max(student_heights)
min_height = min(student_heights)

# 2. Chiều cao trung bình
average_height = sum(student_heights) / len(student_heights)

# 3. Số lượng sinh viên có chiều cao >= chiều cao trung bình
above_average_count = sum(1 for height in student_heights if height >= average_height)

# Hiển thị kết quả
print(f"Chiều cao cao nhất trong lớp: {max_height:.2f} m")
print(f"Chiều cao thấp nhất trong lớp: {min_height:.2f} m")
print(f"Chiều cao trung bình của lớp: {average_height:.2f} m")
print(f"Số lượng sinh viên có chiều cao lớn hơn hoặc bằng trung bình: {above_average_count}")


