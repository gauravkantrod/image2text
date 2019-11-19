from flask import Flask, request, jsonify

app1 = Flask(__name__)

from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import pytesseract
import os
import re


@app.route("/appcheck", methods = "GET")
def check_app_up():
    return "Application is running."


@app.route("/extract_date", methods=['POST'])
def get_data():
    file = request.files['file']
    text = pytesseract.image_to_string(Image.open(file).convert("L"), lang='eng')
    date = re.findall(r'\d{2}[./-]\d{2}[-./]\d{2,4}|\d{2,4}[-/]\w{3,4}[-/]\d{2,4}|\d{1,2}[/]\d{2,4}|\w{3,9}\s?\d{1,2}[\,]\s?\d{4}|\d{2}[/]\w{3,9}[/]\d{2,4}',text)
    if len(date) == 0:
        return jsonify(date='null')
    else:
        return jsonify(date=date)




