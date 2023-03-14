from flask import Flask, request, jsonify
from src.index import run, setup

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/setup', methods=['POST'])
def handle_setup():
    config = request.json['config']
    response = setup(config)
    return jsonify({"success": True, "message": response})


@app.route('/run', methods=['POST'])
def handle_run():
    message = request.json['msg']
    response = run(message)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
