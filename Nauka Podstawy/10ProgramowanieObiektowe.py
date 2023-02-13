
'''
Programowanie obiektowe -  to jeden ze sposobów programowania. Używany jest najczęściej w dużych,
                            skomplikowanych programach w celu ułatwienia pisania/używania kodu w tym
                            samym czasie pracy kilku programistów. Opiera się na obiektach.

Każda zmienna w Pythonie jest obiektem np.

x = 0
print(type(x))                                # typem tej zmiennej jest klasa int.  <class 'int'>

Klasa - to forma, szablon do tworzenia obiektów.

OOP - Object Oriented Programming (Programowanie zorientowane wokół obiektów)

OBIEKT - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze soba powiazanych do dalszego łatwiejszego ponownego uzycia

KLASY - foremki (szablony) do tworzenia egzemplarzy obieków 

Atrybut - cecha opisujaca obiekt
Metoda - funkcja, która operuje na obiekcie

INSTANCJA KLASY - instance z ang. egzemplarz to obiekt ,który wyszedł z foremki (klasy)

self - z ang. "ja", w innych jezykach "this"

__init__ - inicjalizacja(konstrukcja), czyli ustawienie startowych wartosci dla atrybutow

docstring - DOCument string. Jest to komentarz ktory dajemy najczesciej pod klasa albo funkcja opisujacy co robi dana funkcja
            Uzywamy jej w ten sposob(( """ i tutaj piszemy co robi  )
                                     ( """                          )

Metoda typu "d under" - double underscore czyli np. __init__, __str__
'''

class User:

    def __init__(self, name, age):
      self.name = name
      self.age = age

    def print_data_users(self):
        print("Wiek", self.age, self.name)

user1 = User("Michal", 30)
user2 = User("Arek", 40)

user1.print_data_users()
user2.print_data_users()



















'''
userLists[0].age = 20
userLists[0].name = "michal"

userLists[1].age = 30
userLists[1].name = "arek"

userLists[2].age = 40
userLists[2].name = "gosia"

userLists[0].print_age()
userLists[1].print_age()
userLists[2].print_age()
'''


