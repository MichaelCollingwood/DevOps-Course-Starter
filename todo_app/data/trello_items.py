import json
from os import getenv
from flask import session
import requests

# use env var for prefix
cardsUrl = "https://api.trello.com/1/cards"
boardUrl = "https://api.trello.com/1/boards/65c4fed365273e251af75aa5"
listIds = {
    "todo": "65c4fed42c4a7016163343f9",
    "doing": "65c4fed365273e251af75aa5",
    "done": "65c4fed475af8113b502c830"
}

headers = {
    "Accept": "application/json"
}
query = {
    'key': getenv('TRELLO_API_KEY'),
    'token': getenv('TRELLO_API_TOKEN')
}

def get_items():
    """
    Fetches all saved items from the trello board.

    Returns:
        list: The list of items.
    """
    items_response = requests.request(
        "GET",
        f"{boardUrl}/cards",
        headers=headers,
        params=query
    )
    items = json.loads(items_response.text)

    lists_response = requests.request(
        "GET",
        f"{boardUrl}/lists",
        headers=headers,
        params=query
    )
    lists = json.loads(lists_response.text)
    list_names = { list['id']: list['name'] for list in lists }

    return [{
        "id": item['id'],
        "status": list_names[item['idList']],
        "title": item['name'],
    } for item in items]

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
        "idList": listIds["todo"]
        })

    items_response = requests.request(
        "POST",
        cardsUrl,
        headers=headers,
        params=add_item_query
    )

    return items_response
