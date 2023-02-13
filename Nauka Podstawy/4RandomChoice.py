
'''
Random - losowy

random()                0 <= x < 1 lub [0,1)

uniform(2.5, 10.0)      2.5 <= x < 10 lub (2.50,10)

randrange(10)           z puli (0,1,2,3,4,5,6,7,8,9)
randrange(0, 15, 2)     parzyste z puli (0,2,4,...,14)

randint(0, 4) lub [0,4]
'''

'''

import random
import time
from collections import Counter


def if_hit(weapon):
    chance_hit = random.randint(0, 100)
    if chance_hit > weapon:
        return "hit"
    else:
        return  "miss"

hits = []
x = 0

while x < 100:
    x = x + 1
    hits.append(if_hit(50))


for i in range(0, 100):
    i = hits.append(if_hit(50))

dictionaryHit = Counter(hits)
print(dictionaryHit)
'''

'''
for i in range(0, 10):
    i = random.uniform(2.5,10)
    print(i)

for i in range(0, 10):
    i = random.randrange(10)
    print(i)
    
for i in range(0, 10):
    i = random.randint[1,10]
    print(i)
'''


'''

choice - zwraca losowy element
choices - zwraca liste elementow i ma wieksze mozliwosci

'''
'''
import random
from collections import Counter

movieList = ["Piraci", "Wladca", "Hobbit", "Gumisie"]
colorList = ["zolty", "zielony", "czarny", "purpurowy"]

print(random.choice(movieList))

print(Counter(random.choices(colorList, [50,30,15,3], k = 1000)))  # w tej funkcji wpisujemy liste skad chcemy wziac, potem tworzymy liste
                                                            # i procentowo mozemy opisac ile czego ma wylosowac, k = ilosc razy ile ma losowac
'''


'''
Shuffle - randomizes entire list

'''
'''

import random

cardList = ["9", "9","9", "9", 
            "10", "10", "10", "10", 
            "Jack", "Jack", "Jack", "Jack", 
            "Queen", "Queen", "Queen", "Queen", 
            "King", "King", "King", "King", 
            "Ace", "Ace", "Ace", "Ace",
            "Joker","Joker" 
            ]

random.shuffle(cardList)	# nie printujemy w tym miejscu poniewaz ta funcja dziala na oryginale i zwroci nam None

# print(cardList)
'''


### Gra Lotto - wylosuj 6 z 49 liczb.
'''
import random

def losowanie():
	list_user = []
	list_comp = []
	x = 0
	while (x < 6):
		list_user.append(random.randrange(1,49))
		list_comp.append(random.randint(1,50))
		x += 1
	return print(list_comp), print(list_user)

losowanie()
'''

### Zrób listy dla graczy które będa przechowywac wylosowane karty przez graczy.



import random

cardList = ["9", "9", "9", "9", 
            "10", "10", "10", "10", 
            "Jack", "Jack", "Jack", "Jack", 
            "Queen", "Queen", "Queen", "Queen", 
            "King", "King", "King", "King", 
            "Ace", "Ace", "Ace", "Ace",
            "Joker","Joker" 
            ]

karty_gracza1 = []
karty_gracza2 = []
rozdane_karty = []

def rozdanie(ilosc_kart):
	for i in range(1,ilosc_kart + 1):
		random.shuffle(cardList)
		karty_gracza1.append(cardList.pop())
		karty_gracza2.append(cardList.pop())
		rozdane_karty = karty_gracza1 + karty_gracza2
	return  f"{cardList}\n{karty_gracza1}\n{karty_gracza2}"


print(rozdanie(5))
















