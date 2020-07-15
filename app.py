from flask import Flask, render_template, request, redirect, url_for
from trello import Trello

app = Flask(__name__)

@app.route('/')
def index():
    item_list = Trello.fetch_all_items()
    return render_template('index.html', item_list = item_list)

@app.route('/complete_item', methods=['POST'])
def move_item_to_done():
    Trello.complete_item(request.form.get('item_id'))
    return redirect(url_for('index'))

@app.route('/new', methods=['POST'])
def add_item():
    new_item = request.form.get('new_item')
    Trello.add_item(new_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
