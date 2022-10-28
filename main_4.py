from flask import Flask, render_template

app = Flask(__name__)


@app.route("/profile/")
@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", title="User profile", username=username)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
