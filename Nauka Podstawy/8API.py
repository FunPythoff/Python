

import json
import webbrowser
from datetime import datetime, timedelta
from enum import Enum
from pprint import pprint
import requests

'''
API - Application Programming Interface

APIs are mechanisms that enable two software components to communicate with each other 
using a set of definitions and protocols. For example, the weather bureau's software 
system contains daily weather data. The weather app on your phone “talks” to this system
 via APIs and shows you daily weather updates on your phone.

'''

'''
Zadanie:
    Pobrac ostatnie pytania ze strony stackoverflow.com i posortowac:
    -min 15 puntkow
    -malejaco
    -z calego tygodnia
    -kategoria python

'''
'''
daysToChange = timedelta(days=7)
daysIntrested = datetime.today() - daysToChange

params = {
    "site" : "stackoverflow",        # bierz ze strony stackoverflow
    "sort" : "votes",                # sortuj po glosach
    "order": "desc",                 # sortuj malejaco
    "fromdate" : int(daysIntrested.timestamp()),  # wykorzystaj funkcje datatime do pobrania dzisiejszej daty i timestamp do przedstawienia jej w sekundach (od 1970)
    "tagged" : "python",
    "min" : 5
}


r = requests.get("https://api.stackexchange.com/2.3/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
'''


params = {
    "api_key" : "07af2b20aeb4466ba58253f62428b70a",
    "country" : "PL",
    "year" : "2020",
    "month" : "12",
    "date" : "25",

}
# https://holidays.abstractapi.com/v1/?api_key=07af2b20aeb4466ba58253f62428b70a&country=US&year=2020&month=12&day=25
r = requests.get("https://holidays.abstractapi.com/v1/?", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Coś nie tak z linkiem")
else:
    # for item in content:
        pprint(content)
        # print(webbrowser.open_new_tab(item["url"]))




 