
'''
Importowanie pakunków(bibliotek) z zewnatrz nie bedacych w standarcie bibliotek Pythona np. requests
pip - instalator pakunków
PyPi - Python Package Index - indeks(spis) pakunkow do Pythona


'''


import requests
import json
import pprint

daneGoogle = requests.get("http://google.pl/")

# print(daneGoogle.status_code)

# zawartoscStrGoogle = str(daneGoogle.content)

# with open("StronaGoogle.json", "w", encoding="UTF-8") as file:
#     json.dump(zawartoscStrGoogle, file, ensure_ascii=False, indent=4)
    