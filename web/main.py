""" @package web.main Flask Web Application """
####################################################################
#
#       Modeling Wars Web Application main routes
#
#       Author: Alpha <alpha@pokesplash.net>
#
#################################################################### 

from flask import Flask

app = Flask(__name__, template_folder='../templates',
    static_folder='../static')

