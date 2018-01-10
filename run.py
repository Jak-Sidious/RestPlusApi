from flask import Flask
from flask_restplus import Resource, Api, fields
from werkzeug.contrib.fixers import ProxyFix
from app.apis import api

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
