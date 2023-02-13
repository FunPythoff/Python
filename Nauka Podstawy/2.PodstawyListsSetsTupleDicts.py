

################################################# DICTIONARY ###################################################

'''
Tworzymy w klamrach {} w sposób {KLUCZ : WARTOŚĆ}
Klucze identyfikuja zawsze tylko jedna wartość (nie moze byc dwoch takich samych kluczy)

'''



pokoje = {1 : "Michał Gaj", 
          2 : "Elżbieta Gaj",
          100 : "Ania Kowalska"
          }

# print(len(pokoje)) #pokazuje dlugosc listy
# print(pokoje.get(1))    #wyprintuje mi dany element ze slownika


# print(pokoje)
# print(pokoje.items()) #robi nam ze slownika krotke, z na krotkach mozemy juz przypisywać sobie dane elementy ktore sa po przecinku

# pokoje.update({3: "Ania",4: "Paweł"})
# print(pokoje.get(3))
# print(pokoje.get(4))
# pokoje.popitem() # usuwa mi ostatni element ze slownika
# print(pokoje)

# pokoje.update({50 : "Marek Kowalewicz"})  # dodaje mi element do slownika
# print(pokoje)

# pokoje.__delitem__ (2) # usuwa mi klucz wraz z wartością
# print(pokoje)

# pokoje.update({30 : "Ela Gaj"})

# pokoje.update({"Pokoj milosci" : "Ktos z kims"})
# print(pokoje)

# pokoje.update({"Wynik dodawania" : 3+3})
# print(pokoje)
# print(pokoje[50])

# pokoje.pop(1)
# print(pokoje)
# print()




# Slownik w slowniku:

# Dodawanie nowych elementow do slownika jest o wiele lepsze, nie ma znaczenia kolejnosc w slowniku
# Mozna zastosowac identyfikatowy np. id: Vrasd213a1212


# Slownik w liscie:

# Stosujemy, bo pomaga nam to zidentyfikować dane wewnatrz. Zyskujemy na czytelnosci i przetwarzaniu danych. Mozna skategoryzowac dane.
# Stosujemu jesli zalezy nam na kolejnosci danych


dziennik = {
    "Arkadiusz" : (2,1,3,4,2,1),
    "Wiola" : (5,3,2,1,4,2),
    
    }


# for key in dziennik:
    # print(key, dziennik[key])




#                   id         /                    firstkey
people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
        "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
        "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
        "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
        "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
        "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}           
         }

"""
for id, firstkey in people.items():             #lepsza funkcja - szybsza
    print("ID: ", id)
    for secondkey in firstkey:
        print(secondkey, ":", firstkey[secondkey])

"""


"""
for firstkey in people:
    print("ID: ",firstkey)
    for secondkey in people[firstkey]:
        print(secondkey, ":", people[firstkey][secondkey])

"""
        



people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]

# for value in people2:
#     for value2 in value:
#         print(value2, ":", value[value2])




ratings = {
        "Arkadiusz": (2,1,2,3,2,3),
        "Wiola": (4,2,1,3,4)
    }

# for name in ratings:
#     print(name, ratings[name])


ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]


################################################ TYPY ZAGNIEZDZONE  ###############################################


# Typy zagniezdzone uzywamy aby nie tworzyc wiele zmiennych np. imie, nazwisko, wiek, plec. tylko robimy to jako jedna liste (zagniezdzona)


# lista_gosci = [
#                 ["Michal", 26, "Gaj"],                      # ta lista stworzona jest jako lista i mozemy je zmieniac, dodawac, usuwac itp.
#                 ["Krzysiek", 35, "Nowak"],
#                 ["Ania", 19, "Maziarz"],
#                 ["Elzbieta", 20, "Gaj" ],
#               ]

# print(lista_gosci[0])
# print(lista_gosci[1])
# print(lista_gosci[2])
# print(lista_gosci[3])

# lista_gosci[1][1] = 25
# print(lista_gosci[1])



# lista_gosci = (
#                 ("Michal", 26, "Gaj"),                      # ta lista stworzona jest jako krotka i nie mozemy zmienic danych, ale mozemy je dodawac
#                 ("Krzysiek", 35, "Nowak"),                    #najczesciej uzywana bo ma plusy listy i szybkosc krotki
#                 ("Ania", 19, "Maziarz"),
#                 ("Elzbieta", 20, "Gaj" ),
#               )

# lista_gosci.append(("Karol", 20, "Nijaki"))         # .append dodaje na koniec listy
# print(lista_gosci)


# lista_gosci = (
#                 ("Michal", 26, "Gaj"),                      # ta krotka stworzona jest jako krotka i nie mozemy zmienic danych
#                 ("Krzysiek", 35, "Nowak"),
#                 ("Ania", 19, "Maziarz"),
#                 ("Elzbieta", 20, "Gaj" ),
#               )


lista_gosci = {
                ("Michal", 26, "Gaj", 55),                      # ten set(zbior) stworzona jest jako krotka i mozemy zmienic korzystac z funkcji zbiorow.
                ("Krzysiek", 35, "Nowak", 60),                   
                ("Ania", 19, "Maziarz", 20),
                ("Elzbieta", 20, "Gaj", 30),
            }

lista_gosci.add(("Karol", 20, "Nijaki", 30))                    #funkcja .add dodam nam element, ale nie ma scisle okreslonego miejsca
# print(lista_gosci)

lista_gosci2 = {
                ("M", 26, "G"),                      # ten set(zbior) stworzona jest jako krotka i mozemy zmienic korzystac z funkcji zbiorow.
                ("K", 35, "N"),                   
                ("A", 19, "M"),
                ("E", 20, "G" ),
            }

lista_gosci3 = lista_gosci | lista_gosci2

# print(lista_gosci3)
for imie, wiek, nazwisko, numerButa in lista_gosci:
    print("Imie:", imie)
    print("Wiek:", wiek)
    print("Nazwisko:", nazwisko)
    print("Numer buta:", numerButa)
    print("\n")

# import sys

## Wyrazenia(formuly) listowe uzywamy aby zmienic stara liste w cos nowego.

'''liczby = [1, 2, 3, 4, 5, 6]

potegowanie = []                        # ten sposob jest wolniejszy, lepszy jest ten na dole
for element in liczby:
    potegowanie.append(element ** 2)
print(potegowanie)'''

'''
potegiDwa  = [element**2 
              for element in liczby
              ]

print(potegiDwa)

liczbyNieparzyste = [element                   #co zrobic na danym elemencie z listy
                     for element in liczby     #tutaj wskazujemy dane do przerobienia
                     if element % 2 != 0       #tutaj wskazujemy warunek jaki ma byc spelniony
                     ]
print(liczbyNieparzyste)
'''


'''liczbyParzyste = (element
                  for element in range(0,200)
                  if element % 2 == 0 
)                

print(liczbyParzyste)'''

    # stosujac wyrazenie listowe[] zajmie on nam wiecej miejsca w pamieci
    # stosujemy go jesli chcemy zapisać szukane dane i coś z nimi zrobić (wykonywać na nich operacje)

# ListaPierwsza = [element
#                 for element in range(100)
#                 if element % 2 == 0
#                 ]

# print(ListaPierwsza)




############################################################################################################
    # stosujac wyrazenie generujace () zajmie on mniej miejsca w pamieci
    # nie zapisujemy zawartosci w pamieci komputera, pozwala nam to je np. 
    # tylko przepisac bez marnowania pamieci komputera na zapisywanie zawartosci 
    # stosujemy je gdy mamy do czynienia z wielkimi plikami, gdzie chcemy np. cos znalezc, ale nie zapisywac tego w pamieci komputera


ListaDrugaGenerator = (element
                for element in range(5)
                if (element % 2 == 0)
                )

print(ListaDrugaGenerator)

print(sum(ListaDrugaGenerator))

for a in ListaDrugaGenerator:
    print(a)


# print(sys.getsizeof(ListaPierwsza))
# print(sys.getsizeof(ListaDrugaGenerator))


ListaDrugaGenerator = (element ** 2
                for element in range(101)
                )

# for a in ListaDrugaGenerator:
#     print(a)

# print(sum(ListaDrugaGenerator))


#####
# Wyrazenia słownikowe piszemy w klamrach zakreconych {} tak jak i slowniki
#####


Names = ["Arkadiusz", "Michal", "Ania", "Elzbieta", "Krzysztof", "Monika"]

Numbers = [1, 2, 3, 4, 5, 6, 7]

TempCelcius = {"Temperatura 1": 0, "Temperatura 2": 20, "Temperatura 3": 30, "Temperatura 4": 15, "Temperatura 5": -1, "Temperatura 6": 25}

print(TempCelcius)
print(TempCelcius.items())
# NamesLenght = {
#                 name: len(name)
#                 for name in Names
#                 } 

# print(NamesLenght)

# MultipliedNumbers = {
#                     Numbers : Numbers * Numbers
#                     for Numbers in Numbers
#                     }

# print(MultipliedNumbers)

Fahrenheit = {
        Temperature : TempCelcius * 1.8 + 32
        for Temperature, TempCelcius in TempCelcius.items()
        }

print(Fahrenheit)

######
#   Wyrażenia zbioru
#####

names = {"michal", "ania", "karolina", "pawel", "alicja"}

namesC = {
        name.capitalize()
        for name in names
        if name.startswith("a") != True
        }

# print(namesC)



############################################### PODSUMOWANIE ##############################################


"""
     czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy     []    NIE           TAK             TAK                   TAK
krotki    ()    NIE           TAK             NIE                   NIE
słowniki  {}    TAK           NIE             TAK                   TAK
zbiory    {}    TAK           NIE             NIE                   TAK

        ZBIORY: BONUS w postaci 
        | suma sumuje nam oba zbiory
        & koniunkcja daje nam wspolne elementy ze zbiorow
        - odejmowanie wynikiem jest to co jest w A, a nie ma w B
        ^ -ksor(alternatywa wykluczajaca) wyklucza wspolne wartosci
"""

a = {1 ,4 , -2, 5, 5}  # to jest zbior, a elementy musza byc unikalne to znaczy, ze jedna '5' zostanie usunieta
b = [1, 4, 20, 50]			# to jest lista
c = {5, 10, 20, 5, 7, 9}

a.add(7)	# dodajemy wartosc do zbioru

print(set(b))   #usuwa duplikaty zmienia nam dana liste na zbior

print(a&c) # daje nam wspolne wartosci z obu zbiorow

print(a|b|c) # daje nam wszystkie elementy ze zbiorow

print(a-b) # wszystkie elementy co sa w a, a nie ma w b

print(a^b)

print(b^a)

print(a.issubset(b))

# a.discard(1) #usuwa nam elementy w zbiorze, nie wyrzuci error jesli nie ma tej wartosci w zbiorze

# a.remove(1) # usuwa nam wartosci w zbiorze, ale jesli nie ma danej wartosci to wyrzuci error

# print(b.issubset(a)) # sprawdza czy ktores elementy zbioru a sa podzbiorem zbioru b


# print(a-b)
# print(b-a)