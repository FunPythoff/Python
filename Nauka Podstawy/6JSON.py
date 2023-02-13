

'''
JSON - uzywany jest do przetlumaczenia kodu z jednego jezyka na jezyk JSON i z JSON na np. JavaScript.

json.dumps(data) - zapisuje dane do postaci Stringowej json. (dump's' - 's' jest od stringa)
json.dump(data, nameOfFileHandler, ensure_ascii=False) - zapisuje dane do pliku w postacji json

dump z ang. zsypać/zwalić/zrzucać
'''

from base64 import decode
import json


film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
        }

codedOnJson = json.dumps(film) # zapisuje obiekt w postaci stringa, ale przeksztalcony na jezyk json
codedOnJson = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)   # ensure_ascii=False - zmieniamy z powodu tabeli "ascii", 
                                                                               # gdzie nie ma tam polskich znakow, indent=4 dajemy zeby ladnie nam wyprintowalo, 
                                                                               # sort_keys=True sortuje alfabetycznie

with open("SampleJSON.json", "w", encoding="UTF-8") as file:            ### W ten sposob tworzymy plik i zapisujemy w nim to co ponizejVVVVVVVV
    json.dump(film, file, ensure_ascii=False,indent=4, sort_keys=True)  ### W ten sposob zapisujemy obiekt(film) za pomoca uchwytu (file) w pliku (SampleJSON.json) 
                                                                        ### z rozszerzeniem .json, tablica z polskimi znakami, wcieciem = 4, posortowane alfabetycznie


# encodedJson = json.dump(film, file, ensure_ascii=False)

# with open("SampleJSON.json", "r", encoding="UTF-8") as file:            # W ten sposob czytamy plik, wskazujemy kodowanine UTF-8 aby nie bylo znaczkow i chwycimy to do "file"
#     rozkodowane = json.load(file)                                       # tutaj zapisujemy wartosc do obiektu "rozkodowane" i zmienamy format json na .py z uchwytu czyli "file"

# json.loads()                                                            #zmiana wartosci stringowej na pythonową

# print(rozkodowane)










