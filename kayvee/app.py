from flask import Flask, request, render_template
from flask.wrappers import Response
from kayvee.store import Store

app = Flask(__name__)
store = Store()

@app.route("/")
def get_ui() -> str:
    return render_template("index.html", store=store)

@app.route("/<string:key>", methods=["GET"])
def get_key(key: str) -> Response:
    return Response(store.get(key))

@app.route("/<string:key>", methods=["POST"])
def set_key(key: str) -> Response:
    store.set(key, request.get_data())
    return Response(key)
