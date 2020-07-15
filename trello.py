import requests
import LinkBuilder
import Item

link_builder = LinkBuilder.LinkBuilder()

def fetch_all_items():
    r = requests.get(link_builder.get_index_link())
    list_of_dicts = r.json()
    item_list = []
    for dict in list_of_dicts:
        item = Item.Item(dict['id'], dict['name'])
        item_list.append(item)
    return item_list

def complete_item(item_id):
    link = link_builder.get_move_to_done_link(item_id)
    requests.put(link)

def add_item(new_item):
    link = link_builder.get_new_item_link(new_item)
    requests.post(link)