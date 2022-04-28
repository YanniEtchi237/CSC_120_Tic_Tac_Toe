from operator import truediv


board = [["_","_","_"],["_","_","_"],["_","_","_"]]

turn = "x"

def print_board():
    print("printing board....")
    for i in board:
        print(i)


print_board()
def play(turn):
    print("player "+turn+" turn to play")
    row = int(input("enter row to play:"))   
    column = int(input("enter column to play:"))

    if(board[row][column] =="_"):
        board[row][column] = turn

    print_board()

    return "o"  if (turn == "x")  else "x"

def check_if_board_full():
    for i in board:
        for j in i:
            if "_" in j:
               return False
            else:
                break   
    return True  


def check_for_win (game) :
    for row in game: # rows 
        if row[0] == row[1] == row [2] != "_":
            
            return True


    for i in range (0, len(game)): # cols
        if game[0][i] == game [1][i] == game [2] [i] != "_": 
            
            return True

    if game[0][0]== game [1][1] == game [2][2] != "_":
         
         return True
    if game[0][2] == game [1][1] == game [2][0] != "_":
         return True
    
    return False




while (not check_if_board_full()):
    
    if(check_for_win(board)):
        print("player"+turn +" is the winner")
        break
    turn = play(turn)


