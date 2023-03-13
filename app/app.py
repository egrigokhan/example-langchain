from flask import Flask, request, jsonify
from src.index import query

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def handle_query():
    message = request.json['msg']
    response = query(message)
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=8080)
