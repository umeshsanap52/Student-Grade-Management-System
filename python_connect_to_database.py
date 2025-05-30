import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Umesh@123',database='codewithumesh')
my_cursor=conn.cursor()
conn.commit()
conn.close()
print("connection Succesfully Created!")
