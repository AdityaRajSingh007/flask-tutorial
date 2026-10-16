from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello Aditya'

@app.route("/student/<uuid:user_id>")
def user(user_id):
    return str(user_id)

@app.route("/price/<float:amount>")
def price(amount):
    return f'Price, {amount}'

@app.route("/username/<string:name>")
def username(name):
    return f'Username: {name}'

@app.route("/file/<path:file_path>")
def file(file_path):
    return f'File path: {file_path}'

if __name__ == '__main__':
    app.run(debug=True)