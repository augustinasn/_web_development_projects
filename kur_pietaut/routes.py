from flask import jsonify, request

from kur_pietaut import App
from .functions import restaurant_list, scrape_ciop_ciop, scrape_untold, scrape_natali

import os


@App.route('/', methods=['GET', 'POST'])
def welcome():
    return 'Server is running.'


@App.route('/restaurants', methods=['GET', 'POST'])
def get_restaurants():
    restaurants = restaurant_list()

    return restaurants


@App.route('/restaurants/ciop_ciop', methods=['GET', 'POST'])
def get_ciop_ciop():
    menu = scrape_ciop_ciop()

    return menu


@App.route('/restaurants/untold', methods=['GET', 'POST'])
def get_untold():
    menu = scrape_untold()

    return menu


@App.route('/restaurants/natali', methods=['GET', 'POST'])
def get_natali():
    menu = scrape_natali()

    return menu
