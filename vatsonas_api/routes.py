# from flask import jsonify

import json
import os

from vatsonas_api import App

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from .scraping_functions import grab_captcha, detect_text, scrape_vmi_info

from flask import send_file

OPTIONS = webdriver.ChromeOptions() # Options()

OPTIONS.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--disable-gpu")
OPTIONS.add_argument("--no-sandbox")
OPTIONS.add_argument("--window-size=1920,1080")

                          
@App.route("/", methods=["GET", "POST"])
def welcome():
    DRIVER = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                              options=OPTIONS)

    DRIVER.set_page_load_timeout(60)
    
    try:
        DRIVER.get("https://www.vmi.lt/cms/lt/informacija-apie-mokesciu-moketojus")
    except:
        DRIVER.close()
        DRIVER.quit()
        
        return "Server is running, but VMI.lt is taking longer to load. Try again later."
    
    DRIVER.close()
    DRIVER.quit()
    
    return "Server is running."

@App.route("/company/<comp_id>", methods=["GET", "POST"])
def scrape_company(comp_id):
    DRIVER = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                              options=OPTIONS)

    DRIVER.set_page_load_timeout(25)

    img_fp = grab_captcha(DRIVER)

    DRIVER.close()
    DRIVER.quit()

    captcha = detect_text(img_fp)

    vat_code = scrape_vmi_info(DRIVER, comp_id, captcha)

    return "VAT Code - " + vat_code
    
    # return json.dumps(rekvizitai_output, ensure_ascii=False)