from typing import Dict, List
from random import choice

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myths.db'
db = SQLAlchemy(app)


class Myth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String)


db.create_all()

myths_list: List[Dict[str, str]] = [
    {'title': 'Birds are real', 'synopsis': 'Government literally 1984',
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'startyear': '1970', 'endyear': '1990'},
    {'title': 'Birds are fake', 'synopsis': 'Are you stupid',
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'startyear': '1972', 'endyear': '1983'},
    {'title': 'Birds are cringe', 'synopsis': 'Are you sussy',
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'startyear': '1979', 'endyear': '1994'},
]

words: List[str] = 'defenestration amongus red chair fly'.split()
messages: List[str] = [
    'pay your taxes',
    'i hate the irs'
]

@app.route('/')
def index():
    return render_template('index.html', myths=myths_list, years=range(1970, 1995))

@app.route('/simple')
def simple():
    return render_template('simple.html', word=choice(words))

@app.route('/chat_messages')
def chat_messages():
    return render_template('chat_messages.html', messages=messages)

@app.route('/myths/<graduation_year>')
def myths(graduation_year):
    print(graduation_year)
    selected_myths = [myth for myth in myths_list if myth['startyear'] <= graduation_year <= myth['endyear']]
    return jsonify(selected_myths)

#ooga booga


app.run(debug=True)
