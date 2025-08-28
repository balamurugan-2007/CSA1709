N = 8

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq(board, row=0):
    if row == N:
        print_solution(board)
        return True
    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_nq(board, row + 1) or res
            board[row][col] = 0
    return res

board = [[0]*N for _ in range(N)]
solve_nq(board)
