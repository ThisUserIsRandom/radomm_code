import psycopg2
from tkinter import *

#managing database 

class data_connection:
    class check_connection:
        conn = psycopg2.connect(dbname='comm',user='postgres',password=2004,host='127.0.0.1',port=5432)
        def try_connection():
            try:
                data_connection.check_connection.conn
                return 1
            except:
                return 0
    class do_smth:
        def insert_data(name,message):
            curr = data_connection.check_connection.conn.cursor()
            curr.execute("Insert into talk values('{0}','{1}')".format(name,message))
            data_connection.check_connection.conn.commit()

#handeling gui
root = Tk()
label1 = Label(root,text='Enter name:')
label1.grid(row=0,column=0)
label2 = Label(root,text='Enter message:')
label2.grid(row=1,column=0)
entry1 = Entry(root)
entry1.grid(row=0,column=1,padx=10)
entry2 = Entry(root)
entry2.grid(row=1,column=1,padx=10)

#handling button functions
def send_data():
    global entry1
    global entry2
    data_entry1 = entry1.get()
    data_entry2 = entry2.get()
    entry2.delete(0,END)
    data_connection.do_smth.insert_data(data_entry1,data_entry2)
Button1 = Button(root,text="send",command=send_data)
Button1.grid(row=2,column=1,pady=10)

root.mainloop()


