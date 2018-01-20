# /instance/config.py
''' This script contains all the environment configurations'''

class Config(object):
    '''The base configurations all the environments should have'''
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "3te6guqywd6tug"
    SQLALCHEMY_DATABASE_URI = 'postgresql:///yummy_db2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    '''Configurations for Development. '''
    DEBUG = True
    RESTPLUS_VALIDATE = True


class TestingConfig(Config):
    '''Configurations for testing with a separate test database'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///testing_db'
    DEBUG = False

class ProductionConfig(Config):
    '''Configurations for Preoduction.'''
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig
}

