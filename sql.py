import sqlite3

##connect to sqlite database
conn = sqlite3.connect('student.db')

##create a cursor object using the cursor() method to insert record, create table, retrieve
cursor = conn.cursor()

##create a table
table_info="""
CREATE TABLE student(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

##insert some records
cursor.execute("INSERT INTO student VALUES ('Rohan', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO student VALUES ('Sohan', 'Data Science', 'B', 80)")
cursor.execute("INSERT INTO student VALUES ('Rahul', 'Data Science', 'A', 70)")
cursor.execute("INSERT INTO student VALUES ('Sumit', 'Devops', 'B', 85)")
cursor.execute("INSERT INTO student VALUES ('Raj', 'Devops', 'A', 60)")
cursor.execute("INSERT INTO student VALUES ('Rahul', 'Devops', 'B', 75)")
##display the records
print("the inserted records are:")

data=cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

    ##close the connection
    conn.commit()
    conn.close()



