# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:39:27 2021

@author: home
"""

import requests

url = "https://language-translation.p.rapidapi.com/translateLanguage/detect-language"

querystring = {"text":"Привет, мой дорогой друг!"}

headers = {
    'x-rapidapi-key': "5d797ab107mshe668f26bd044e64p1ffd34jsnf47bfa9a8ee4",
    'x-rapidapi-host': "language-translation.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)