from flask import flash, redirect, url_for
from flask_login import logout_user as flask_logout_user


def logout_user():
    flask_logout_user()
    flash("Çıkış yapıldı.", "success")
    return redirect(url_for("core.home"))