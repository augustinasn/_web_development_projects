from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "b9147debbf1525fbf88d3dcb7f14b511"

from ocr_app import routes