#### Zadanie: Stwórz klase która bedzie reprezentowała rakiete, zastanów sie jaka ta rakieta jest
#             jakie powinna miec atrubyty i metody. Potem stworz 5 instancji(klas) rakiet o startowej
#             wysokosci 0. Porusz wszystkie rakiety do gory losowo. Wypisz wszystkie wysokosci rakiet.

from math import sqrt
from random import randint

class Rocket:
    def __init__(self, x = 0):
        self.altitude = 0
        self.speed = 2
        self.x = x

    def move_up(self):
        '''Tutaj piszemy co ta funckja robi, a potem wyswietla nam sie odnosnik z informacja
        podczas kiedy chcemy uzyc tej funkcji
        '''
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest na wysokości: " + str(self.altitude)
    

class RocketBoard:
    def __init__(self,rocketAmount=0, rocketMoves = 0):
        """ Podaj liczbe rakiet na planszy, a nastepnie ile razy maja isc do gory"""
        self.rockets = [Rocket() for _ in range(rocketAmount)]   #Robimy ilosc rakiet o zadana wartosc z rocketAmount

        for _ in range(rocketMoves):                     #Poruszamy rakiety ilosc razy z (rocketMoves) o zadana wartosc self.speed
            rocketIndexToMove = randint(0,len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].move_up() 

        for rocket in self.rockets:                  #Wyrazenie pozwalajace nam na wyprintowanie wyniku,
            print(rocket)                              # gdzie jaka rakieta poruszyla sie do gory.

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].x = value
    
    def get_amount_of_rockets(self):            #Metoda dzieki ktorej poznamy ilosc rakiet na planszy, jest bardziej czytelna
        return len(self.rockets)
    """ Moge uzyc get_amount_of_rocket, ale moge tez uzyc dunderscore (__len__) 
    """
    def __len__(self) -> int:                   # to tez metoda dzieki ktorej poznamy ilosc rakiet, ale odwolujac sie do len, 
        return self.get_amount_of_rockets()     #nie bardzo nam to mowi czego "dlugosc chcemy"



    @staticmethod                                            #metoda statyczna nie odwoluje sie do selfa czyli nie odwolamy sie do 
    def get_distance(rocket1, rocket2):                      # innych rakiet w planszy, tylko do zadanych przez nas argumentow
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)

# for rocket in range(5):
#     rocket = Rocket()
#     print("Pozycja poczatkowa rakiet to:", rocket.altitude, "a teraz pozycja rakiet to:", rocket.move_up())

# for rocket in rockets:
#     finishPos = rocket.altitude + randint(0,10)
#     print("Poczatkowa pozytcja rakiety to:", rocket.altitude, "a teraz pozycja rakiety to:", finishPos)
    

    

'''
print(rockets[0].move_up())
print(rockets[1].move_up())
print(rockets[2].move_up())
print(rockets[3].move_up())
print(rockets[4].move_up())
'''