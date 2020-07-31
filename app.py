from flask import Flask, render_template, request, redirect, url_for
from trello import Trello
from view_model import ViewModel

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        items = Trello.fetch_all_items()
        return render_template('index.html', view_model=ViewModel(items))

    @app.route('/complete_item', methods=['POST'])
    def move_item_to_done():
        Trello.complete_item(request.form.get('item_id'))
        return redirect(url_for('index'))

    @app.route('/new', methods=['POST'])
    def add_item():
        new_item = request.form.get('new_item')
        Trello.add_item(new_item)
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    create_app.run()
