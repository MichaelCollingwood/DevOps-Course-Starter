import json
from os import getenv
import os
import requests

from todo_app.domain.item import Item

# use env var for prefix
cards_url = "https://api.trello.com/1/cards"
todo_list_id = "65c4fed42c4a7016163343f9"

headers = {
    "Accept": "application/json"
}
query = {
    'key': getenv('TRELLO_API_KEY'),
    'token': getenv('TRELLO_API_TOKEN')
}

def get_items():
    """
    Fetches all saved items in the trello board.

    Returns:
        list: The list of all items.
    """
    board_id = os.environ.get('TRELLO_BOARD_ID')
    items_response = requests.request(
        "GET",
        f"https://api.trello.com/1/boards/{board_id}/cards",
        headers=headers,
        params=query
    )
    
    return [Item.from_trello_card(item) for item in json.loads(items_response.text)]

def get_lists():
    """ 
    Fetches all saved lists in the trello board.

    Returns:
        list: The list of all lists.
    """
    board_id = os.environ.get('TRELLO_BOARD_ID')
    lists_response = requests.request(
        "GET",
        f"https://api.trello.com/1/boards/{board_id}/lists",
        headers=headers,
        params=query
    )

    return json.loads(lists_response.text)

def update_item_status(item_id, list_id):
    """
    
    """
    update_item_status_query = {}
    update_item_status_query.update(query)
    update_item_status_query.update({
        "idList": list_id
        })

    response = requests.request(
        "PUT",
        f'{cards_url}/{item_id}',
        headers=headers,
        params=update_item_status_query
    )

    return response

def add_item(title):
    """
    Adds a new item with the specified title to trello.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    add_item_query = {}
    add_item_query.update(query)
    add_item_query.update({
        "name": title,
        "idList": todo_list_id
        })

    response = requests.request(
        "POST",
        cards_url,
        headers=headers,
        params=add_item_query
    )

    return response
