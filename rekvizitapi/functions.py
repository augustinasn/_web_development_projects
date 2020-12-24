from time import sleep

def getRekvizitaiUrl(d, code):
    d.get("https://rekvizitai.vz.lt/imoniu-paieska/")

    name_field = d.find_element_by_xpath("//input[@id='code']")
    name_field.send_keys(code) 
    
    ok_btn = d.find_element_by_id("ok")
    d.execute_script("arguments[0].click();", ok_btn)
    
    sleep(3)

    try:
        result = d.find_element_by_xpath("//div[@class='firm']/div[@class='info']/a[@class='firmTitle']")
    except:
        output = "Not found."
    else:
        output = result.get_attribute("href")

    return output

def scrapeRekvizitai(d, url):

    if url != "Not found.":
        d.get(url)

        title = d.find_element_by_xpath("//h1[@class='fn']").text
        vat_code = d.find_element_by_xpath("//td[contains(text(), 'PVM mokėtojo kodas')]/following-sibling::td").text
        address = d.find_element_by_xpath("//td[contains(text(), 'Adresas')]/following-sibling::td").text

        output = {
            "name": title,
            "vat": vat_code,
            "address": address
        }
    else:
        output = {
            "name": "Not found.",
            "vat": "Not found.",
            "address": "Not found."
        }

    return output