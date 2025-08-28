import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif all(cell != " " for row in board for cell in row):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = " "
        return best

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        row = int(input("Player X enter row (0-2): "))
        col = int(input("Player X enter column (0-2): "))
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Cell occupied. Try again.")
            continue
        
        if check_winner(board) or all(cell != " " for row in board for cell in row):
            break
        
        i, j = best_move(board)
        board[i][j] = "O"
        print_board(board)
        if check_winner(board) or all(cell != " " for row in board for cell in row):
            break
    
    winner = check_winner(board)
    print_board(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

# Run the game
play_game()
