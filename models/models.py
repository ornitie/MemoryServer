from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)