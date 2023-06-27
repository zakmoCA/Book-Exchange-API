from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.books_bp import books_bp
from blueprints.users_bp import users_bp


#This is a factory function, a function whose job is to create and configure, and return an object
def create_app():
    app = Flask(__name__)
    # app.debug = True

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(cli_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)

    # Using 'flask run' will run the app as long as this file is called app.py
    # and as long as our code is wrapped inside a 'create_app()' function
    return app
    # When i run this in terminal, set env var = 'FLASK_DEBUG=1 flask run' to run in debug
    # OR create '.flaskenv' file and add FLASK_DEBUG=1

