import Board as bd
import time 
import random

# Welcome section
print("\n")
print(" WELCOME TO BATLESHIP TERMINAL GAME!!")
time.sleep(3)
bd.clear()

# Input players names
print("\n")
player_1_name = input(" Please input name of the PLAYER 1: ")
print("\n")
player_2_name = input(" Please input name of the PLAYER 2: ")
#print("\n")
board_1 = bd.Board(player_1_name, "PLAYER 1")
board_2 = bd.Board(player_2_name, "PLAYER 2")
time.sleep(3)

def play_game():

    bd.clear()

    board_1.reset_for_new_game()
    board_2.reset_for_new_game()

    # Place fleets by users
    board_1.place_fleet()
    #board_1.place_fleet_random()
    bd.clear()
    time.sleep(1)
    print("\n OK. Let's do the same for the second player")
    board_2.place_fleet()
    #board_2.place_fleet_random()
    bd.clear()
    # print(board_1.player_name)
    #print(board_1.fleet_array)
    # print(board_2.player_name)
    #print(board_2.fleet_array)
    time.sleep(2)

    print("\n")
    print(" OK. WE ARE READY FOR BATLLESHIP!!")
    print("\n")
    time.sleep(4)
    bd.clear()
    
    bd.show_pair_of_boards(board_1, board_2)
    
    #Determining whose shot is the first
    if board_1.won_prev_game:
        print("\n PLAYER 1 won previos game. So his shot will be the first.")
        shot_player_id = board_1.player_id

    elif board_2.won_prev_game:
        print("\n PLAYER 2 won previos game. So his shot will be the first.")
        shot_player_id = board_2.player_id

    else:
        print("\n This is initial battle!.\n\n Whose move is the first will be determined by chance.\n\n")
        
        if random.getrandbits(1) == 1:
            shot_player_id = board_1.player_id
        else:
            shot_player_id = board_2.player_id

        print(" " + shot_player_id + "! Today is your day. Shot first.\n\n")
    time.sleep(7)
    bd.clear()
    bd.show_pair_of_boards(board_1, board_2)
    
    while board_1.fleet_array and board_2.fleet_array:
        if shot_player_id == board_1.player_id:
            if not board_2.shot_at(shot_player_id):
                shot_player_id = board_2.player_id
        else:
            if not board_1.shot_at(shot_player_id):
                shot_player_id = board_1.player_id
        bd.clear()
        bd.show_pair_of_boards(board_1, board_2)

    print("\n  " + shot_player_id + " WON THIS BATTLE!!")
    time.sleep(7)
    
    if board_1.player_id == shot_player_id:
        board_1.wins_number += 1
        board_1.won_prev_game = True
    else:
        board_2.wins_number += 1
        board_2.won_prev_game = True

    bd.clear()
    print("\n\n  " + board_1.player_id + " won in games: " + str(board_1.wins_number))
    print("\n  " + board_2.player_id + " won in games: " + str(board_2.wins_number))                          
    input('\n Press ENTER begin new game')
    return True

while play_game():
    pass

    










