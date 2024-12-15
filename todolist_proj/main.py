from flask import Flask, request,render_template
from connectDB import *

app = Flask(__name__)



@app.get('/')
def index():
    result = get_todolist()
    print(result)
    return render_template('index.html', data=result)



if __name__ == '__main__':
    app.run(debug=True)