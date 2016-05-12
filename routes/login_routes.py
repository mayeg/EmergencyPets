from flask.blueprints import Blueprint
from flask import request, redirect, url_for
from controllers.login import Login

login_r = Blueprint("login", __name__)


@login_r.route("/", methods=["GET"])
def get_home():
    return Login().get_home_usuario()


@login_r.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return Login().get_login_iniciar()
    email = request.form.get('email', None)
    contrasena = request.form.get('contrasena', None)
    Login().login(email, contrasena)
    return redirect(url_for("login.get_home"))


@login_r.route("/logout", methods=["GET"])
def logout():
    Login().logout()
    return redirect(url_for("login.get_home"))
