from flask import Blueprint, render_template
from utils.register import register_service
from utils.login import login_service
from utils.logout import logout_user

core = Blueprint("core", __name__)

@core.route("/")
def home():
    return render_template("index.html")

@core.route("/register", methods=["GET", "POST"])
def register():
    return register_service()


@core.route("/login", methods=["GET", "POST"])
def login():
    return login_service()


@core.route("/logout", methods=["GET", "POST"])
def logout():
    return logout_user()