class Item:
    def __init__(self, id, name, list_id):
        self.id = id
        self.name = name
        self.list_id = list_id

    @classmethod
    def from_stored_item(cls, card):
        return cls(card['_id'], card['title'], card["status"])