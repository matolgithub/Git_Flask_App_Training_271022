from flask import Flask
from flask import jsonify
from flask.views import MethodView

app = Flask("app")


class HelloWorld(MethodView):

    def get(self):
        return jsonify({"http_method": "GET", "hello": "world"})

    def post(self):
        return jsonify({"http_method": "POST", "hello": "world"})

    def patch(self):
        return jsonify({"http_method": "PATCH", "hello": "world"})

    def delete(self):
        return jsonify({"http_method": "DELETE", "hello": "world"})


app.add_url_rule('/hello_world/', view_func=HelloWorld.as_view("hello-world"),
                 methods=["GET", "POST", "PATCH", "DELETE"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
