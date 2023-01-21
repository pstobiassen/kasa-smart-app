import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "<h1>My Kasa API</h1><p>This site is a prototype API for my Kasa Smart Device App.</p>"


app.run()
