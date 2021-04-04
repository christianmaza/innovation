
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts", methods=["GET"])
def posts():

    # get start and endpoints for the newly generated posts
    start = int(request.args.get("start") or 0)
    end = int(request.args.get("end") or (start + 14))

    data = []

    # render new cards from the card template
    for i in range(start, end + 1):
        data.append(render_template("card.html"))

    return jsonify(data)
