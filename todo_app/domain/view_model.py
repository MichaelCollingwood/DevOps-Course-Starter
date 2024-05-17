class ViewModel:
    def __init__(self, lists, list_organised_items):
        self._lists = lists
        self._list_organised_items = list_organised_items
 
    @property
    def lists(self):
        return self._lists
    
    @property
    def list_organised_items(self):
        return self._list_organised_items