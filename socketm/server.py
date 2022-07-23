import psycopg2
print(''' 
+--------------------------------- WELCOME ---------------------------------+
''')

conn = psycopg2.connect(dbname='comm',user='postgres',password='2004',host='localhost',port='5432')
curr = conn.cursor()
curr.execute('Delete from talk;')
conn.commit()
curr.execute("Insert into talk values('name','message')")
conn.commit()
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
        continue
    else:
        continue