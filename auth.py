from flask import Blueprint, render_template, redirect, session, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import pymongo
import certifi
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from user import User
from forms import SignupForm


client = pymongo.MongoClient("mongodb+srv://app:AttJuVwv0PXDyEJS@clustermongodbdorsetcol.4v2cbuo.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.todoApp
users = db.users

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    # Check if the user exists in the database
    user = users.find_one({'email': email})
    if user is None:
        # User not found
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # Check if the password is correct
    if not check_password_hash(user['password'], password):
        # Password incorrect
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    # Login successful, add the user to the session
    userLogged = User(user)
    session['user_id'] = str(userLogged.id)
    login_user(userLogged, remember=remember)

    return redirect(url_for('profile'))

@auth.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html' , form=form)

@auth.route('/signup', methods=['POST'])
def signup_post():
    form = SignupForm()
    if form.validate_on_submit():
        # create a new user with the form data. Hash the password so the plaintext version isn't saved and 
        # get the user id to store in the session
        email = form.email.data
        name = form.name.data
        password = form.password.data
        result = users.insert_one({'email': email, 'name': name, 'password': generate_password_hash(password, method='sha256')})
        user_id = result.inserted_id
        session['user_id'] = str(user_id)
        return redirect(url_for('auth.login'))
    else:
        flash('Please correct the errors and try again.')
        return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
