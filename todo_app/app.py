from flask import Flask, redirect, request
from flask import render_template
import pymongo
from os import getenv

from todo_app.data.db_items import Repository
from todo_app.domain.view_model import ViewModel
from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    client = pymongo.MongoClient(getenv("MONGO_CONNECTION_STRING"))
    app.db = client[getenv("MONGO_DB_NAME")]
    respository = Repository(app.db)

    @app.route('/')
    def index():
        items = respository.get_items()
        lists = respository.get_lists()
        view_model = ViewModel(items, lists)
        return render_template('index.html', view_model=view_model)

    @app.route('/createTodo', methods=['POST'])
    def create_todo():
        new_title = request.form.get('title')
        respository.add_item(new_title)
        return redirect('/')

    @app.route('/updateStatus', methods=['POST'])
    def update_status():
        item_id = request.form.get('itemId')
        list_id = request.form.get('listId')
        respository.update_item_status(item_id, list_id)
        return redirect('/')
    
    return app
