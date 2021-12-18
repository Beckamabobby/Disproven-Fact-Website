from typing import Dict, List

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
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'startyear': '1972', 'endyear': '1984'}
]

@app.route('/')
def index():
    return render_template('index.html', myths=myths_list)

@app.route('/myths/<graduation_year>')
def myths(graduation_year):
    print(graduation_year)
    # TODO filter by graduation year
    return jsonify(myths_list)

#ooga booga


app.run(debug=True)
