from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId
import pymongo
import certifi

app = Flask(__name__)

# root
# wV580D9bM3zvewtE
# app
# AttJuVwv0PXDyEJS

client = pymongo.MongoClient("mongodb+srv://app:AttJuVwv0PXDyEJS@clustermongodbdorsetcol.4v2cbuo.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.test

todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
