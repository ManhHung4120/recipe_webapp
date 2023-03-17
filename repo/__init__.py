from flask import Flask
from repo.config import *
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def create_app(config_class = DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    from user.user_blueprint import user_blueprint
    from recipe.recipe_blueprint import recipe_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(recipe_blueprint)
    from models import User,Recipe
    return app