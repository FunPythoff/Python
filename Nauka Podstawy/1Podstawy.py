



#### 1. Assignment operators - Operatory przypisania ####
'''
x = 5
print(x + 5)
print(x - 5)
print(x * 5)
print(x / 5)
print(x ** 5)
print(x // 5)
print(12 % x)
'''




#### 2. Comparision operators - Operatory porownania ####
'''
print(5 > 4)      # >   - wieksze niz
print(6 < 6)      # <   - mniejsze niz
print(5 == 5)     # ==  - rowne
print(5 != 4)     # !=  - nierowne
print(3 >= 5)     # >=  - wieksze lub rowne
print(2 <= 5)     # <=  - mniejsze lub rowne


# Przyklad zastosowania:
# a = input()
# print(a == 5)           #Jesli sprawdzimy czy a == 5 wyjdzie nam false, poniewaz trzeba zrobić rzutowanie int na zmienna 'a'.

a = int(input("Wprowadź cyfrę: "))
b = int(input("Wprowadź drugą cyfrę: "))  
print(a == 5)
print(b >= 6)

'''




#### 3. FUNKCJE ####
'''
import math

print(math.sqrt(3))

imie = ("micHal")


print(imie.capitalize())
print(imie.upper())
print(imie.lower())
print(imie)         
'''




#### 4. POBIERANIE I FORMATOWANIE DANYCH ####
'''
a = input()  
b = input() 

print(a + b)   #Komp traktuje to co wprowadzimy w input() jako ciag znakow wiec jesli a=5 + b=10 to nie bedzie 15 tylko "510".
               #Jeśli chcemy aby to co wprowadzamy w input było liczbą, musimy zrobić "rzutowanie"

a = int(input())
b = int(input())  # W ten sposób RZUTUJEMY intiger na input czyli l. calkowite ale mozemy tez float czyli l.zmiennoprzecinkowe

print(a + b)

print("Witaj w kalkulatorze dodawania !")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Wynik dodawania" + " " + str(a) + " do " + str(b) + " to " + str(a + b))  #Wersja z plusami
print("Wynik dodawania", a, "do", b, "to", (a + b))  #Wersja z przecinkami (lepsza)
'''



#### 5. PETLE WHILE I FOR ####

'''
number = -100

while number <=0:
    print(number)
    number +=1
'''
'''
x = int(input())        #Od jakiej wartosci ma zaczac liczenie "0 przy + i -, input() przy * i /"

q = 0                                   # Od jakiej wartosci ma zaczac liczenie petli
while q < 3:                            # Jak wiele razy uzytkownik moze dodawać do siebie liczby
    wynikuzytkownika = int(input("Podaj liczbę: "))    # Tutaj uzytkownik wpisuje liczby
    x += wynikuzytkownika                          # Tu wpisujemy co ma kalkulator robić
    q += 1                              # Musimy wskazac czynnik dla ktorego petla bedzie sie konczyc czyli od 0 do ... (bez 0)

print("Wynik dodawania to:", x)
'''

# Cwiczenie numer 1: Wypisz liczby podzielne przez 6 uzywajac "while"
'''
liczba = 0

while liczba <= 150:
    
    if liczba % 5 == 0:
        print(liczba, "ta liczba jest podzielna przez 5")
    else:
        print(liczba)
    liczba += 1
'''

 # Cwiczenie numer 2: Wypisz liczby od 1 do 200 ktore sa podzielne przez 5, a nie sa podzielne przez 7, uzywajac funkcji for.

'''
for a in range (1, 201):
    if (a % 5 == 0) and (a % 7 == 0):
        print(a, "jest podzielne przez 5 i 7")
'''





#### 6. BREAK I CONTINUE ####
'''
ZADANIE :         Napisz program, który doda 3 parzyste liczby dodatnie podane przez użytkownika.

wynik = 0
y = 0

while y < 3:
    x = int(input("Podaj dodatnia, parzysta liczbe: "))

    if (x < 0):
        print("Musisz podac dodatnia liczbe.")
        continue
    elif (x % 2 != 0):
        print("Musisz podac parzysta liczbe.")
        continue
    else:
        wynik += x
        y += 1

print("Wynik dodawania to: ", wynik)

 ####### LUB NA ODWROT VVVVVVV

wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj parzystą, dodatnią liczbę:"))
    if (x > 0 and x % 2 == 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia parzysta, zapytam się o liczbę ponownie")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1
'''




#### 7. ConditionalStatements - Instrukcje Warunkowe ####
'''
if - jesli, prawda 
to wykonaj to .... 
jesli co innego prawda
to wykonaj to ....


elif - "else if" jeśli jeszcze cos innego jest prawda to wykonaj ...
else - "a jesli cos innego niz prawda to wykonaj ..."

a = 2
b = 1
if (a > b):     # Po "if,elif,else" stawiamy : inaczej nie bedzie nam dzialalo
    print("Tak a jest wieksze od b")    #Musimy zrobic indended block czyli wciecie blokowe
elif (b > a):
    print("Tak b jest wieksze od a")
else:
    print("a jest rowne b")


print("Witaj w prostym kalkulatorze")

ChooseFunction = input("Wybierz 1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie, 5-potegowanie:  ")

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

if (ChooseFunction == "1"):
    print("Wynik dodawania to:", (a + b))
elif (ChooseFunction == '2'):
    print("Wynik odejmowania to:", (a - b))
elif (ChooseFunction == '3'):
    print("Wynik to:", (a * b))
elif (ChooseFunction == '4'):
    if (b == 0):
        print("Nie mozna dzielic przez 0")
    else:
        print("Wynik to:", (a / b))
elif (ChooseFunction == '5'):
    print("Wynik to:", (a ** b))
else:
    print("Wybrales zla wartosc")
'''




#### 8. Zabawa ze stringami ####
'''
name = "Michal"
surname = "Gaj"

print(name + " " + surname)

dlugiString = "    xxxxxxxxxxxxxxxxxxxxx \n\
    xxxxxxxxxxxxxxxxxxxxxx"   #ToJestKomentarzLiniowy , \n\ oznacza enter (przesuniecie o linie w dół).


longString = """    yyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyy.""" 


print(dlugiString)
print(longString)

# M  i  c  h  a  l    
# 0  1  2  3  4  5   - tak program numeruje indeksy.
#-6 -5 -4 -3 -2 -1 - tak program numeruje indeksy od konca.
#[] - za pomoca tego znaku mozna odwolac sie do indeksow czyli liter w imieniu.

print(name[4]) #Wybierz mi 4-ty element czyli "a".
print(name[0:2]) #Wybierz element 0 do 2, bez 2 czyli Mi.
print(name[-1]) #Wybierz ostatni element czyli "l".
#Mozna tez wykorzystac do sprawdzania czy ostatnia 
# litera to "l" z uzyciem "if".

print(name[1:]) #Napisz wszystkie litery oprocz pierwszej czyli ichal.
print(name[:-1]) #Napisz wszystkie litery oprocz ostatniej.
'''



#### 9. LISTY - ZADANIA I ICH TWORZENIE ####

'''
#Listy są jak zmienne, tylko że dla kilku wartości na raz, tworzymy je po prostu dodajac je 
#w klamrze [] zamiast w nawiasach zwyklych().


NamesList = ["Adam", "Kamil", "Kacper", "Melchior", "Baltazar"]
SurnamesList = ["Gaj", "Blachowicz", "Rucinski", "Obibok", "Niemy"]

for Names in NamesList:
    print(Names)

NamesList[-2] = "Marcin"   # Zamieniam wartośc z listy (Melchior) na (Marcin)
print(NamesList)

print(NamesList[2])    #Wypisuje tylko 2 miejsce z listy w tym przypadku Kacper


print("Michal" in Nameslist)   # sprawdzam czy "Michal" jest w liscie Nameslist
    
if ("Adam" in Nameslist):  #
        print("Witaj Adamie")
if ("Michal" not in Nameslist):
        print ("Michal nie jest na liscie")

# Na liczbach mozna wykonywac operacje vvvvvvvv

print (3 * Nameslist) # Wypisze wtedy liste 3 razy tak samo obok siebie

lista = [3,3,3,3]
lista.clear()
print(lista)


Na listach możemy wykonywać różne czynności takie jak:
.append()				dodaje nam wpisane wartosci do listy jako osobny element na koncu listy
.extend()				(rozszerza) nam liste o wpisane wartości już do istniejacej listy
.insert(index,wartosc)	(wstawia) nam w dane miejsce(index), wartosc ktora wpiszemy
.pop()					usuwa nam ostatni element z listy, chyba ze damy () i wprowadzimy ktory index ma usunac
.clear()				wyczysci nam wszystkie elementy z listy
.remove()				usunie nam pierwsze wystapienie wprowadzonej wartosci podanej przez nas
.sort()					(sortuje) nam dana liste domyslne rosnaco, ale aby to zmienic robimy np. lista1.sort(reverse=True)
.count()				policzy nam ile razy znajduje sie dana wartosc w liscie
.reverse()				zamienia kolejnosc danej listy to co bylo na poczatku jest na koncu
len()					(length)sprawdza nam ile elementow znajduje sie w danej liscie
max()					'wyprintuje' nam najwieksza wartosc z danej listy
min()					'wyprintuje' nam najmniejsza wartosc z danej listy
'''




#### 10. KROTKI ####
'''
KROTKA-jest to też stworzenie zmiennej na dane jak i lista, tylko że nie możemy już zmieniać wartości 
    wewnatrz. Mozemy je - sortować(.sort), liczyć(.count), max, min, len, index. 
    Tylko nie - .append(dowawać), .extend(rozszerzać), .insert(index,wartosc)(wstawiac), .pop()(usuwac),
    .clear()(czyscic), .remove()(usuwac wartosci). Uzywamy KROTEK zawsze kiedy mozemy po to aby 
    zaoszczedzic miejsce w pamieci i zbednie jej nie rezerwować dla zmieniania wartosci
    jesli wiemy ze te wartosci maja byc nie zmienne.



a = 10                  # to jest zmienna
lista1 = [1,2,3,4,5]    # to jest lista
krotka = 1,2,3,4        # tak tworzymy krotke
krotka = (1,2,3,4)      # lub tak tworzymy krotke w nawiasach()
'''


