from flask import Flask
from backend.controller import controller

app = Flask(__name__)
app.register_blueprint(controller)

if __name__ == '__main__':
    app.run(host="localhost", port=9081)
