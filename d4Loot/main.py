from flask import Flask, render_template, request,jsonify,redirect
import pandas as pd
from fileinput import filename
from connectDB import *
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.post('/upload')
def upload():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)

    for idx, rows in data.iterrows():
        helltide = (rows['Helltide'])
        ih = (rows['i'])
        lboss = (rows['Ladder Boss'])
        wboss = (rows['World Boss'])
        lgn = (rows['Legion'])
        nmd = (rows['Nmd'])
        tree = (rows['tree'])
        dark = (rows['Dark Citadel'])
        under = (rows['Undercity'])
        pit = (rows['pit'])

        ##upload data to db
        #insert2db(helltide,ih,lboss,wboss,lgn,nmd,tree,dark,under,pit)


    data = getAll()
    createGraph()
    return render_template('dashboard.html',data=data,)


@app.get('/upload')
def getTable():
    data = getAll()
    createGraph()
    return render_template('dashboard.html',data=data)


def createGraph():
    place = ['helltide','IH','L boss']
    score = [23,25,22]

    plt.bar(place,score)

    # plt.xlabel('แกน x')
    # plt.ylabel('แกน y')
    plt.title('SCORE WHERE TO FARM')
    plt.savefig('static/output999.png')


#Catch-all route for undefined routes
@app.errorhandler(404)
def route_not_found(e):
    # Redirect or render specific message
    return redirect('/ushallnotpass')

# Route /ushallnotpass
@app.route('/ushallnotpass', methods=['GET'])
def no_access():
    return jsonify({'message': 'You shall not pass!'})

if __name__ == '__main__':
    app.run(debug=True)