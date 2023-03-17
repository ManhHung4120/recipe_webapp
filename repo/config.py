import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ""
    
class ProductConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
   

class TestingConfig(Config):
    TESTING = True