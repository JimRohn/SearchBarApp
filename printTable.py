import sqlite3

##connect to sqlite database
conn = sqlite3.connect('student.db')

##create a cursor object using the cursor() method to retrieve records
cursor = conn.cursor()

##display the records
print("The records in the student table are:")

data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

##close the connection
conn.close()
