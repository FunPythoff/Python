
from enum import IntEnum
import math

def dzielenie(a, b):
    if (b == 0):
        return
    return (a / b)

def pole_prostokata(a, b):
    return (a * b)

def pole_kwadratu(a):
    return (a * a)

def pole_kola(r):
    return (math.pi * 2 * r)

def pole_rombu(a, h):
    return (a * h)


Menu_figury = IntEnum('Math_choose', {'Prostokat': 1, 'Kwadrat': 2, 'Kolo': 3, 'Romb': 4})

print(list(Menu_figury))

choose = int(input("""Wybierz czego pole chcialbys obliczyc:
1 - Prostokat
2 - Kwadrat
3 - Kolo
4 - Romb
Twój wybor: """))

if choose == (Menu_figury.Prostokat):
    a = float(input("Podaj 1 bok prostokata: "))
    b = float(input("Podaj 2 bok prostokata: "))
    print(Figury.pole_prostokata(a,b))

if choose == (Menu_figury.Kwadrat):
    a = float(input("Podaj bok kwadratu: "))  
    print(Figury.pole_kwadratu(a))

if choose == (Menu_figury.Kolo):
    r = float(input("Podaj promien kola: "))
    print(Figury.pole_kola(r))

if choose == (Menu_figury.Romb):
    a = float(input("Podaj bok rombu: "))
    h = float(input("Podaj wysokosc rombu: "))
    print(Figury.pole_rombu(a,h))
    