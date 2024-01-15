from flask import Flask, request
from models.models import db, Question, insert_question, get_question as getq

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/word', methods=['POST'])
def create_word():
    return 'creating word'

@app.route('/word', methods=['GET'])
def get_word():
    return 'reading word'

@app.route('/word', methods=['PUT'])
def update_word():
    return 'updating word'

@app.route('/word', methods=['DELETE'])
def delete_word():
    return 'deleting word'

@app.route('/question', methods=['POST'])
def create_question():
    data = request.json
    id = data.get('id')
    insert_question(Question())
    return 'creating question'

@app.route('/question/<id>', methods=['GET'])
def get_question(id):
    question = getq(id)
    print(question.id)
    return str(question.id)

@app.route('/question', methods=['PUT'])
def update_question():
    return 'updating question'

@app.route('/question', methods=['DELETE'])
def delete_question():
    return 'deleting question'

if __name__ == '__main__':
    app.run(debug=True)
