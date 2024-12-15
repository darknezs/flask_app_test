from flask import Flask, request, render_template,jsonify
import json
import pandas as pd
from fileinput import filename
from caldate import *
app = Flask(__name__)

@app.get('/')
def upload():
    return render_template('upload.html')



@app.post('/data')
def getData():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)

    bd_data = []

    for idx,rows in data.iterrows():

        bd_data.append({'band':rows['band'], 'name':rows['name'],'birthday':rows['birthday']})

        # band = rows['band']
        # name = rows['name']
        # birthday = rows['birthday']

    list_birthday = nextBd(bd_data)
    print(list_birthday)
    return render_template('table.html', data_list=list_birthday)


@app.get('/api/next_birthday')
def nxt_bd():
    data = pd.read_excel('C:\\kpop_web.xlsx')
    bd_data = []

    for idx,rows in data.iterrows():
        bd_data.append({'band':rows['band'], 'name':rows['name'],'birthday':rows['birthday']})
    list_birthday = nextBd(bd_data)
    return jsonify(list_birthday)



if __name__ == '__main__':
    app.run(debug=True)
