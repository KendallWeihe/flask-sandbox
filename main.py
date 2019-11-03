from flask import Flask, jsonify
import json

app_name = "kendalls-flask-app"
app = Flask(app_name)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/dummy_data/<name>")
def get_dummy_data(name):
    f = open("dummy_data/{0}.json".format(name), "r")
    return jsonify(json.loads(f.read()))

if __name__ == '__main__':
    app.run(host="0.0.0.0")