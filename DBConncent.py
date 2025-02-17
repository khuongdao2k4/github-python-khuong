import mysql.connector #khai báo thư viện 
from mysql.connector import Error #khai báo thêm hàm Error để hỗ trợ thông báo lỗi

# Kết nối database
def connect_to_mysql(host="localhost", user="root", passwd="", database='test_db'): #khai báo tên pass của csdl với các tham số trong đó
    """Connect to MySQL database and return connection object"""
    try:
        connection = mysql.connector.connect( # cú pháp kết nối database
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}") #in ra lỗi nếu kết nối không thành công
        return None

# truy vấn cơ sở dữ liệu và dùng for in ra dự liệu trong bảng 
def fetch_users_data(connection): 
    """Fetch and print data from the users table"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users") #try vấn cú pháp sql
        rows = cursor.fetchall()
        print("\nData from users table:")
        for row in rows: #dùng vòng lặp for/in để in ra các phần tử trong bảng 
            print(row)
    except Error as e:
        print(f"Error fetching data: {e}") #in ra lỗi nếu lấy dữ liệu không thành công 
    finally:
        cursor.close() #đóng kết nối sau khi lấy dữ liệu trong bảng 

# Đóng kết nối nếu không còn sử dụng
if __name__ == "__main__": #kiểm tra đã chạy đúng file gốc hay chưa

    conn = connect_to_mysql() #gọi lại hàm kết nối 
    if conn:
        fetch_users_data(conn) # gọi lại hàm lấy dữ liệu  sau khi hàm dc thực hiện xong sẽ đóng kết nối 
        conn.close()
        print("\nMySQL connection is closed") # in ra thống báo đóng kết nối 
