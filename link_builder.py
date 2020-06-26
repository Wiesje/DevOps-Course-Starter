import secrets

class LinkBuilder:
    baseUrl = "https://api.trello.com"
    listId = "5eeb6d36261b73280b211344"
    yourKey = secrets.TRELLO_API_KEY
    yourToken = secrets.TRELLO_API_TOKEN

    def __init__(self):
        self.index_link = f"{self.baseUrl}/1/lists/{self.listId}/cards?key={self.yourKey}&token={self.yourToken}"
        self.new_item = "" 

    def get_index_link(self):
        return self.index_link

    def get_new_item_link(self, new_item):
        self.new_item = new_item
        self.new_item_link = f"{self.baseUrl}/1/cards?key={self.yourKey}&token={self.yourToken}&idList={self.listId}&name={self.new_item}"
        return self.new_item_link