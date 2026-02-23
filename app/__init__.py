from flask import Flask
from .routes.products import products_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp)

    return app