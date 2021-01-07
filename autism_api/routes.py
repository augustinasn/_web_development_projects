from flask import jsonify, request

from autism_api import app
from autism_api.functions import predict


@app.route("/", methods=["GET", "POST"])
def welcome():
    return "Server is running and is ready for requests."


@app.route("/predict_autist", methods=["GET", "POST"])
def web_search():
    req = request.form

    text = req["text"]

    res = predict(text)

    return res
