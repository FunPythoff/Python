
'''
yield - z ang. dostarczyc, wydac z siebie

'''


'''
def even_numbers_generator():                       # To jest funkcja generujaca, ktora pozwala nam zwrocic w tym przypadku wiele razy 
                                                    #liczby parzyste miedzy 0-48
    for element in range(50):
        if (element % 2 == 0):
            yield element

x = even_numbers_generator()

print(list(x))
'''
'''
even_numbers_generator_expression = (x                              #To jest wyrazenie generujace, ktore jak juz raz wygenerujemy to potem zwroci nam pusta liste, bo juz nie ma co generowac.
                                                                for x in range(50)
                                                                if x % 2 == 0
                                                                )

print(list(even_numbers_generator_expression))
print(list(even_numbers_generator_expression))
'''





