# from flask import jsonify

import json
import os

from rekvizitapi import App

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from .functions import getRekvizitaiUrl, scrapeRekvizitai

OPTIONS = webdriver.ChromeOptions() # Options()

OPTIONS.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--disable-gpu")
OPTIONS.add_argument("--no-sandbox")
                          
@App.route("/", methods=["GET", "POST"])
def welcome():
    return "Server is running."

@App.route("/company/<comp_id>", methods=["GET", "POST"])
def scrape_company(comp_id):
    DRIVER = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                              options=OPTIONS)

    rekvizitai_url = getRekvizitaiUrl(DRIVER, comp_id)

    rekvizitai_output = scrapeRekvizitai(DRIVER, rekvizitai_url)
    
    DRIVER.close()
    DRIVER.quit()
    
    return json.dumps(rekvizitai_output, ensure_ascii=False)