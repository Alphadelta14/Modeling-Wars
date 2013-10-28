""" @package web.home Flask Web Application: home blueprints """
####################################################################
#
#       Modeling Wars Web Application home routes
#
#       Author: Alpha <alpha@pokesplash.net>
#
####################################################################

from flask import Blueprint, render_template

__all__ = ["home"]

home = Blueprint("home_pages", __name__)

@home.route("/")
@home.route("/index")
def index():
    return render_template("home/index.html")