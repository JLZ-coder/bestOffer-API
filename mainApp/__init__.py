from flask import Flask
import os
from . import users


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    
    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(users.bp)

    return app

