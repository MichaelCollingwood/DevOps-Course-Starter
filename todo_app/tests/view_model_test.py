from todo_app.domain.item import Item
from todo_app.domain.view_model import ViewModel

items = [
    Item("item-id-1", "Example Name", "list-id-1"),
    Item("item-id-2", "Another Name", "list-id-1"),
    Item("item-id-3", "Doing Item Name", "list-id-2"),
    Item("item-id-4", "Done Item Name", "list-id-3"),
    Item("item-id-5", "Another Done Item Name", "list-id-3"),
]
lists = [
    {
        "id": "list-id-1",
        "name": "To Do"
    },
    {
        "id": "list-id-2",
        "name": "Doing"
    },
    {
        "id": "list-id-3",
        "name": "Done"
    }
]

def test_view_model_list_organised_items_returns_correct_object():
    # Arrange
    view_model = ViewModel(items, lists)

    # Act
    result = view_model.list_organised_items

    # Assert
    assert result == [
        {
            "id": 1,
            "name": "some list",
            "entries": [
                Item("item-id-1", "Example Name"),
                Item("item-id-2", "Another Name"),
            ]
        },
        {
            "id": 2,
            "name": "doing",
            "entries": [
                Item("item-id-3", "Doing Item Name"),
            ]
        },
        {
            "id": 3,
            "name": "done",
            "entries": [
                Item("item-id-4", "Done Item Name"),
                Item("item-id-5", "Another Done Item Name"),
            ]
        },
    ]

def test_view_model_todo_items_returns_correct_items():
    # Arrange
    view_model = ViewModel(items, lists)

    # Act
    result = view_model.todo_items

    # Assert
    assert len(result) == 3
    assert result[0].id == "item-id-1"
    assert result[1].id == "item-id-2"

def test_view_model_doing_items_returns_correct_items():
    # Arrange
    view_model = ViewModel(items, lists)

    # Act
    result = view_model.doing_items

    # Assert
    assert len(result) == 1
    assert result[0].id == "item-id-3"

def test_view_model_done_items_returns_correct_items():
    # Arrange
    view_model = ViewModel(items, lists)

    # Act
    result = view_model.done_items

    # Assert
    assert len(result) == 2
    assert result[0].id == "item-id-4"
    assert result[1].id == "item-id-5"
