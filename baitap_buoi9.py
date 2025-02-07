# Bài 2.2.1 (Trang 17): Đọc dữ liệu từ tệp CSV 
import pandas as pd

# Đọc file CSV (thay 'data.csv' bằng tên file của bạn)
df = pd.read_csv('data.csv')

# Hiển thị 5 dòng đầu tiên
print(df.head()) 

# Bài 2.2.2: Xử lý danh sách số nguyên 
def nhap_danh_sach():
    lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
    return lst

def tinh_tong_chan(lst):
    return sum(x for x in lst if x % 2 == 0)

def sap_xep_tang_dan(lst):
    return sorted(lst)

def main():
    danh_sach = nhap_danh_sach()
    print(f"Tổng các số chẵn trong danh sách: {tinh_tong_chan(danh_sach)}")
    danh_sach_sap_xep = sap_xep_tang_dan(danh_sach)
    print(f"Danh sách sau khi sắp xếp: {danh_sach_sap_xep}")

if __name__ == "__main__":
    main()


#Bài 2.3 (Trang 28): Đọc dữ liệu từ tệp JSON
import pandas as pd

# Đọc file JSON
df = pd.read_json('data.json')

# Hiển thị dữ liệu
print(df.head())

#  Bài 2.4 (Trang 34): Đọc dữ liệu từ API
import pandas as pd
import requests

# URL API mẫu (có thể thay bằng API khác)
url = "https://jsonplaceholder.typicode.com/posts"

# Gửi request và lấy dữ liệu
response = requests.get(url)
data = response.json()

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Hiển thị thông tin
print(df.head())

# Bài 2.5 (Trang 41): Đọc dữ liệu từ MongoDB
from pymongo import MongoClient
import pandas as pd

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["database_name"]
collection = db["collection_name"]

# Lấy dữ liệu từ MongoDB
data = list(collection.find())

# Chuyển thành DataFrame
df = pd.DataFrame(data)

# Hiển thị thông tin
print(df.head())

# Bài 4.1 (Trang 48): Xử lý dữ liệu với Pandas
import pandas as pd

# Đọc file CSV
df = pd.read_csv('data.csv')

# Xóa hàng có giá trị NaN
df_cleaned = df.dropna()

# Hiển thị dữ liệu
print(df_cleaned.head())

#Bài 4.2 (Trang 49): Chuẩn hóa dữ liệu
import pandas as pd

# Đọc file CSV
df = pd.read_csv('data.csv')

# Chuyển đổi dữ liệu chữ thành chữ thường
df['column_name'] = df['column_name'].str.lower()

# Hiển thị kết quả
print(df.head())

# Bài 5.1 (Trang 56): Tạo tập dữ liệu mẫu với sklearn
from sklearn.datasets import make_classification
import pandas as pd

# Tạo dữ liệu
X, y = make_classification(n_samples=100, n_features=5, random_state=42)

# Chuyển thành DataFrame
df = pd.DataFrame(X, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
df['Label'] = y

# Hiển thị dữ liệu
print(df.head())

#  Bài 5.2 (Trang 57): Lưu dữ liệu vào CSV
import pandas as pd

# Giả sử df là DataFrame có dữ liệu
df.to_csv('output.csv', index=False)

print("Dữ liệu đã được lưu vào output.csv")

#Bài 6.1 (Trang 64): Vẽ biểu đồ với Matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Đọc dữ liệu từ CSV
df = pd.read_csv('data.csv')

# Vẽ biểu đồ cột
plt.bar(df['column_name'], df['value'])
plt.xlabel('Tên cột')
plt.ylabel('Giá trị')
plt.title('Biểu đồ cột')
plt.show()
