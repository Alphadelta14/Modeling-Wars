""" @package web.user Flask Web Application: user blueprints """
####################################################################
#
#       Modeling Wars Web Application User routes
#
#       Author: Alpha <alpha@pokesplash.net>
#
####################################################################

from flask import Blueprint, render_template, request, session

__all__ = ["user_blueprint"]

INVALID_USER = "Incorrect Username/Password"

user_blueprint = Blueprint("user_pages", __name__)

@user_blueprint.route("/")
@user_blueprint.route("/index")
def index():
    return render_template("user/index.html")

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        if not data:
            return render_template("user/login.html", error="Bad request")
        username = data.get("username", "")
        password = data.get("password", "")
        if not username or not password:
            return render_template("user/login.html", error=INVALID_USER)
        # TODO: Database auth
    else:
        return render_template("user/login.html")