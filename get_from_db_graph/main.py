from flask import Flask, render_template,redirect
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mysql.connector
import time
import random
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv() 

host = os.getenv("host")

mydb = mysql.connector.connect(
    host = os.getenv("host"),
    user = os.getenv("user"),
    password = os.getenv("password"),
    database = os.getenv("database")
)

mycursor = mydb.cursor()

# Cache control for static files
# @app.after_request
# def add_header(response):
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
#     return response

@app.get('/')
def main():
    list_name = []
    list_prio = []
    data = get_data()
    for x in data:
        list_name.append(x[0])
        list_prio.append(x[1])
    plt.clf()
    plt.bar(list_name,list_prio)
    plt.title('PRIORITY OF method')
    plt.savefig('static/priority.png')
    print('save new file')
    return render_template('index.html')

@app.get('/update')
def update():
    n = random.randint(5,25)
    sql = "update data set priority = %s where method_name = %s"
    val =(n,'get_item_base_info')
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect('/')

def get_data():
    print('from get_data')
    sql = 'select method_name,priority from data'
    mycursor.execute(sql)
    res = mycursor.fetchall()
    mydb.commit()
    print(res)
    return res



if __name__ == '__main__':
    app.run(debug=True)