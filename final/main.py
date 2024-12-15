from flask import Flask, redirect, render_template, request, url_for, flash,jsonify
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from fileinput import filename
# from connectDB import *
from flask_login import UserMixin ,LoginManager, login_user, logout_user, login_required, current_user
import hashlib

app = Flask(__name__)
app.secret_key = 'ymfkloose5timesinarows'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    data = getUser(user_id)
    return User(id=data[0], username=data[1], password=data[2])



@app.route('/login',methods=['get','post'])
def login():
    if request.method == 'POST':
        username_f = request.form['username']
        password_f = request.form['password']

        row = getLogin(username_f)
        print(row)
        result = hashlib.md5(password_f.encode())
        enc_password = result.hexdigest()

        if row[1] and row[2] == enc_password:
            user = User(id=row[0], username=row[1], password=row[2])
            login_user(user)
            flash('login success')
            return jsonify({'msg':'YES'})
        else:
            flash('something wrong')
            return jsonify({'msg':'nope'})
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.get('/')
def main():
    return render_template('index.html')

@app.get('/table')
# @login_required
def table():
    # data = get_data()
    # return render_template('table.html',data=data)
    return render_template('table.html')

@app.get('/upload')
def upload():
    return render_template('upload.html')

@app.get('/graph')
def graph():
    # data = get_data()
    # res = []
    # summ = 0
    # score = []
    # for item in data:
    #     res.append(item[1])
    #     score.append(item[2] + item[3] + item[4] + item[5] + item[6])
    # plt.clf()
    # plt.bar(res,score)
    # plt.savefig('static/graph.png')
    return render_template('graph.html')

@app.post('/upload')
def postUploadFile():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)
    for idx, rows in data.iterrows():
        rec = rows['Resource']
        hell = rows['Helltide']
        ih	= rows['IH']
        nmd = rows['Nmd']
        tree = rows['tree']
        pit = rows['pit']

        # insert2Db(rec, hell, ih, nmd, tree, pit)
        data = get_data()

    return render_template('table.html', data=data)

@app.post('/update')
def update():
    # print(request.json)
    id = request.json['id']
    hell = request.json['ht']
    ih = request.json['ih']
    nmd = request.json['nmd']
    tree = request.json['tree']
    pit = request.json['pit']

    status = update_data(hell, ih, nmd, tree, pit ,id)
    # print(hell, ih, nmd, tree, pit ,id)

    if status:
        return jsonify({'msg':'update success!'}),200
    else:
        return jsonify({'msg':'CANT update!'}),400


@app.post('/crate_user')
def new_user():
    username = request.json['username']
    plain_password = request.json['password']
    result = hashlib.md5(plain_password.encode())
    enc_password = result.hexdigest()
    res = add_user(username,enc_password)
    if res:
        return jsonify({'msg':'Add user succuss'})

if __name__ == '__main__':
    app.run(debug=True)
