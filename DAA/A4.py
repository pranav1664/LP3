#  Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final n-queen‘s matrix.

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True  
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True
            
            board[i][col] = 0

    return False

def generate_n_queens_with_first_queen(n, first_queen_position):
    board = [[0 for _ in range(n)] for _ in range(n)]

    row, col = first_queen_position
    board[row][col] = 1

    if solve_n_queens_util(board, col + 1, n):
        return board
    else:
        return None

n = 4
first_queen_position = (0, 1)
result = generate_n_queens_with_first_queen(n, first_queen_position)
if result:
    for row in result:
        print(row)
else:
    print("No solution exists")