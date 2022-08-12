from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hey from the server."

app.run(port=9000)

'''
aryanharitsh@production-new:~$ sudo iptables -A INPUT -p tcp --destination-port 9000 -j DROP
aryanharitsh@production-new:~$ sudo iptables -F
'''