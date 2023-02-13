from RocketGameSettings import RocketBoard

board = RocketBoard(4, 3)



board[0] = 2
board[1] = 4
rocketDistance = RocketBoard.get_distance(board[0],board[1])

print(board.get_amount_of_rockets())
print(rocketDistance)
print(len(board))

'''
rocket = Rocket(x=0, speed=2)
rocket2 = Rocket(x=2, speed=4)
rocket.move_up()
rocket2.move_up()

print(rocket)
print(rocket2)


print(rocket.get_distance(rocket2))
'''