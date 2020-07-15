from flask import Flask, render_template, request, redirect, url_for
import trello

app = Flask(__name__)

@app.route('/')
def index():
    item_list = trello.fetch_all_items()
    return render_template('index.html', item_list = item_list)

@app.route('/complete_item', methods=['POST'])
def move_item_to_done():
    trello.complete_item(request.form.get('item_id'))
    return redirect(url_for('index'))

@app.route('/new', methods=['POST'])
def add_item():
    trello.add_item(request.form.get('new_item'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
