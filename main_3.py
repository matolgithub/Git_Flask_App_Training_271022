from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index_page():
    return "It is index page!"


@app.route("/about/")
def about_page():
    return "<h1>About us!</h1>"


@app.route("/list/")
def list_page():
    return [item for item in range(1, 11)]


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
