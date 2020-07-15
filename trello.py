import requests
from link_builder import LinkBuilder
from item import Item

class Trello:

    link_builder = LinkBuilder()

    @classmethod
    def fetch_all_items(cls):
        r = requests.get(cls.link_builder.get_index_link())
        list_of_dicts = r.json()
        item_list = []
        for dict in list_of_dicts:
            item = Item(dict['id'], dict['name'])
            item_list.append(item)
        return item_list

    @classmethod
    def complete_item(cls, item_id):
        link = cls.link_builder.get_move_to_done_link(item_id)
        requests.put(link)

    @classmethod
    def add_item(cls, new_item):
        link = cls.link_builder.get_new_item_link(new_item)
        requests.post(link)