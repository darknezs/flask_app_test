import pandas as pd 
from flask import Flask, request, render_template,make_response,jsonify
from fileinput import filename
# from connectDB import *
import matplotlib.pyplot as plt
import numpy as np
import io
app = Flask(__name__)

@app.get('/')
def landingpage():
    return render_template('landing.html')

@app.get('/upload')
def upload():
    return render_template('upload-excel.html')

@app.post('/view')
def view():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)

    for idx,row in data.iterrows():
        name = row['method_name']
        dc_eng = row['desc_eng']
        summarize = row['summarize']
        dc_th = row['desc_th']

        insert(name, dc_eng, summarize, dc_th)

    select()
    return data.to_html()


@app.get('/show')
def show():
    result = select()
    print(result)
    return render_template('showfromdb.html', data=result)

@app.post('/update')
def update():
    data = request.get_json()  # Get the JSON data from the frontend
    print("**** from route /update ****")
    # print(data)
    if data:
        updateDB(data)
        return jsonify({"message": "Data updated successfully!"}), 200  # HTTP status code 200 OK
    else:
        return jsonify({"error": "No data provided"}), 400  # Bad Request

@app.get('/getplot')
def plot_png():
    # Arrays for method ID (x-axis) and priority (y-axis)
    id = []
    priority = []
    # x = np.array([30, 31, 32, 33])  # method id
    # y = np.array([10, 5, 1, 7])     # priority values
    data = select()
    for i in data:
        id.append(i[0])
        priority.append(i[5])
    print(priority)
    x = np.array(id)  # method id
    y = np.array(priority)     # priority values
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='b')  # Plot x vs y
    ax.set_xlabel("Method ID")
    ax.set_ylabel("Priority")
    ax.set_xticks(np.arange(min(x), max(x)+1, 1))  # Set ticks to whole numbers

    # Save the plot to a BytesIO buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Move cursor to the start of the file
    
    # Return the image as a response
    response = make_response(img.read())
    response.headers.set('Content-Type', 'image/png')
    return response

# Route to render HTML template
@app.get('/graph')
def index():
    return render_template('graph.html', plot_url="/getplot")

@app.get('/chart')
def chart():
    return render_template('chart.html')

@app.get('/practiseES6')
def es6():
    return render_template('practiseES6.html')

@app.post('/testtest')
def testtest():
    data = request.get_json()
    print(f'--- *** >>> get data from client: {data}')
    return jsonify({"message": "test 12345",
                    "code" : "777"}), 200


@app.post('/user')
def postUser():
    return jsonify({'user':'admin'}),200




if __name__ == '__main__':
    app.run(debug=True)    