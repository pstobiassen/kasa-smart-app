import flask
from flask import jsonify, request
from discover import DiscoverDevices

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "<h1>My Kasa API</h1><p>This site is a prototype API for my Kasa Smart Device App.</p>"


@app.route("/api/discover", methods=["GET"])
def discover_devices():
    return jsonify(DiscoverDevices())


app.run()
