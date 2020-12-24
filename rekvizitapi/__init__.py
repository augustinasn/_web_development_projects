from flask import Flask
from flask_cors import CORS

App = Flask(__name__)

CORS(App)

from rekvizitapi import routes