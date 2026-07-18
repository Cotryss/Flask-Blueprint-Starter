from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from models import User


def login_service():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user:
            flash("Kullanıcı bulunamadı.", "danger")
            return redirect(url_for("security.login"))

        if not check_password_hash(user.password, password):
            flash("Şifre hatalı.", "danger")
            return redirect(url_for("security.login"))

        login_user(user)

        flash("Giriş başarılı.", "success")
        return redirect(url_for("core.home"))

    return render_template("login.html")