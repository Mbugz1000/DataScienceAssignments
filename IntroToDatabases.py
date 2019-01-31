# Introduction to Databases

# Our connection parameters
mysql_driver = 'mysql+pymysql'
mysql_server = '35.243.166.3'
mysql_uname = 'user1'
mysql_pwd ='123456'
mysql_host = 'localhost'
mysql_port = '3306'
mysql_db = 'safaricom_2019'

### Using Standard Python

# import the sql connector parameters
import mysql.connector

db_conn = mysql.connector.connect(
    host = mysql_server,
    user = mysql_uname,
    passwd = mysql_pwd,
    database = mysql_db
)
    
if db_conn:
    print ('Success! Database connected successfully')
else:
    print('Error! Database not connected')        


# Select
def selectFromDB(query):
    mycursor = db_conn.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        print(x)
    
selectFromDB('show tables')

selectFromDB('SELECT * FROM departments')

