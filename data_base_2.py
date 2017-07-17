import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO CELUSION (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Praveen', 32, 'India', 200000.00 )")

conn.execute("INSERT INTO CELUSION (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Shubham', 21, 'Texas', 15000.00 )")

conn.execute("INSERT INTO CELUSION (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Alia', 21, 'Borivali', 20000.00 )")

conn.execute("INSERT INTO CELUSION (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Rohit', 25, 'Dharavi ', 65000.00 )")

conn.execute("INSERT INTO CELUSION (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (5, 'Priya', 55, 'Thane ', 87000.00 )")

conn.execute("INSERT INTO CELUSION (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (6, 'Preeti', 76, 'Bandra ', 115000.00 )")
conn.commit()
print("Records created successfully")
conn.close()
