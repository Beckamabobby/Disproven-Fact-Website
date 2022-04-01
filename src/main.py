from typing import Dict, List

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myths.db'
db = SQLAlchemy(app)


user_myth = db.Table('user_myth',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                     db.Column('myth_id', db.Integer, db.ForeignKey('myth.id'), primary_key=True)
                     )

class Myth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    synopsis = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    startyear = db.Column(db.Integer, nullable=False)
    endyear = db.Column(db.Integer, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)

# class UserMyth(db.Model):
#     id      = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     myth_id = db.Column(db.Integer, db.ForeignKey('page.id'), primary_key=True)

db.create_all()

myths = Myth.query.all()
myths_list: List[Dict[str, str | int]] = [{
    'title': myth.title,
    'synopsis': myth.synopsis,
    'url': myth.url,
    'startyear': int(myth.startyear),
    'endyear': int(myth.endyear)} for myth in myths]

@app.route('/')
def index():
    return render_template('index.html', myths=myths_list, years=range(1970, 1995))

@app.route('/myths/<int:graduation_year>')
def myths(graduation_year: int):
    print(graduation_year)
    selected_myths = [myth for myth in myths_list if myth['startyear'] <= graduation_year <= myth['endyear']]
    return jsonify(selected_myths)

app.run(debug=True)
