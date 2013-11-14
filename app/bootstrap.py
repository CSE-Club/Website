from flask import Flask
from flask import Blueprint
from . import blueprints
import importlib


def create_app():

    app = Flask(__name__)
    app.config.from_object('app.settings')

    # Register all blueprint packages
    for package_name in blueprints.__all__:
        package = importlib.import_module('app.blueprints.%s' % (package_name))
        for module_name in package.__all__:
            module = importlib.import_module(
                'app.blueprints.%s.%s' % (package_name, module_name))
            for item in dir(module):
                item = getattr(module, item)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)

    return app
