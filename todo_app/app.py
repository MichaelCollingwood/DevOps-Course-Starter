from flask import Flask, redirect, request
from flask import render_template
from todo_app.data.trello_items import get_items, get_lists, add_item, update_item_status

from todo_app.domain.view_model import ViewModel
from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = get_items()
        lists = get_lists()
        view_model = ViewModel(items, lists)
        return render_template('index.html', view_model=view_model)

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
    
    return app
