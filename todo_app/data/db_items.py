from todo_app.domain.item import Item

class Repository:
    def __init__(self, db):
        self.db = db

    def get_items(self):
        """
        Fetch all items from MongoDB.

        Returns:
            list: A list of items.
        """
        collection = self.db["items"]
        items = collection.find()
        return [Item.from_stored_item(item) for item in items]

    def get_lists(self):
        """
        Fetch all unique statuses from the items.

        Returns:
            list: The list of all statuses.
        """
        collection = self.db["items"]
        statuses = collection.distinct("status")
        return [{"id": status, "name": status} for status in statuses]

    def update_item_status(self, item_id, new_status):
        """
        Update the status of an item in MongoDB.

        Args:
            item_id: The ID of the item.
            new_status: The new status for the item.

        Returns:
            dict: The updated item.
        """
        collection = self.db["items"]
        collection.update_one(
            {"_id": item_id}, 
            {"$set": {"status": new_status}}
        )

    def add_item(self, title, status="To Do"):
        """
        Add a new item with the specified title to MongoDB.

        Args:
            title: The title of the item.
            status: The initial status of the item.

        Returns:
            dict: The saved item.
        """
        collection = self.db["items"]
        new_item = {"title": title, "status": status}
        collection.insert_one(new_item)
