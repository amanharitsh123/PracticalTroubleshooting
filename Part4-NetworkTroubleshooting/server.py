from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hey from the server."

app.run(port=9000)