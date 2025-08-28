from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from db.queries import (
    add_message,
    delete_message_from_db,
    get_message_by_id,
    get_messages,
)

app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address, app=app, default_limits=["200 per day", "50 per hour"]
)


@app.route("/")
def index():
    messages = get_messages()
    return render_template("index.html", messages=messages)


@app.route("/new", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def new_message():
    if request.method == "POST":
        text = request.form["text"]
        username = request.form["username"]
        added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_message(text, username, added)
        return redirect(url_for("index"))

    return render_template("form.html")


@app.route("/messages/<int:message_id>")
def message_detail(message_id):
    message = get_message_by_id(message_id)
    return render_template("message.html", message=message)


@app.route("/messages/<int:message_id>/delete", methods=["POST"])
def delete_message(message_id):
    delete_message_from_db(message_id)
    return redirect(url_for("index"))
