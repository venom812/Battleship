print("WELCOME TO BATLESHIP GAME!!))")
print("\n")
print("XXXXXXXX")

#The length of aplphabe sets demisions of board
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #, 'K', 'L', 'M', 'N'] 

#First numbers are ship sizes, second numbers are number of ships 
fleet_list = [[4, 1], [3, 2], [2, 3], [1, 4]]  

ship_clases = {4: "Battleship", 3: "Cruiser", 2: "Destroyer", 1: "Torpedo boat"}

class Board:

    def __init__(self, player_name):
        self.name = player_name
        self.matrix = generate_empty_board_matrix()
    
    def __repr__(self) -> str:
        return self.name
    
    def show(self):

        string = "\n"*2
        for row in self.matrix:
            for cell in row:
                string += cell + " "*2
            string += "\n"*2
        print(string)

    def shot(self, coord):
        
        x, y = coordinates_from_string(coord)

        self.matrix[y][x] = 'X'



    def place_ship(self, begining_coord, size, direction):
        x, y = coordinates_from_string(begining_coord)

        for i in range(size)[1:]:
            print(i)



def generate_empty_board_matrix():
    
    matrix = ["  "]
    matrix.extend(alphabet)
    matrix = [matrix] 
    
    for i in range(len(alphabet)):
        
        if (i+1) < 10: 
            row = [" " + str(i+1)]
        else: 
            row = [str(i+1)]

        for i in range(len(alphabet)):
            row += "~"   
        matrix.append(row)
    
    return matrix

def coordinates_from_string(string):
        string = string.strip().upper()
        x = alphabet.index(string[0]) + 1
        y = int(string[1:])
        return x, y

#board_1 = Board(input("Please input First Player name: "))

board_1 = Board("Anton")

board_1.shot(" d10   ")

board_1.place_ship("A1",4,"S")


board_1.show()

#board_2 = Board(input("Please input Second Player name: "))



input('Press any key to exit')