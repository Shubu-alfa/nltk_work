#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT * from COMPANY where age > 30 and age < 60")
for row in cursor:
   # print ("ID = ", row[0])
   # print ("NAME = ", row[1])
   # print ("ADDRESS = ", row[2])
   # print ("SALARY = ", row[3], "\n")
   print(row)

print ("Operation done successfully");
conn.close()

#similarly delete also