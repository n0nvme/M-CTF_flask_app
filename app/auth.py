from flask import render_template, url_for, request, flash, redirect, Blueprint
from flask import request
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from user import User
from app import mongo
from forms import LoginForm, RegistrationForm
from flask_pymongo import ObjectId
ALLOWED_KEYS = ['username','is_admin','first_name','last_name','email','country','password']
auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = LoginForm(request.form)
        if form.validate():
            user = mongo.db.users.find_one({"username": form.username.data})
            if user and check_password_hash(user.get('password', None), form.password.data):
                user_obj = User(_id=user.get('_id'), username=user.get('username'))
                login_user(user_obj)

                return redirect(url_for('home'))
            else:
                flash("Invalid username or password")

    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        if form.validate():
            if mongo.db.users.find_one({'username': form.username.data}) is None:
                id = mongo.db.users.insert_one({"username": form.username.data,
                                                "password": generate_password_hash(form.password.data),
                                                'is_admin': False}).inserted_id
                login_user(User(_id=str(id), username=form.username.data))
            else:
                flash('User already exist!')
        else:
            flash("Login or password is not sent!")
    return render_template('register.html')


@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = request.form
    user_data = mongo.db.users.find_one({'_id':ObjectId(current_user.id)})

    for key,value in  form.items():
        if key in ALLOWED_KEYS:
            if key == 'password':
                user_data[key] = generate_password_hash(value)



            user_data[key] = value
        print(value)
    mongo.db.users.update({'_id':ObjectId(current_user.id)}, { "$set":  user_data })
    return render_template('profile.html')
