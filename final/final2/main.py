from flask import Flask, render_template,request,redirect,jsonify
from fileinput import filename
import pandas as pd
import mysql.connector
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host = "192.168.0.109",
    user = "",
    password = "",
    database = ""
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('upload.html')

@app.post('/upload')
def upload():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)

    info = getData()
    return render_template('table.html',data=info)

@app.get('/table')
def table():
    data = getData()
    # inssert()
    # uppdate()
    # dellete()
    return render_template('table.html',data=data)

@app.get('/graph')
def graph():
    text = ['a','b','c']
    nums = [1,2,3]
    plt.clf()
    plt.bar(text,nums)
    plt.savefig('static\output.png')
    return render_template('graph.html')

@app.get('/testapi')
def testapi():
    return render_template('index.html')

@app.post('/api/v1')
def api_1():
    if 'name' not in request.json or 'age' not in request.json:
        return jsonify({'msg':'missing name or age'}),400
    name = request.json['name']
    age = request.json['age']
    msg = f' hello {name} {age} years'
    return jsonify({'msg' : msg}),200
###### CRUD ######
def getData():
    sql = "select * from data"
    mycursor.execute(sql)
    data =  mycursor.fetchall()
    return data

def inssert():
    sql = 'insert into data(method_name,priority) values(%s,%s)'
    val = ('eiei',15)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f'{mycursor.rowcount} row add')

def uppdate():
    sql = 'update data set method_name = %s where id = %s'
    val = ('eieizzz',34)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f'{mycursor.rowcount} row update')

def dellete():
    sql = 'delete from  data where id = %s'
    val = (34,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f'{mycursor.rowcount} row delete')
if __name__ == '__main__':
    app.run(debug=True)
