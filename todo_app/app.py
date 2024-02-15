from flask import Flask, redirect, request
from flask import render_template
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=get_items())

@app.route('/createTodo', methods=['POST'])
def createTodo():
    new_title = request.form.get('title')
    add_item(new_title)
    return redirect('/')