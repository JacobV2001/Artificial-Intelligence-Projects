import Backtracking as BT
import HillClimbing as HC
import SimulatedAnnealing as SA

def check_initial_puzzle(puzzle):

    # check rows for duplicates
    for row in range(9):
        seen = set() # create set to hold numbers
        for col in range(9):
            num = puzzle[row][col]
            if num != 0: 
                if num in seen:
                    return True  # duplicate found
                seen.add(num)
    
    # check columns for duplicates
    for col in range(9):
        seen = set() 
        for row in range(9):
            num = puzzle[row][col]
            if num != 0: # default val is 0
                if num in seen:
                    return True  # duplicate found
                seen.add(num)
    
    # check 3x3 boxes 
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = puzzle[start_row + i][start_col + j]
                    if num != 0:
                        if num in seen:
                            return True  # duplicate found
                        seen.add(num)
    
    # initial puzzle valid
    return False

puzzle_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

puzzle_2 = [
    [0, 0, 0, 1, 0, 2, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 8, 0, 0, 0, 9, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [2, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 9, 0, 0, 0, 8, 0, 5],
    [0, 7, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 3, 0, 4, 0, 0, 0]
]

puzzle_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def run(puzzle):
    if check_initial_puzzle(puzzle):
        print("Puzzle Invaild")
        exit()
    else:
        SA.SA_run(puzzle)
        HC.HC_run(puzzle)    
        BT.BT_run(puzzle)

if __name__ == "__main__":
    run(puzzle_2)