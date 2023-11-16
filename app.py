from flask import Flask
from models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://memory_server'

db = (app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/word', methods=['POST'])
def create_word():
    return 'creating word'

@app.route('/word', methods=['GET'])
def create_word():
    return 'reading word'

@app.route('/word', methods=['PUT'])
def create_word():
    return 'updating word'

@app.route('/word', methods=['DELETE'])
def create_word():
    return 'deleting word'

if __name__ == '__main__':
    app.run(debug=True)
