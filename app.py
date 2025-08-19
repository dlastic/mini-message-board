from flask import Flask, render_template

app = Flask(__name__)

messages = [
    {"text": "Hello, World!", "user": "Alice", "added": "2025-08-01"},
    {"text": "Flask is great!", "user": "Bob", "added": "2025-08-02"},
    {"text": "I love coding!", "user": "Charlie", "added": "2025-08-03"},
]


@app.route("/")
def index():
    return render_template("index.html", messages=messages)


@app.route("/new")
def new_message():
    return render_template("new.html")
