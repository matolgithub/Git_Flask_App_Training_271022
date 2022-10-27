from flask import Flask
from flask import jsonify

app = Flask('app')


def hello_world():
    return jsonify({'hello': 'world'})


app.add_url_rule('/hello_world/', view_func=hello_world, methods=['GET'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
