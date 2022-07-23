# import psycopg2

# conn = psycopg2.connect(dbname='comm',user='postgres',password='2004',host='localhost',port='5432')
# def insertdata():
#     while True:
#         texct = input('enter text to insert :')
#         curr = conn.cursor()
#         curr.execute("Insert into talk values('random','{0}');".format(texct))
#         conn.commit()
# insertdata()

import psycopg2
import time 

conn = psycopg2.connect(dbname='comm',user='postgres',password='2004',host='localhost',port='5432')
curr = conn.cursor()
curr.execute('Select * from talk;')
data = curr.fetchall()
conn.commit()
emp_list = []
for x in range(0,len(data)):
    print("{0} : {1}".format(data[x][0],data[x][1]))
    emp_list.append(data[x])
while True:
    curr.execute('Select * from talk;')
    data = curr.fetchall()
    conn.commit()
    if data != emp_list:
        emp_list.append(data[-1])
        print("{0} : {1}".format(data[-1][0],data[-1][1]))
        time.sleep(0.5)
        continue
    else:
        time.sleep(0.5)
        continue