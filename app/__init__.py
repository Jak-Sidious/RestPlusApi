from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

from flask_jwt_extended import (
    JWTManager , jwt_required, create_access_token,
    get_jwt_identity
)

cors = CORS()
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    cors.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    


    from app.apis import apiv1_bp
    app.register_blueprint(apiv1_bp , url_prefix='/apiv1')
    return app