#11
import pandas as pd

path = 'Data_Excersice\\CSV\\Data_CSV.csv'

#Sử dụng phương thức read_csv
data = pd.read_csv(path)

#Hiển thị thông tin biến Data
data.info()

#13
import pandas as pd

#Sử dụng phương thức read_csv()
#Tham số: Thiết lập cột index là cột Personal
data1 = pd.read_csv(path,
                    index_col=0)

data1.info()

#Hiển thị dữ liệu 5 dòng đầu tiên
data1.head()

#14
import pandas as pd

#Sử dụng phương thức read_csv()
#Thiết lập số hàng, cột muốn đọc dữ liệu
data2 = pd.read_csv(path,
                    nrows=100,
                    usecols=['Height_cm', 'Weight_kg'])
data2.info()

#15
import pandas as pd

#Thiết lập tham số đọc dữ liệu từ dòng thứ 5 trong file
#và đặt lại tên của các cột dữ liệu
data3 = pd.read_csv(path,
                    names=['ID', 'Sex', 'H(cm)', 'W(kg)'],
                    skiprows=5)

data3.info()

#21
import pandas as pd

path_excel = 'Data_Excersice\\Data_Excel.xlsx'

#Đọc dữ liệu từ file excel
data_ex = pd.read_excel(path_excel)
data_ex.info()

#Hiển thị 5 dòng dữ liệu đầu tiên
data_ex.head()

#23
import pandas as pd

#Ví dụ:
#Đọc dữ liệu tại sheet đầu tiên,
#Chỉ lấy dữ liệu cột Mã SV và các cột điểm
#Thiết lập cột đầu tiên làm index
data_ex1 = pd.read_excel(path_excel,
                          sheet_name=0,
                          usecols=[1,2,3,4,5,6,7,8,9,10],
                          index_col=0)

data_ex1.info()

#Hiển thị 5 dòng dữ liệu đầu tiên
data_ex1.head()

#25
import pandas as pd

#Đọc dữ liệu tại sheet 2,từ dòng 9
data_ex3 = pd.read_excel(path_excel,
                          sheet_name='4080130_02',
                          skiprows=9)

data_ex3.info()

#Hiển thị 5 dòng dữ liệu đầu tiên
data_ex3.head()

#26
import pandas as pd

data_ex41 = pd.read_excel(path_excel,
                          sheet_name='4080130_03',
                          header=None,
                          usecols=[1,6,7,8,9,10],
                          names=['Mã SV','A','B1','B2','C1','C2'],
                          index_col=0)

data_ex41.info()

#Hiển thị 5 dòng dữ liệu đầu tiên
data_ex41.head()

#31 
import pandas as pd

path_json = 'Data_Excersice\\json_Data_product.json'

#Đọc dữ liệu từ file Json vào biến DataFrame
data_json = pd.read_json(path_json)
data_json

#Đọc dữ liệu từ file Json vào biến DataFrame
#Sử dụng tham số orient='index'
data_json1 = pd.read_json(path_json, orient='index')
data_json1

#32
#Hoặc Sử dụng thư viện json làm việc với dữ liệu json
import json

with open(path_json, 'r') as myfile:
    data=myfile.read()

# Đọc dữ liệu vào biến obj
obj = json.loads(data)
type(obj)

#Lấy giá trị của key = 'Product'
obj['Product']

#Lấy giá trị của key = 'Price'
obj['Price']# Ví dụ trang 14: Đọc 100 dòng đầu tiên từ CSV
import pandas as pd

# Đọc 100 dòng đầu tiên
df = pd.read_csv('data.csv', nrows=100)

# Hiển thị dữ liệu
print(df)

#Ví dụ trang 15: Đọc CSV từ dòng thứ 5 và đổi tên cột
import pandas as pd

# Đọc file CSV từ dòng thứ 5, đặt lại tên cột
df = pd.read_csv('data.csv', skiprows=4, names=['ID', 'Sex', 'H(cm)', 'W(kg)'])

# Hiển thị dữ liệu
print(df)

# Ví dụ trang 21: Đọc file Excel
import pandas as pd

# Đọc file Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Hiển thị dữ liệu
print(df.head())

# Ví dụ trang 23: Đọc file Excel với một số tham số
import pandas as pd

# Đọc sheet 2 từ dòng thứ 9
df = pd.read_excel('data.xlsx', sheet_name='Sheet2', skiprows=8)

# Hiển thị dữ liệu
print(df.head())

#  Ví dụ trang 24: Đọc sheet 3 không có header
import pandas as pd

# Đọc file Excel sheet 3 không có header
df = pd.read_excel('data.xlsx', sheet_name='Sheet3', header=None)

# Hiển thị dữ liệu
print(df.head())

#Ví dụ trang 25: Đọc cột cụ thể từ Excel
import pandas as pd

# Đọc chỉ các cột 1,6,7,8,9,10 và đặt tên cột
df = pd.read_excel('data.xlsx', sheet_name='Sheet3', usecols=[0, 5, 6, 7, 8, 9], 
                   names=['Mã SV', 'A', 'B1', 'B2', 'C1', 'C2'])

# Hiển thị dữ liệu
print(df.head())

# Ví dụ trang 26: Thiết lập cột đầu tiên làm index
import pandas as pd

# Đọc file Excel và đặt cột đầu tiên làm index
df = pd.read_excel('data.xlsx', sheet_name='Sheet3', index_col=0)

# Hiển thị dữ liệu
print(df.head())

# Ví dụ trang 31: Đọc file JSON
import pandas as pd

# Đọc file JSON
df = pd.read_json('data.json')

# Hiển thị dữ liệu
print(df.head())

#Ví dụ trang 32: Đọc JSON bằng thư viện json
import json

# Đọc file JSON
with open('data.json') as file:
    data = json.load(file)

# Hiển thị dữ liệu
print(data)

# Ví dụ trang 38: Lấy dữ liệu từ API
import requests # type: ignore
import pandas as pd

# Gọi API lấy dữ liệu
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

# Chuyển thành DataFrame
df = pd.DataFrame(data)

# Hiển thị dữ liệu
print(df.head())

# Ví dụ trang 39: Gửi request với tham số
import requests # type: ignore

# Gửi request với tham số
params = {'q': 'python'}
response = requests.get('https://api.github.com/search/repositories', params=params)

# Hiển thị kết quả
print(response.json())

# Ví dụ trang 45: Kết nối MongoDB
from pymongo import MongoClient # type: ignore

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Lấy danh sách collection
print(db.list_collection_names())

# Ví dụ trang 46: Chuyển dữ liệu MongoDB sang DataFrame
import pandas as pd
from pymongo import MongoClient # type: ignore

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Lấy dữ liệu
data = list(collection.find({}, {"_id": 0}))

# Chuyển thành DataFrame
df = pd.DataFrame(data)

# Hiển thị dữ liệu
print(df.head())

# Ví dụ trang 51: Sử dụng Sklearn để lấy dataset
from sklearn.datasets import load_iris # type: ignore
import pandas as pd

# Lấy dữ liệu iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Hiển thị dữ liệu
print(df.head())

# Ví dụ trang 60: Tạo dataset phân lớp
from sklearn.datasets import make_classification # type: ignore

# Tạo dataset
X, y = make_classification(n_samples=100, n_features=5, random_state=42)

# Hiển thị dữ liệu
print(X[:5])

#  Trang 61: Tạo Dữ Liệu Mẫu cho Bài Toán Hồi Quy 
from sklearn.datasets import make_regression # type: ignore
import matplotlib.pyplot as plt

# Tạo dữ liệu hồi quy
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Vẽ biểu đồ dữ liệu
plt.scatter(X, y)
plt.title('Dữ liệu mẫu hồi quy')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.show()

# Trang 62: Tạo Dữ Liệu Mẫu cho Bài Toán Phân Cụm
from sklearn.datasets import make_blobs # type: ignore
import matplotlib.pyplot as plt

# Tạo dữ liệu phân cụm
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Vẽ biểu đồ phân tán
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Dữ liệu mẫu phân cụm')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
