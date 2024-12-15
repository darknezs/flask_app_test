from flask import Flask, render_template, request,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
bootstrap = Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อ",validators=[DataRequired()])
    gender = RadioField('เพศ',choices=[('male','ชาย'),('female','หญิง'),('lgbtq','อื่นๆ')], validators=[Optional()])
    skill = SelectField('ความสามารถ',choices=[('พูดภาษาอังกฤษ','พูดภาษาอังกฤษ'),('เขียนเกม','เขียนเกม'),('ร้องเพลง','ร้องเพลง')])
    address = TextAreaField('ที่อยู่ของคุณ')
    isAccept = BooleanField("ยอมรับเงื่อนไข")
    submit = SubmitField("บันทึก")

@app.route('/',methods=['GET','POST'])
def index():

    form = MyForm()
    session['name'] = "" 
    session['isAccept'] = ""
    session['gender'] = ""
    session['skill'] = ""
    session['address'] = ""
    if form.validate_on_submit():
        flash('SAVE!!!')
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        session['address'] = form.address.data

        clsformdata(form)

    return render_template('index.html', form=form)

def clsformdata(form):
    form.name.data = ""
    form.isAccept.data = ""
    form.gender.data = ""
    form.skill.data = ""
    form.address.data  = ""
# @app.get('/admin')
# def admin():
#     name = 'somebody'
#     return render_template('admin.html', user=name)

# @app.get('/about')
# def about():
#     return render_template('about.html')

# @app.post('/submit')
# def form_submit():
#     name = request.form.get('fname')
#     desc = request.form.get('desc')
#     return render_template('ty.html',data={'name':name, 'desc':desc})

# @app.get('/user/<name>')
# def user(name):
#     return '<h1>สวัสดี : {} <h1/>'.format(name)

@app.get('/secret')
def testForm():
    return render_template('testform.html')

@app.get('/testform')
def abc():
    id = request.args.get('id')
    print(id)
    return render_template('testform.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)