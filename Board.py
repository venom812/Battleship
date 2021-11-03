import random
import re
import os
import platform
import time 

# Defining clear() function using lambdas after requesting OS
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

# GENERAL GAME SETTINGS:
# -Board size. Length of aplphabet list below sets size of the board. From "A" to "J" board size is 10 x 10 cells
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']#, 'K', 'L', 'M', 'N'] 
# -Fleet configuration. First numbers in list below are ship sizes, second numbers are number of ships 
fleet_config = [[4, 1], [3, 2], [2, 3], [1, 4]]
#fleet_config = [[1, 1]] #test config
# -Ship class names. In dictionaries below  
ship_class_names = {4: "Battleship", 3: "Cruiser", 2: "Destroyer", 1: "Torpedo boat"}
# -Space factor. Defines the size of spaces between cells
space_factor = 2

#This Class represnts players board with all its information
class Board: 

    def __init__(self, player_name, player_id):
        self.player_name = player_name
        self.player_id = player_id
        self.array = generate_empty_board_array()
        self.size = len(self.array)
        self.fleet_array = []
        self.won_prev_game = False
        self.wins_number = 0
        self.shot_list = []
    
    def __repr__(self) -> str:
        return self.player_name

    def reset_for_new_game(self):
        self.array = generate_empty_board_array()
        self.fleet_array = []
        self.shot_list = []

    
    def show(self): #Show the board on terminal with using space factor value
        string = "\n" * space_factor + "     " + self.player_id + ": " + self.player_name + "\n" * space_factor
        for row in self.array:
            string += " " * space_factor
            for cell in row:
                string += cell + " " * space_factor
            string += "\n" * space_factor
        print(string)

    def place_ship(self, ship_size, begining_coord_and_direction, manual_input = True): #Place ship on the board
        
        x, y = coordinates_from_string(begining_coord_and_direction)

        if ship_size > 1:
            direction = ship_direction_from_string(begining_coord_and_direction)
        else:
            direction = "N"

        if direction == "S":
            x_d = 0
            y_d = 1
        elif direction == "N":
            x_d = 0
            y_d = -1
        elif direction == "W":
            x_d = -1
            y_d = 0
        elif direction == "E":
            x_d = 1
            y_d = 0
        else:
            if manual_input:
                print(" ERROR: Wrong ship direction!!")
                input(" Press any key to continue")
            return False

        ship_array = []

        for i in range(ship_size):

            if x <= self.size-1 and y <= self.size-1 and x > 0 and y > 0:
                if self.array[y][x] == u"\u2588":
                    if manual_input:
                        print(" ERROR: Intersection with existing ship!!")
                        input(" Press any key to continue")
                    return False
                else:
                    ship_array.append([x,y])
            else:
                if manual_input:
                    print(" ERROR: Coordinates go beyond the board limits!!")
                    input(" Press any key to continue")
                return False
            
            x += x_d
            y += y_d

        for i in range(ship_size):
            self.array[ship_array[i][1]][ship_array[i][0]] = u"\u2588"

        self.fleet_array.append(ship_array)
        return True

    def place_fleet(self): #Place fleet on the board manualy by player
        message = "\n Allow the " + self.player_id + " to secretly place his fleet. Try not to peek)"
        print("\n")
        print(message)
        self.show()
        for ship in fleet_config:
            
            for n in range(ship[1]):
                
                while not self.place_ship(ship[0], \
                    # Format "A8S", "A" - X coord by alphabet axis, "8" - Y coord by digit axis, "S" - ship diretion
                    str(input(" Input begining coordinates and heading of the ship: "))):
                    pass
                clear()
                print(message)
                self.show()
             
        print(" All ships of " + self.player_id + " are on positions.\n")
        input(' Press ENTER to continue')
        #print(self.fleet_array)
        self.array = generate_empty_board_array()
        return (self.fleet_array)

    def place_fleet_random(self): #Place fleet on the board randomly by computer
        for ship in fleet_config:
            
            for n in range(ship[1]):
                
                while not self.place_ship(ship[0], random.choice(alphabet) + str(random.randint(1, 10)) + random.choice(['N', 'E', 'S', 'W']), False):
                    pass
        clear()
        self.show()
             
        print(" All ships of " + self.player_id + " are on positions.\n")
        input(' Press ENTER to continue')
        self.array = generate_empty_board_array()
        return (self.fleet_array)

    def shot_at(self, shot_player_id): 
        shot_x, shot_y = coordinates_from_string(input(" " + shot_player_id + " Enter the SHOT: "))
        
        while [shot_x, shot_y] in self.shot_list:
            print("\n This cell is already shot!. Try another.\n\n")
            shot_x, shot_y = coordinates_from_string(input(" " + shot_player_id + " Enter the SHOT: "))
            
        else:
            self.shot_list.append([shot_x, shot_y])

            for ship in self.fleet_array:
                for cell_ind in range(len(ship)):
                    if ship[cell_ind] == [shot_x, shot_y]:
                        self.array[shot_y][shot_x] = 'X'
                        ship[cell_ind] = 'X'

                        if ship.count('X') == len(ship):
                            print("\n You sank a " + ship_class_names.get(len(ship)) + "!")
                            self.fleet_array.remove(ship)
                            if len(self.fleet_array) == 0:
                                self.fleet_array = False
                        else:
                            print("\n You hit the target. Finish her off!")
                        time.sleep(4)
                        return True
                    
            self.array[shot_y][shot_x] = u"\u2219"
            print("\n You missed!")
            time.sleep(2)
            return False


def generate_empty_board_array(): #Creates empty board field 2D array
    
    array = ["  "]
    array.extend(alphabet)
    array = [array] 
    
    for i in range(len(alphabet)):
        
        if (i+1) < 10: 
            row = [" " + str(i+1)]
        else: 
            row = [str(i+1)]

        for i in range(len(alphabet)):
            row += "~"   
        array.append(row)

    return array

def coordinates_from_string(string): #Read cordinateds from string in format "A8S", "A" - X coord by alphabet axis, "8" - Y coord by digit axis, "S" - ship diretion
        string = string.strip().upper()

        ints  = re.findall("\d+",string) # one or more digits
        strings = re.findall("[A-Z]+",string) # one or more uppercase  letters 

        x = alphabet.index(strings[0]) + 1
        y = int(ints[0])
        return x, y

def ship_direction_from_string(string): #Read ship direction from string in format "A8S", "A" - X coord by alphabet axis, "8" - Y coord by digit axis, "S" - ship diretion
    string = string.strip().upper()
    strings = re.findall("[A-Z]+",string) # one or more uppercase  letters
    return strings[1]

def show_pair_of_boards(brd1, brd2): #Show two players boards side by side

    string = ""
    for row_num in range(len(brd1.array)):
        string += " " * space_factor
        for cell in brd1.array[row_num]:
            string += cell + " " * space_factor
        string += " " * space_factor
        for cell in brd2.array[row_num]:
            string += cell + " " * space_factor
        string += "\n" * space_factor 

    h1 = brd1.player_id + ": " + brd1.player_name
    h2 = brd2.player_id + ": " + brd2.player_name
    head_double = " " * (string.find('A')-2) + h1 + " " * (string.find('A',string.index('A') + 1) - string.find('A')-len(h2)) + h2 + "\n"

    print("\n")
    print(head_double)
    print(string)
