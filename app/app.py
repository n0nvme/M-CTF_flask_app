from flask_pymongo import PyMongo, ObjectId
from flask_login import LoginManager
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'CHANGE_ME'


app.config["MONGO_URI"] = "mongodb://ktftime-db:27017/db"
mongo = PyMongo(app)


# Login conf
login = LoginManager(app)
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'




#register Blueprints
from auth import auth as auth_bp
app.register_blueprint(auth_bp)
from teams import teams as teams_bp
app.register_blueprint(teams_bp)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
