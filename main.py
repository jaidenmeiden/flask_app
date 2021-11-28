from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    user_ip = request.remote_addr
    return {
        'Hello': 'World Flask!',
        'IP': user_ip
    }
