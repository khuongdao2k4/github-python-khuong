# 1. Kiểm tra kết nối Python với MySQL
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456")
print(myconn)

# 2. Tạo đối tượng kết nối Python với MySQL
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456")
print(myconn)

# 3. Kết nối với một cơ sở dữ liệu cụ thể
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="mydb")
print(myconn)

# 4. Tạo đối tượng con trỏ
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="mydb")
cur = myconn.cursor()
print(cur)

# 5. Lấy danh sách các cơ sở dữ liệu
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456")
cur = myconn.cursor()
cur.execute("SHOW DATABASES")
for x in cur:
    print(x)
myconn.close()

# 6. Tạo cơ sở dữ liệu mới
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456")
cur = myconn.cursor()
cur.execute("CREATE DATABASE PythonDB")
myconn.close()

# 7. Tạo bảng trong MySQL
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("CREATE TABLE Employee (name VARCHAR(20) NOT NULL, id INT PRIMARY KEY, salary FLOAT NOT NULL, dept_Id INT NOT NULL)")
myconn.close()

# 8. Thêm cột vào bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("ALTER TABLE Employee ADD branch_name VARCHAR(20) NOT NULL")
myconn.close()

# 9. Chèn một bản ghi vào bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
sql = "INSERT INTO Employee(name, id, salary, dept_id, branch_name) VALUES (%s, %s, %s, %s, %s)"
val = ("The Mac", 10001, 25000.00, 101, "Hanoi")
cur.execute(sql, val)
myconn.commit()
myconn.close()

# 10. Chèn nhiều bản ghi vào bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
sql = "INSERT INTO Employee(name, id, salary, dept_id, branch_name) VALUES (%s, %s, %s, %s, %s)"
val = [("Vinh", 10002, 26000.00, 101, "Hanoi"), ("Trung", 10003, 26000.00, 102, "Danang")]
cur.executemany(sql, val)
myconn.commit()
myconn.close()

#11. Lấy toàn bộ dữ liệu từ bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("SELECT * FROM Employee")
result = cur.fetchall()
for x in result:
    print(x)
myconn.close()

#12. Đọc cột cụ thể từ bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("SELECT name, id, salary FROM Employee")
result = cur.fetchall()
for x in result:
    print(x)
myconn.close()

# 13. Lấy từng dòng dữ liệu với fetchone()
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("SELECT name, id, salary FROM Employee")
result = cur.fetchone()
print(result)
result = cur.fetchone()
print(result)
myconn.close()

# 14. Định dạng kết quả khi đọc dữ liệu
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("SELECT name, id, salary FROM Employee")
result = cur.fetchall()
print("Name    ID    Salary")
for row in result:
    print("%s    %d    %d" % (row[0], row[1], row[2]))
myconn.close()

#15. Cập nhật dữ liệu trong bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("UPDATE Employee SET name = 'Đạt' WHERE id = 10001")
myconn.commit()
myconn.close()

# 16. Xóa bản ghi trong bảng
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="PythonDB")
cur = myconn.cursor()
cur.execute("DELETE FROM Employee WHERE id = 10001")
myconn.commit()
myconn.close()

