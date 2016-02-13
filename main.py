from flask import Flask, request, redirect, render_template, url_for
import db
from models import Player

app = Flask(__name__)
db.database_connect()

@app.route('/')
def index():
    players = Player.find()
    return render_template('index.html', players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    name = request.form.get('name')
    surname = request.form.get('surname')
    Player.create({'name': name, 'surname': surname})
    return redirect(url_for('index'))

if __name__ == '__main__':
    print "Running!"
    app.run(debug=True)