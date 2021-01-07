import os
import json
import requests
import datetime

from bs4 import BeautifulSoup
from facebook_scraper import get_posts


def restaurant_list():
    restaurants = {"untold": {
        "key": 1,
        "url": "https://kur-pietaut.herokuapp.com/restaurants/untold",
        "name": "Untold Grill Stories",
        "search_string": "untoldgrillstories",
        "favourite": 1
    },
        "ciop_ciop": {
        "key": 2,
        "url": "https://kur-pietaut.herokuapp.com/restaurants/ciop_ciop",
        "name": "Čiop Čiop",
        "search_string": "ciopciop",
        "favourite": 1
    },
        "natali": {
        "key": 3,
        "url": "https://kur-pietaut.herokuapp.com/restaurants/natali",
        "name": "Natali",
        "search_string": "natali",
        "favourite": 0
    }
    }

    return json.dumps(restaurants, ensure_ascii=False)


def scrape_ciop_ciop():
    url = "https://www.ciopciop.lt/pietus/"
    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

    with requests.get(url, headers=headers) as resp:
        page_content = resp.content

    html = BeautifulSoup(page_content, "html.parser")

    menu_div = html.find("div", {"id": "text-block-6"})
    menu_items = menu_div.findAll(["strong", "b", "li"])

    output = {"text": "",
              "image": "https://www.ciopciop.lt/wp-content/themes/cc/assets/img/logo-dark.svg",
              "time": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
              }

    for i in menu_items:
        output["text"] += i.text + "\n"

    return json.dumps(output, ensure_ascii=False)


def scrape_untold():
    first_post = {}

    for post in get_posts('UNTOLDrestoranas', pages=1):
        first_post["text"] = post["text"]
        first_post["image"] = post["image"]
        first_post["time"] = post["time"].strftime("%m/%d/%Y, %H:%M:%S")

        return json.dumps(first_post, ensure_ascii=False)


def scrape_natali():
    first_post = {}

    for post in get_posts('restoranasnatali', pages=1):
        first_post["text"] = post["text"]
        first_post["image"] = post["image"]
        first_post["time"] = post["time"].strftime("%m/%d/%Y, %H:%M:%S")

        return json.dumps(first_post, ensure_ascii=False)
