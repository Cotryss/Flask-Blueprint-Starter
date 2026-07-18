from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models import User


def register_service():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Tüm alanları doldurun.", "danger")
            return redirect(url_for("core.register"))

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Bu kullanıcı adı zaten alınmış.", "warning")
            return redirect(url_for("core.register"))

        user = User(
            username=username,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        flash("Kayıt başarılı.", "success")
        return redirect(url_for("core.login"))

    return render_template("register.html")