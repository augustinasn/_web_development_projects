from flask import jsonify, request
from foxtrapper_api import app
from foxtrapper_api.functions import detect_web, get_similar_products_file, file_upload

import os
import json


@app.route("/", methods=["GET", "POST"])
def welcome():
    return "Server is running and is ready for requests."


@app.route("/web_search", methods=["GET", "POST"])
def web_search():
    file = request.files["file"]
    destination = file_upload(file)

    web_results = detect_web(destination)
    local_results = get_similar_products_file(
        "foxtrapper", "europe-west1", "laptops", "homegoods-v2", destination, None
    )
    results = web_results + local_results

    return json.dumps(results)

