from datetime import datetime
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite3'

db = SQLAlchemy(app)

# user table in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# adding data to the database
@app.route('/<username>/<location>')
def index(username, location):
    new_user = User(username=username, location=location)
    db.session.add(new_user)
    db.session.commit()
    
    return '<h1>User Added Successfully!'