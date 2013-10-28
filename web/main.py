""" @package web.main Flask Web Application """
####################################################################
#
#       Modeling Wars Web Application main routes
#
#       Author: Alpha <alpha@pokesplash.net>
#
#################################################################### 

from flask import Flask
from gevent.pywsgi import WSGIServer

from web.home import home

app = Flask(__name__, template_folder='../templates',
    static_folder='../static')
app.register_blueprint(home)


if __name__ == "__main__":
    http = WSGIServer(('127.0.0.1', 5000), app)
    http.serve_forever()