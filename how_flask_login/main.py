from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'itsnotasecretatall'

# flask-login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirect to 'login' if not authenticated

#dummy user database
users = {"testuser":{"password":"1234"}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

#user loader (require flask-login)
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes
@app.get('/')
def home():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            login_user(User(username))
            flash('logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password!", "danger")
        
    return render_template('login.html')


@app.get('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',name=current_user.id)

@app.get('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.get('/sss')
@login_required
def sss():
    return 'sss'

if __name__ == '__main__':
    app.run(debug=True)