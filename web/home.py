""" @package web.home Flask Web Application: home blueprints """
####################################################################
#
#       Modeling Wars Web Application home routes
#
#       Author: Alpha <alpha@pokesplash.net>
#
####################################################################

from flask import Blueprint

__all__ = ["home"]

home = Blueprint("home_pages", __name__)
