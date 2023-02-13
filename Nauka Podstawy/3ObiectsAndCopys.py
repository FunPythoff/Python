

'''
Obiekt to zmienna, ktora ma wiecej mozliwosci,
mozna wywolac na nim "funkcje"
moze miec wiecej niz 1 wartosc

obiekty immutable : bool, float, int, tuple, str

immutable - niezmienne
mutable - zmienne

Znak "=" miejsce wskazywania na nowy adres, na inny obiekt 

'''

'''
a = 4

listSample = [1,5,6,10]
print(id(listSample))

a = 4
print(id(a))
b = a
b = 7

# print(a)
# print(b)

def append_element_to_list(lista,element):
    lista.append(element)
    listSample = a
    print(id(listSample))
    return lista

append_element_to_list(listSample, 5)
print(id(listSample))
print(id(a))
'''

'''
### copy - plytka (kopiujemy dana liste,zbior itp., ale nie kopiujemy jej zawartosci i mozemy ja zmienic)
### copy - glebokie(deep) (kopiejemy dana liste wraz z zawartoscia, ktorej nie mozna zmienic)

import copy


def evil_function(lista_do_zniszczenia):
    lista_do_zniszczenia[0] = 3
    print(lista_do_zniszczenia)

lista = [1, 5, 3, 7, 8]
### 3 rozne sposoby na kopiowanie plytkie
# evil_function(list(lista))
# evil_function(lista[0:3])
# evil_function(lista.copy()))

###sposob na kopiowanie glebokie
evil_function(copy.deepcopy(lista))

print(lista)

'''

### Funkcje anonimowe(funkcja bez nazwy) - nie maja nazwy(korzystamy ze slowka lambda)
#                uzywamy kiedy chcemy cos szybko zrobic

def podwoj(x):
    return (x * 2)

def filtruj(x):
    if (x % 2) != 0:
        return x


lista = [1,2,3,4,5,6]
listaprzefitrowana = [              # wyrazenie listowe
                    x * 2               # co robimy
                    for x in lista  # gdzie robimy
                    if x % 2 != 0   # warunek jaki ma spelnic
                    ]

filtred_list = list(filter(lambda x: x % 2 == 0, lista)) # tak piszemy jesli odwolanie jest do lambdy
filtred_list2 = list(filter(filtruj, lista))   # tak piszemy jesli odwolanie jest do funkcji

print(filtred_list)
print(filtred_list2)
print(listaprzefitrowana)

