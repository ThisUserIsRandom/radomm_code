from flask import Flask, render_template, request
import psycopg2

# managing database
class database_connection:
    class try_connection:
        conn = psycopg2.connect(dbname='expense',
                                user='postgres',
                                password=2004,
                                host='127.0.0.1',
                                port='5432')
        def function_try_connect():
            try:
                database_connection.try_connection.conn
                return 1
            except:
                return 0
    class do_something(try_connection):
        def insert_data(query):
            connet = database_connection.try_connection.conn
            curr = connet.cursor()
            curr.execute(query)
            connet.commit()
            return "submitted"
        def fetch_data(query):
            connet = database_connection.try_connection.conn
            curr = connet.cursor()
            curr.execute(query)
            dataget = curr.fetchall()
            connet.commit()
            return dataget
# managing web app

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/subm',methods=['POST'])
def postreq_page():
    founddata = database_connection.do_something.fetch_data("Select * from expense;")
    date = request.form['date']
    expense = request.form['expense']
    amount = request.form['amount']
    category = request.form['category']
    query = '''Insert into expense values({4},'{0}','{1}',{2},'{3}');'''.format(date,expense,amount,category,len(founddata)+1)
    submmit = database_connection.do_something.insert_data(query)
    print(submmit)
    return "<p> submitted </p>"

@app.route('/db')
def data_check():
    data_checked = database_connection.try_connection.function_try_connect()
    return render_template('databasecheck.html',databool=data_checked)

@app.route('/fetch')
def fetched_data():
    founddata = database_connection.do_something.fetch_data("Select * from expense;")
    lenfounddata = len(founddata)
    query = '''Select sum(amount) from expense;'''
    total_karch = database_connection.do_something.fetch_data(query)
    return render_template('fetched.html',data=lenfounddata,founddata=founddata,karcha=total_karch[0][0])
    
if __name__ == '__main__':
    app.run('127.0.0.1','5050',debug=True)