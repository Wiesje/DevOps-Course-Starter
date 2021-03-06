from flask import Flask, render_template, request, redirect, url_for
import trello_items as trello
from view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object('app_config.Config')

    @app.route('/')
    def index():
        items = trello.get_items()
        return render_template('index.html', model=ViewModel(items))

    @app.route('/items/new', methods=['POST'])
    def add_item():
        name = request.form['name']
        trello.add_item(name)
        return redirect(url_for('index'))

    @app.route('/items/<id>/start')
    def start_item(id):
        trello.start_item(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/complete')
    def complete_item(id):
        trello.complete_item(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/uncomplete')
    def uncomplete_item(id):
        trello.uncomplete_item(id)
        return redirect(url_for('index'))

    return app


if __name__ == '__main__':
    create_app().run()
