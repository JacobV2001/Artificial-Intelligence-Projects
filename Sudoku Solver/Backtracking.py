def BT_is_valid(puzzle, row, col, num):

    # checks for conflicts in rows
    for i in range(9):
        if puzzle[row][i] == num:
            return False # conflict in rows
        
    # checks for conflicts in columns
    for i in range(9):
        if puzzle[i][col] == num:
            return False # conflict in column
        
    # checks for conflict in corresponding 3x3
    start_row, start_col = 3 * (row//3), 3 * (col//3)
    for i in range(3):
        for j in range(3):
            if puzzle[i+start_row][j+start_col] == num:
                return False # conflict in 3x3
            
    return True # return true if no conflict


def BT_find_empty_location(puzzle):

    # iterate through the puzzle to find any empty value (0)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0: 
                return (i, j) # return row, col of empty value
    return None

def BT_solve_sudoku(puzzle):

    # get empty location if one is present
    empty_location = BT_find_empty_location(puzzle)

    # puzzle solved if no empty locations
    if not empty_location: 
        return True
    
    # grab the row and column from the empty location found
    row, col = empty_location
    
    for num in range(1, 10):
        
        if BT_is_valid(puzzle, row, col, num):
            puzzle[row][col] = num

            # recursively call the solve sudoku function
            if BT_solve_sudoku(puzzle):
                return True # if no more empty cells
            
            puzzle[row][col] = 0 # reset back to 0
        
    return False # puzzle could not be solved

def BT_print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) for num in row ))

def BT_run(puzzle):
    if BT_solve_sudoku(puzzle):
        print('Sudoku Puzzle Solved With Backtracking')
        BT_print_puzzle(puzzle)
    else:
        print('No Solution with Backtracking.')