def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  
            return True
        if all([board[j][i] == player for j in range(3)]): 
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]): 
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    for move in range(9):
        print_board(board)
        row = int(input(f"Player {players[turn%2]} enter row (0-2): "))
        col = int(input(f"Player {players[turn%2]} enter column (0-2): "))
        if board[row][col] == " ":
            board[row][col] = players[turn%2]
            if check_winner(board, players[turn%2]):
                print_board(board)
                print(f"Player {players[turn%2]} wins!")
                return
            turn += 1
        else:
            print("Cell already occupied. Try again.")
    
    print_board(board)
    print("It's a draw!")
tic_tac_toe()
