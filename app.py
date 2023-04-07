from flask import Flask, Blueprint, render_template, request, url_for, redirect, session, flash
from bson.objectid import ObjectId
import pymongo
import certifi
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.secret_key = '246e7d90e59b61d3d69aea7d966e0a76'

# blueprint for auth routes in the app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    user = users.find_one({'_id': ObjectId(user_id)})
    if user is None:
        return None
    return User(user['_id'], user['email'], user['name'])

# root
# wV580D9bM3zvewtE
# app
# AttJuVwv0PXDyEJS

client = pymongo.MongoClient("mongodb+srv://app:AttJuVwv0PXDyEJS@clustermongodbdorsetcol.4v2cbuo.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.todoApp

users = db.users
todos = db.todos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todo', methods=('GET', 'POST'))
def todo():
    if request.method=='POST':
        user_id = session['user_id']
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'user_id': user_id,'content': content, 'degree': degree})
        return redirect(url_for('todo'))
    all_todos = todos.find({'user_id': session['user_id']})
    return render_template('todos.html', todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('todo'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, total_todos=todos.count_documents({'user_id': session['user_id']}))

if __name__ == '__main__':
    app.run()
