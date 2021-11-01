import Board as bd
import time
import os
import platform
#board_1 = Board(input("Please input First Player name: "))

# Defining clear() function using lambdas after requesting OS
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')


print("WELCOME TO BATLESHIP TERMINAL GAME!!")
print("\n")
time.sleep(3)
clear()

print("\n")
board_1 = bd.Board(input("Please input name of the first player: "))
print("\n")
board_2 = bd.Board(input("Please input name of the second player: "))
print("\n")
time.sleep(3)
clear()

# print("\n")
# print("OK. Allow the first player " + board_1.player_name + " to secretly place his fleet. Try not to peek)")
# board_1.show()
board_1.place_fleet()


input('Press any key to exit')