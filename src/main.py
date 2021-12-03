from typing import Dict, List

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myths.db'
db = SQLAlchemy(app)


class Myth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String)


db.create_all()


@app.route('/')
def index():
    myths: List[Dict[str, str]] = [
        {'title': 'Birds are real', 'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'},
        {'title': 'Birds are fake', 'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}
    ]
    return render_template('index.html', myths=myths)


app.run(debug=True)
