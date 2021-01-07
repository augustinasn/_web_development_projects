from time import sleep
from PIL import Image
from io import BytesIO
from datetime import datetime
from google.cloud import vision

import io
import os
import time

def grab_captcha(d):
    try:
        d.get("https://www.vmi.lt/cms/lt/informacija-apie-mokesciu-moketojus")
    except:
        print("Page is taking longer to load.")

    time.sleep(10)

    el = d.find_element_by_xpath("//img[@class='captcha']")

    img = el.screenshot_as_png

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

    filepath = os.path.join(os.getcwd(),
                            "vatsonas_api",
                            'captchas',
                            f"{timestamp}.png")

    with open(filepath, "wb") as fp:
        fp.write(img)

    return filepath


def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts[0].description

def scrape_vmi_info(d, code, captcha):
    tab = d.find_element_by_xpath("//a[contains(text(), 'Juridiniai asmenys')]")
    tab.click()

    code_el = d.find_element_by_xpath("//input[@name='_taxespayersportlet_WAR_eskisliferayportlet_juridical_code']")
    captcha_el = d.find_element_by_xpath("//input[@name='_taxespayersportlet_WAR_eskisliferayportlet_captchaText']")
    
    code_el.send_keys(code)
    captcha_el.send_keys(captcha)

    search_key = d.find_element_by_xpath("//input[@value='Ieškoti']")
    search_key.click()

    vat_code = d.find_element_by_xpath("//td[contains(text(), 'PVM mokėtojo kodas')]/following-sibling::td").text

    return vat_code



# def getRekvizitaiUrl(d, code):

#     name_field = d.find_element_by_xpath("//input[@id='code']")
#     name_field.send_keys(code) 
    
#     ok_btn = d.find_element_by_id("ok")
#     d.execute_script("arguments[0].click();", ok_btn)
    
#     sleep(3)

#     try:
#         result = d.find_element_by_xpath("//div[@class='firm']/div[@class='info']/a[@class='firmTitle']")
#     except:
#         output = "Not found."
#     else:
#         output = result.get_attribute("href")

#     return output

# def scrapeRekvizitai(d, url):

#     if url != "Not found.":
#         d.get(url)

#         title = d.find_element_by_xpath("//h1[@class='fn']").text
#         vat_code = d.find_element_by_xpath("//td[contains(text(), 'PVM mokėtojo kodas')]/following-sibling::td").text
#         address = d.find_element_by_xpath("//td[contains(text(), 'Adresas')]/following-sibling::td").text

#         output = {
#             "name": title,
#             "vat": vat_code,
#             "address": address
#         }
#     else:
#         output = {
#             "name": "Not found.",
#             "vat": "Not found.",
#             "address": "Not found."
#         }

#     return output