import os

from flask import Flask
from pathlib import Path

from config import Config
from extensions import db, logger, login_manager
from models import User

from startup.blueprints import register_blueprints
from startup.database import initialize_database

BASE_DIR = Path(__file__).resolve().parent.parent

def create_app():
    app = Flask(__name__, 
    template_folder=str(BASE_DIR / "templates"), 
    static_folder=str(BASE_DIR / "static"))

    app.config.from_object(Config)

    register_blueprints(app)

    db.init_app(app)

    login_manager.init_app(app)

    initialize_database(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        logger.info("Web server started successfully")

    return app