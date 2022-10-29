from flask import Flask, render_template, request

app = Flask(__name__)

menu_list = [
    {"name": "Install", "url": "install"},
    {"name": "First application", "url": "first_app"},
    {"name": "Contacts", "url": "contacts"},
]


@app.route("/")
@app.route("/index/")
def index_page():
    return render_template("index.html", title="Index_Title",
                           text="Main page of the website!", main_string="--Flask - it is very COOL!--")


@app.route("/about/")
def about_page():
    return render_template("about.html", title="About_title")


@app.route("/list/")
def list_page():
    return render_template("list.html", title="List_Title", string_1="this is string_1")


@app.route("/menu/")
def menu_page():
    return render_template("menu.html", title="Menu_title", menu=menu_list)


@app.route("/profile/")
@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", title="User profile", username=username)


@app.route("/menu/contacts/", methods=["GET", "POST"])
def contacts_page():
    if request.method == "POST":
        # print(request.form)
        print(f" We get from web the name: {request.form['username']},email: {request.form['email']}")
    return render_template("contacts.html", title="Contacts_title")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
