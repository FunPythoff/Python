
'''
podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:
r+ - do czytania i pisania

file.read file.write

w+ - do pisania i czytania
różni sie tym, że usunie zawartość istniejącego pliku
lub stworzy plik gdy go nie było

a+ - "wieczny tryb" dopisywania i przy okazji czytania
UWAGA! wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istniał - stworzy go

'''
############################################################

'''
try:
    file = open("Pierwszy_otwarty_plik.txt", "w") ### robimy obiekt file = aby "uchwycić" ten plik i miec mozliwosc odwolania sie do niego,
                                                        # wykonywania jakis operacji, np zapisac cos w nim

    file.write("To pierwszy test napisany w innym pliku")
    
    print(0/0)
    file.write("To pierwszy test napisany w innym pliku")
finally:
    
    file.close()  # plik musimy zawsze zamknac aby zapisac dana operacje na nim i aby nie zajmowac miejsca w pamieci, bo jest wciaz otwarty.

'''


with open("Pierwszy_otwarty_plik.txt", "w", encoding="UTF-8") as file:
    
    file.tell() # mowi w ktorym miejscu jest wskaznik
    file.tell()
    
    # print(zawartosc_pliku)
    # for line in zawartosc_pliku:
    #     print(line)


# with open("Pierwszy_otwarty_plik.txt", "w+", encoding="UTF-8") as file:
    
#     print(file.readlines())





