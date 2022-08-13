import Board as bd
import time 
import random

# Welcome section
print("\n WELCOME TO BATLESHIP TERMINAL GAME!!!:):)")
time.sleep(3)
bd.clear()

# Input players names
player_1_name = input("\n Please input name of the PLAYER 1: ")
player_2_name = input("\n Please input name of the PLAYER 2: ") #If You want to play with computer input 0
board_1 = bd.Board(player_1_name, "PLAYER 1")

if player_2_name == '0': #If Player 2 is COMPUTER
    board_2 = bd.Board("HAL 9000", "COMPUTER")
    print("\n You'e going to play against computer))")
else:
    board_2 = bd.Board(player_2_name, "PLAYER 2")
time.sleep(3)

def play_game():

    bd.clear()

    board_1.reset_for_new_game()
    board_2.reset_for_new_game()

    # Place fleets by users
    board_1.place_fleet()
    bd.clear()
    time.sleep(1)

    if player_2_name == '0': #If Player 2 is COMPUTER:
        board_2.place_fleet_random()
    else:
        print("\n OK. Let's do the same for the second player")
        board_2.place_fleet()
        bd.clear()
        time.sleep(2)

    print("\n OK. WE ARE READY FOR BATLLESHIP!!")
    time.sleep(4)
    bd.clear()
    
    #show_pair_of_boards(board_1, board_2)
    
    #Determining whose shot is the first
    if board_1.won_prev_game:
        print("\n PLAYER 1 won previos game. So his shot will be the first.")
        shot_player_id = board_1.player_id

    elif board_2.won_prev_game:
        print("\n PLAYER 2 won previos game. So his shot will be the first.")
        shot_player_id = board_2.player_id

    else:
        print("\n This is initial battle.\n\n So, whose move is the first will be determined by chance.")
        
        if random.getrandbits(1) == 1:
            shot_player_id = board_1.player_id
        else:
            shot_player_id = board_2.player_id

        print("\n " + shot_player_id + "! Today is your day. Shot first.")
    time.sleep(7)
    bd.clear()
    #show_pair_of_boards(board_1, board_2)
    
    while board_1.fleet_array and board_2.fleet_array:
        
        if shot_player_id == board_1.player_id:
            board_2.show()
            if not board_2.shot_at(shot_player_id):
                shot_player_id = board_2.player_id
        else:
            board_1.show()
            if not board_1.shot_at(shot_player_id):
                shot_player_id = board_1.player_id
        #bd.clear()
        #show_pair_of_boards(board_1, board_2)
        time.sleep(5)
        bd.clear()

    bd.show_pair_of_boards(board_1, board_2)
    print("\n  " + shot_player_id + " WON THIS BATTLE!!")
    time.sleep(12)
    
    if board_1.player_id == shot_player_id:
        board_1.wins_number += 1
        board_1.won_prev_game = True
    else:
        board_2.wins_number += 1
        board_2.won_prev_game = True

    bd.clear()
    print("\n  " + board_1.player_id + " won in games: " + str(board_1.wins_number))
    print("\n  " + board_2.player_id + " won in games: " + str(board_2.wins_number))                          
    input('\n Press ENTER begin new game')
    return True

while play_game():
    pass

