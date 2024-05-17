import json
from os import getenv
from flask import session
import requests

from todo_app.domain.item import Item

# use env var for prefix
cards_url = "https://api.trello.com/1/cards"
board_url = "https://api.trello.com/1/boards/65c4fed365273e251af75aa5"
todo_list_id = "65c4fed42c4a7016163343f9"

headers = {
    "Accept": "application/json"
}
query = {
    'key': getenv('TRELLO_API_KEY'),
    'token': getenv('TRELLO_API_TOKEN')
}

def get_list_organised_items():
    """
    Fetches all saved items for each status in the trello board.

    Returns:
        list: The list of list names with corresponding items.
    """
    items_response = requests.request(
        "GET",
        f"{board_url}/cards",
        headers=headers,
        params=query
    )
    items = [Item.from_trello_card(item) for item in json.loads(items_response.text)]

    lists_response = requests.request(
        "GET",
        f"{board_url}/lists",
        headers=headers,
        params=query
    )
    list_organised_items = [{
        "name": list["name"],
        "entries": [item for item in items if item.list_id == list["id"]]
        } for list in json.loads(lists_response.text) ]

    return list_organised_items

def get_lists():
    """
    Fetch all lists in board

    Returns:
        list: list of lists in the board
    """
    lists_response = requests.request(
        "GET",
        f"{board_url}/lists",
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

    print("response")
    print(response.content)

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
