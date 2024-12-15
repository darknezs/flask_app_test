from flask import Flask, render_template, request,redirect,jsonify
from fileinput import filename
import pandas as pd
import time
# from connectDB import *
app = Flask(__name__)

@app.get('/')
def mainPage():
    print('from mainPage')
    data = getAll()
    return render_template('index.html',data=data)

@app.get('/upload')
def showUploadForm():
    return render_template('upload.html')

@app.post('/upload')
def getExcelData():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)

    for idx, rows in data.iterrows():
        band = rows['band']
        name = rows['name']
        bd   = rows['birthday']

        #insert
        # insert_2_db(band, name, bd)
    data = getAll()
    # return data.to_html()
    return render_template('index.html',data=data)

@app.post('/formAdd')
def formAdd():

    name = request.form['name']
    band = request.form['band']
    bd = request.form['bd']

    th_year_number = int(bd[:4])+int(543)
    ad_year = bd[:4]
    new_bd = bd.replace(ad_year,str(th_year_number))

    # print(new_bd)

    insert_2_db(band, name, new_bd)

    # data = getAll()
    # return render_template('index.html',data=data)
    return redirect('/')

@app.post('/delete/<id>')
def delete_from_table(id):

    delete_data(id)

    return jsonify({'status':'success'})


@app.post('/update')
def update_from_table():

    data = request.json
    id = data['id']
    name = data['name']
    band = data['band']
    bd = data['bd']
    if "/" in bd:
        bd = dateConverte(bd)


    update(id,name,band,bd)
    return jsonify({'status':'success'})


@app.get('/sleep')
def sleep():

    time.sleep(10)
    return jsonify({'message' : 'wake up to the ground'})


def dateConverte(date):
    d = date[0:2]
    m = date[3:5]
    y = date[-4:]
    newdate = y+"-"+m+"-"+d
    return newdate
    # type :  <class 'str'> value:25/02/2546 err
    # type :  <class 'str'> value:2546-02-25 yes


if __name__ == '__main__':
    app.run(debug=True)