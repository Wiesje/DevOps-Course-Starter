import secrets

class LinkBuilder:
    baseUrl = "https://api.trello.com"
    yourKey = secrets.TRELLO_API_KEY
    yourToken = secrets.TRELLO_API_TOKEN

    def __init__(self):
        self.to_do_list = "5eeb6d36261b73280b211344"
        self.done_list = "5eec7a03ebdf3b6d3eb2158e"
        self.index_link = f"{self.baseUrl}/1/lists/{self.to_do_list}/cards?key={self.yourKey}&token={self.yourToken}"
        

    def get_index_link(self):
        return self.index_link

    def get_new_item_link(self, new_item):
        new_item_link = f"{self.baseUrl}/1/cards?key={self.yourKey}&token={self.yourToken}&idList={self.to_do_list}&name={new_item}"
        return new_item_link

    def get_move_to_done_link(self, card_id):
        move_to_done_link = f"{self.baseUrl}/1/cards/{card_id}?key={self.yourKey}&token={self.yourToken}&idList={self.done_list}"
        return move_to_done_link