#Bài 8: Xây dựng lớp Person
class Person:
    def __init__(this, name, year, height, weight):
        """
        Hàm khởi tạo cho lớp Person
        """
        this.name = name
        this.year = year
        this.height = height
        this.weight = weight

    def greeting(this):
        """
        Phương thức hiển thị thông tin của Person
        """
        return f"Họ tên: {this.name}, Năm sinh: {this.year}, Chiều cao: {this.height} m, Cân nặng: {this.weight} kg"

    def bmi(this):
        """
        Phương thức tính chỉ số BMI của Person
        :return: Chỉ số BMI và phân loại tình trạng cân nặng
        """
        bmi_value = this.weight / (this.height ** 2)

        if bmi_value < 18.5:
            return f"BMI của bạn là {bmi_value:.2f}. Bạn đang thiếu cân."
        elif 18.5 <= bmi_value <= 24.9:
            return f"BMI của bạn là {bmi_value:.2f}. Cân nặng của bạn bình thường."
        elif 25 <= bmi_value <= 29.9:
            return f"BMI của bạn là {bmi_value:.2f}. Bạn đang thừa cân."
        else:
            return f"BMI của bạn là {bmi_value:.2f}. Bạn đang béo phì."


# Nhập thông tin từ bàn phím
name = input("Nhập họ và tên: ")
year = int(input("Nhập năm sinh: "))
height = float(input("Nhập chiều cao (m): "))
weight = float(input("Nhập cân nặng (kg): "))

# Tạo đối tượng Person
person = Person(name, year, height, weight)

# Hiển thị thông tin và kết quả BMI
print(person.greeting())
print(person.bmi())



#Bai 9:  Tập tin
# Mở file để đọc dữ liệu
f = open('demo.txt')

#Đọc nội dung của file vào biến st
st = f.read()

print('Nội dung file: ')
print(st)

# Mở file để đọc dữ liệu
f = open('demo.txt')

#Đọc 15: ký tự đầu tiên của file
st1 = f.read(15)

print(st1, '-- Số ký tự là: ', len(st1))


#Bài 10: Đọc file
#Mở file để đọc dữ liệu
f = open('demo.txt')

#Đọc từng dòng dữ liệu của file
print(f.readline())
print(f.readline())

#Đóng file dữ liệu
f.close()

# Mở file để đọc dữ liệu
f = open("demo.txt")

#Đọc tất cả các dòng của file
for x in f:
    print(x)
    
#Đóng file dữ liệu
f.close()


#Bài 11: Ghi file

f1= open('Ghifile.txt', 'a+')
#Dữ Liệu muốn ghi vào file
st = 'This is new line.....'
#Ghi tiếp dữ liệu vào file
f1.write(st) 
f1.close()
f = open("Ghifile.txt", "r")
print(f.read())

#Bai12: 
#Lấy các thông số của file
f2= open('Ghifile.txt')
print('1. Tên file:', f2.name)
print('2. Chế độ mở file:', f2.mode)
print('3. Trạng thái đóng file:', f2.closed)

#Bai13:
# Mở file để ghi  
fo = open("data.txt", "w")  
# Ghi dữ liệu lên file  
fo.write("Tobe or not tobe. \n Nghi lon de thanh cong ! \n");  
# Close opened file  
fo.close()  
print("Ghi file thanh cong !")

#Bai14:
obj=open("test.txt","w")  
obj.write("Chao mung cac ban den voi khoa CNTT")  
obj.close()  
obj1=open("test.txt","r")  
s=obj1.read()  
print (s)  
obj1.close()  
obj2=open("test.txt","r")  
s1=obj2.read(20)  
print (s1)  
obj2.close()


#Bai15: 
def doi_cho_so_lon_nhat_nho_nhat(filename_input, filename_output):
    """
    Đổi chỗ phần tử lớn nhất và nhỏ nhất trong một dãy số.

    Args:
        filename_input (str): Tên file đầu vào.
        filename_output (str): Tên file đầu ra.
    """

    with open(filename_input, 'r') as f:
        numbers = list(map(int, f.read().split()))

    # Tìm vị trí của số lớn nhất và nhỏ nhất xuất hiện đầu tiên
    max_value = numbers[0]
    min_value = numbers[0]
    max_index = 0
    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
        elif numbers[i] < min_value:
            min_value = numbers[i]
            min_index = i

    # Đổi chỗ
    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

    # Ghi vào file mới
    with open(filename_output, 'w') as f:
        f.write(' '.join(map(str, numbers)))

# Gọi hàm với tên file cụ thể
doi_cho_so_lon_nhat_nho_nhat('dayso1_bai17.txt', 'dayso2_bai17.txt')