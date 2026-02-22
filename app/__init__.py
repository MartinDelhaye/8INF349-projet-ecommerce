from flask import Flask
from .models import db
from .routes.accounts import accounts_bp
from .routes.transactions import transactions_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(accounts_bp)
    app.register_blueprint(transactions_bp)

    @app.cli.command("init-db")
    def init_db():
        from .models import Account, Transaction
        db.create_tables([Account, Transaction])

    return app