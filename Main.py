import Board as bd
import time

print("\n")
print(" WELCOME TO BATLESHIP TERMINAL GAME!!")
time.sleep(3)
bd.clear()

print("\n")
board_1 = bd.Board(input(" Please input name of the first player: "))
print("\n")
board_2 = bd.Board(input(" Please input name of the second player: "))
print("\n")
time.sleep(3)
bd.clear()

#board_1.place_fleet()
board_1.place_fleet_random()
bd.clear()
time.sleep(3)
print(" OK. Let's do the same for the second player")
#board_2.place_fleet()
board_2.place_fleet_random()

bd.clear()
time.sleep(3)

print(board_1.player_name)
print(board_1.fleet_array)
print(board_2.player_name)
print(board_2.fleet_array)
print("\n")
print(" OK. Let's PLAY!!")
print("\n")
#bd.clear()
time.sleep(3)
bd.show_pair_of_boards(board_1, board_2)
input(' Press ENTER to continue')




