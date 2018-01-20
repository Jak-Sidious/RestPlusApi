import sys

from flask import Flask, jsonify, request
from flask_restplus import Api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

app = Flask(__name__)

from app.apis import apiv1_bp
app.register_blueprint(apiv1_bp , url_prefix='/apiv1')
# return app

if __name__ == '__main__':
    app.run()

