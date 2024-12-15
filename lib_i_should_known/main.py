from flask import Flask, request, render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def mainpage():
    form = MyForm()
    return render_template('index.html',form=form)

@app.route('/user/<username>')
def user_profile(username):
    return f"User : {username}"


if __name__ == '__main__':
    app.run(debug=True)