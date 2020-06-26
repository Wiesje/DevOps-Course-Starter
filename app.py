from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import secrets
import requests

app = Flask(__name__)
app.config.from_object('flask_config.Config')

baseUrl = "https://api.trello.com"
listId = "5eeb6d36261b73280b211344"
yourKey = secrets.TRELLO_API_KEY
yourToken = secrets.TRELLO_API_TOKEN

@app.route('/')
def index():
    r = requests.get(f"{baseUrl}/1/lists/{listId}/cards?key={yourKey}&token={yourToken}")
    item_list = r.json()
    return render_template('index.html', item_list = item_list)

@app.route('/complete_item', methods=['POST'])
def move_item_to_done():
    item_id = request.form.get('item_id')
    print(item_id)

    return redirect(url_for('index'))

@app.route('/new', methods=['POST'])
def add_item():
    new_item = request.form.get('new_item')
    requests.post(f"{baseUrl}/1/cards?key={yourKey}&token={yourToken}&idList={listId}&name={new_item}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
