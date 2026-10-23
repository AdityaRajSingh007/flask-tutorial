from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello World'

@app.route("/search")
def search():
    name = request.args.get("name", "guest")
    course = request.args.get("course", "unknown")
    return f'Hello, {name} is in {course}'


if __name__ == '__main__':
    app.run(debug=True)