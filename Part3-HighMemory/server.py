from unittest import expectedFailure
from flask import Flask, request, send_from_directory

app = Flask(__name__)

arr = [1]

@app.route('/', methods=['GET'])
def chaos():
    for x in list(arr):
        arr.append(x)

    return "Hello from the server!"

app.run(port=8080)

        