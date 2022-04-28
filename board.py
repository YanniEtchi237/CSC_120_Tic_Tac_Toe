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



while (not check_if_board_full()):
    turn = play(turn)


