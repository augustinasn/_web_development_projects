# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\G022409\Documents\keyFile.json

import argparse
import io
import re
import os
import uuid

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

def generate_filename():
    filename = str(uuid.uuid4().hex)[:15] + ".jpg"

    return filename

def detect_text(path):

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    strings = [text.description.replace("\n", "")
                for text in texts]

    print(strings)

    return strings

def save_img(app, file):
    fn = generate_filename()
    fp = os.path.join(app.root_path,
                          "static",
                          fn)

    img = Image.open(file)
    img.save(fp)

    return fn, fp

def parse_text(list_of_words):
    full_text = " ".join(list_of_words)

    try:
        surname = re.findall("1\.\s{0,1}([ĄČĘĖĮŠŲŪŽA-Z]+)", full_text)[0]
    except:
        surname = "-"

    try:
        name = re.findall("2\.\s{0,1}([ĄČĘĖĮŠŲŪŽA-Z]+)", full_text)[0]
    except:
        name = "-"

    try:
        born = re.findall("3\.\s{0,1}([0-9\s]{10})", full_text)[0]
    except:
        born = "-"

    try:
        valid_from = re.findall("4a\.\s{0,1}([0-9\s]{10})", full_text)[0]
    except:
        valid_from = ""
    
    try:
        valid_until = re.findall("4b\.\s{0,1}([0-9\s]{10})", full_text)[0]
    except:
        valid_until = ""

    output = {
        "name": name,
        "surname": surname,
        "born": born,
        "valid_from": valid_from,
        "valid_until": valid_until
    }

    return output
