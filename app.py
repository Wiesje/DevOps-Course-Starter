from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    item_list = session.get_items()
    return render_template('index.html', item_list = item_list)

@app.route('/', methods=['POST'])
def add_item():
    new_item = request.form.get('new_item')
    session.add_item(new_item)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
