from flask import Flask, render_template

app = Flask(__name__)

menu_list = ["menu_1", "menu_2", "menu_3"]


@app.route("/")
@app.route("/index/")
def index_page():
    return render_template("index.html", text="Main page of the website!", main_string="--Flask - it is very COOL!--")


@app.route("/about/")
def about_page():
    return render_template("about.html")


# @app.route("/list/")
# def list_page():
#     return [item for item in range(1, 11)]

@app.route("/list/")
def list_page():
    return render_template("list.html", title="List_List", string_1="gygygjyjgyjggjgyjgyg")


@app.route("/menu/")
def menu_page():
    return render_template("menu.html", menu=menu_list)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
