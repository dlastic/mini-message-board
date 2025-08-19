from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = [
    {"text": "Hello, World!", "user": "Alice", "added": "2025-08-01"},
    {"text": "Flask is great!", "user": "Bob", "added": "2025-08-02"},
    {"text": "I love coding!", "user": "Charlie", "added": "2025-08-03"},
]


@app.route("/")
def index():
    return render_template("index.html", messages=messages)


@app.route("/new", methods=["GET", "POST"])
def new_message():
    if request.method == "POST":
        text = request.form["text"]
        user = request.form["user"]
        added = datetime.now().strftime("%Y-%m-%d")
        messages.append({"text": text, "user": user, "added": added})
        return redirect(url_for("index"))

    return render_template("form.html")


@app.route("/messages/<int:message_id>")
def message_detail(message_id):
    message = messages[message_id]
    return render_template("message.html", message=message)
