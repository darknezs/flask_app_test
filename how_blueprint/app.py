from flask import Flask
from main.routes import main
from auth.routes import auth

app = Flask(__name__)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)