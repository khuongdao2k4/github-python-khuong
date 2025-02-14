import mysql.connector
from mysql.connector import Error

def connect_to_mysql(host="localhost", user="root", passwd="", database='test_db'):
    """Connect to MySQL database and return connection object"""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def fetch_users_data(connection):
    """Fetch and print data from the users table"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\nData from users table:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching data: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":

    conn = connect_to_mysql()
    if conn:
        fetch_users_data(conn)
        conn.close()
        print("\nMySQL connection is closed")
