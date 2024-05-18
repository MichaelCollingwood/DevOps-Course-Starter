from todo_app.domain.item import Item


class ViewModel:
    def __init__(self, items, lists):
        self._list_organised_items = [{
            "id": list["id"],
            "name": list["name"],
            "entries": [item for item in items if item.list_id == list["id"]]
        } for list in lists]
    
    @property
    def list_organised_items(self):
        return self._list_organised_items

    # Below properties not needed for actual functionality, just for exercise 3
    @property
    def todo_items(self):
        for list_and_items in self._list_organised_items:
            if list_and_items.name == "To Do":
                return list_and_items.entries
    
    @property
    def doing_items(self):
        for list_and_items in self._list_organised_items:
            if list_and_items.name == "Doing":
                return list_and_items.entries
            
    @property
    def done_items(self):
        for list_and_items in self._list_organised_items:
            if list_and_items.name == "Done":
                return list_and_items.entries
