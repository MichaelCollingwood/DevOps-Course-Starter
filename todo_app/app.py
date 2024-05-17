from flask import Flask, redirect, request
from flask import render_template
from todo_app.data.trello_items import get_list_organised_items, get_lists, add_item, update_item_status

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', list_organised_items=get_list_organised_items(), lists=get_lists())

@app.route('/createTodo', methods=['POST'])
def create_todo():
    new_title = request.form.get('title')
    add_item(new_title)
    return redirect('/')

@app.route('/updateStatus', methods=['POST'])
def update_status():
    item_id = request.form.get('itemId')
    list_id = request.form.get('listId')
    update_item_status(item_id, list_id)
    return redirect('/')
