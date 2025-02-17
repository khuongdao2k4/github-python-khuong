#1
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('electronics_store.db')
cursor = conn.cursor()

# Hàm thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = float(entry_price.get())
    quantity = int(entry_quantity.get())
    
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    messagebox.showinfo("Thông báo", "Sản phẩm đã được thêm thành công!")
    view_products()

# Hàm xem sản phẩm
def view_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    listbox_products.delete(0, tk.END)
    for row in rows:
        listbox_products.insert(tk.END, f"ID: {row[0]}, Tên: {row[1]}, Giá: {row[2]}, Số lượng: {row[3]}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý bán thiết bị điện tử")

# Tạo các widget
label_name = tk.Label(root, text="Tên sản phẩm:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_price = tk.Label(root, text="Giá:")
label_price.grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

label_quantity = tk.Label(root, text="Số lượng:")
label_quantity.grid(row=2, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=2, column=1)

button_add = tk.Button(root, text="Thêm sản phẩm", command=add_product)
button_add.grid(row=3, column=0, columnspan=2)

listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=4, column=0, columnspan=2)

# Hiển thị danh sách sản phẩm ban đầu
view_products()

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát
conn.close()

#2
import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
    
# in đối tượng connection ra màn hình 
print(myconn) 

#3
import mysql.connector 
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
passwd = "", database = "oidoioi") 
# in đối tượng connection ra màn hình 
print(myconn) 

#4
import mysql.connector 

myconn = mysql.connector.connect(host = "localhost", user = "root",  
passwd = "", database = "oidoioi") 
# in đối tượng connection ra màn hình 
print(myconn) 
# tạo đối tượng cursor 
cur = myconn.cursor() 
# in đối tượng cursor ra màn hình 
print(cur)

#5
import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
  
# tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    dbs = cur.execute("show databases") 
except: 
    myconn.rollback() 
for x in cur: 
    print(x) 
myconn.close() 

#6
import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    password = "") 
  
# tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    cur.execute("create database PythonDB") 
    dbs = cur.execute("show databases") 
except: 
    myconn.rollback() 
for x in cur: 
    print(x) 
myconn.close()

#7
import mysql.connector 

# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
        password = "", database = "pythondb") 
    
# tạo đối tượng cursor 
cur = myconn.cursor()   
    
try: 
    # tạo bảng Employee gồm 4 cột name, id, salary, và department id   
    dbs = cur.execute("create table Employee(name varchar(20) not null, " 
        + "id int(20) not null primary key, salary float not null, " 
        + "dept_id int not null)") 
except:  
    myconn.rollback() 

myconn.close()

#8
import mysql.connector
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
        passwd = "", database = "PythonDB") 
    
# tạo đối tượng cursor 
cur = myconn.cursor()   
    
try: 
    # thêm cột branch name vào bảng Employee 
    cur.execute("alter table Employee add branch_name varchar(20) not null") 
except: 
    myconn.rollback() 

myconn.close() 

#9
import mysql.connector 
  
#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
sql = ("insert into Employee(name, id, salary, dept_id, branch_name) " 
    + "values (%s, %s, %s, %s, %s)") 
  
#giá trị của một row được cung cấp dưới dạng tuple 
val = ("The Mac", 10001, 25000.00, 101, "Hanoi") 
  
try: 
    #inserting the values into the table 
    cur.execute(sql,val) 
  
    #commit the transaction 
    myconn.commit() 
  
except: 
    myconn.rollback() 
  
print(cur.rowcount,"record inserted!") 
myconn.close() 

#10
import mysql.connector 
  
#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
sql = ("insert into Employee(name, id, salary, dept_id, branch_name) " 
    "values (%s, %s, %s, %s, %s)") 
  
#giá trị của một row được cung cấp dưới dạng tuple 
val = [("Vinh", 10002, 26000.00, 101, "Hanoi"),  
       ("Trung", 10003, 26000.00, 102, "Danang")] 
  
try: 
    #inserting the values into the table 
    cur.executemany(sql, val) 
  
    #commit the transaction 
    myconn.commit() 
  
except: 
    myconn.rollback() 
  
print(cur.rowcount,"record inserted!") 
myconn.close() 

#11
import mysql.connector 
  
#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    # select dữ liệu từ database 
    cur.execute("SELECT * FROM Employee") 
      
    # tìm nạp các hàng từ đối tượng con trỏ   
    result = cur.fetchall() 
  
    for x in result: 
        print(x);  
  
except: 
    myconn.rollback() 
  
myconn.close() 

#12
import mysql.connector 
  
#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    cur.execute("SELECT name, id, salary FROM Employee") 
      
    # tìm nạp các hàng từ đối tượng con trỏ   
    result = cur.fetchall() 
  
    for x in result: 
        print(x);  
  
except: 
    myconn.rollback() 
  
myconn.close() 

#13
import mysql.connector 

#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
#tạo đối tượng cursor 
cur = myconn.cursor() 

try: 
    # select dữ liệu từ database 
    cur.execute("SELECT name, id, salary FROM Employee") 
    # tìm nạp hàng đầu tiên từ đối tượng con trỏ   
    result = cur.fetchone() 
    print(result); 

    # tìm nạp hàng tiếp theo từ đối tượng con trỏ   
    result = cur.fetchone() 
    print(result); 

except: 
    myconn.rollback() 
      
myconn.close()

#14
import mysql.connector 
  
#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    # select dữ liệu từ database 
    cur.execute("SELECT name, id, salary FROM Employee") 
      
    # tìm nạp các hàng từ đối tượng con trỏ   
    result = cur.fetchall() 
  
    print("Name    ID    Salary") 
      
    for row in result: 
        print("%s    %d    %d"%(row[0],row[1],row[2])) 
  
except: 
    myconn.rollback() 
    
#15
import mysql.connector 

#tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "", database = "PythonDB") 
  
#tạo đối tượng cursor 
cur = myconn.cursor() 
  
try: 
    # cập nhật name cho bảng Employee 
    cur.execute("update Employee set name = 'Đạt' where id = 10001") 
    myconn.commit() 
  
except: 
    myconn.rollback() 
  
myconn.close() 

