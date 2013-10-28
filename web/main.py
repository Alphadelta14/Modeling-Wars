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

app = Flask(__name__, template_folder='../templates',
    static_folder='../static')

if __name__ == "__main__":
    http = WSGIServer(('127.0.0.1', 5000), app)
    http.serve_forever()