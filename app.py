from flask import Flask, render_template, request, redirect, url_for
import requests
import LinkBuilder

app = Flask(__name__)

link_builder = LinkBuilder.LinkBuilder()

@app.route('/')
def index():
    r = requests.get(link_builder.get_index_link())
    item_list = r.json()
    return render_template('index.html', item_list = item_list)

@app.route('/complete_item', methods=['POST'])
def move_item_to_done():
    item_id = request.form.get('item_id')
    print(item_id)

    link = link_builder.get_move_to_done_link(item_id)
    print(link)
    requests.put(link)

    return redirect(url_for('index'))

@app.route('/new', methods=['POST'])
def add_item():
    new_item = request.form.get('new_item')
    link = link_builder.get_new_item_link(new_item)
    requests.post(link)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
