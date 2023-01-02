from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)

def insert_question(question: Question):
    db.session.add(question)
    db.session.commit()

def get_question(id):
    question = Question.query.filter(Question.id == id).first()
    return question