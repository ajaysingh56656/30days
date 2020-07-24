from flask import Flask

app = Flask(__name__)


# taskkill /f /im ngrok.exe # stop ngrok session
# http://localhost:8000/
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world. This is Flask'


# http://localhost:8000/abc
@app.route('/abc', methods=['GET'])
def abc_view():
    return 'Hello, world. This is abc'


env: app = "server1.py"
# flask run command
