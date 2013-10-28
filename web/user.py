""" @package web.user Flask Web Application: user blueprints """
####################################################################
#
#       Modeling Wars Web Application User routes
#
#       Author: Alpha <alpha@pokesplash.net>
#
####################################################################

from flask import Blueprint, render_template

__all__ = ["user_blueprint"]

user_blueprint = Blueprint("user_pages", __name__)

@user_blueprint.route("/")
@user_blueprint.route("/index")
def index():
    return render_template("user/index.html")