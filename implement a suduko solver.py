def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_safe(board, row, col, num):
    # Check if the number is not in the row
    if num in board[row]:
        return False
    
    # Check if the number is not in the column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is not in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    
    if not empty_location:
        return True  # No empty space means the puzzle is solved
    
    row, col = empty_location
    
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack
    
    return False

def input_sudoku():
    board = []
    print("Enter the Sudoku grid row by row (use 0 for empty cells):")
    for i in range(9):
        row = list(map(int, input(f"Enter row {i+1}: ").strip().split()))
        board.append(row)
    return board

if __name__ == "__main__":
    board = input_sudoku()
    print("\nOriginal Sudoku puzzle:")
    print_board(board)
    
    if solve_sudoku(board):
        print("\nSolved Sudoku puzzle:")
        print_board(board)
    else:
        print("No solution exists.") 