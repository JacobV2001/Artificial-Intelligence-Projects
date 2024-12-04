import random
import copy
from collections import Counter

# 9x9 grid to keep track of the number of conflicts
HC_conflicts_puzzle = [[0 for _ in range(9)] for _ in range(9)]

def HC_generate_initial_solution(puzzle):
    initial_solution = copy.deepcopy(puzzle) # create a copy of puzzle

    for i in range(9):
        occurences = Counter(initial_solution[i]) # count number of occurances in row
        for j in range(9):
            if initial_solution[i][j] == 0:

                # number is avaliable if it has not appeared in the row
                avaliable_numbers = [num for num in range(1, 10) if occurences]
                
                # insert number into solution and update occaurances
                num = random.choice(avaliable_numbers)
                initial_solution[i][j] = num
                occurences[num] += 1

    return initial_solution 
    
def HC_count_conficts(puzzle):
    # create grid to hold conflicts
    conflicts = [[0 for _ in range(9)] for _ in range(9)]

    # count for conflicts in row
    for row in range(9):
        # count occurences for each number in current row
        row_counts = Counter(puzzle[row])
        # check if each number in the row appears more than once (except 0)
        for num, count in row_counts.items():
            if num != 0 and count > 1:
                # if appears more than once, increase conflict count
                for col in range(9):
                    if puzzle[row][col] == num:
                        conflicts[row][col] += (count - 1)

    # count for conflicts in cols
    for col in range(9):
        # count occurences for each number in current col
        col_counts = Counter(puzzle[row][col] for row in range(9))
        # check if each number in the col appears more than once
        for num, count in col_counts.items():
            if num != 0 and count > 1:
                # if number appears more than once, incease counter
                for row in range(9):
                    if puzzle[row][col] == num:
                        conflicts[row][col] += (count - 1)

    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            # for counting occurances of numbers
            block_counts = Counter(
                puzzle[row][col]
                for row in range(start_row, start_row + 3)
                for col in range(start_col, start_col + 3)
            )
            # check if numbers appear more than once
            for num, count in block_counts.items():
                if num != 0 and count > 1:
                    # if num appears more than once, increase counter
                    for row in range(start_row, start_row + 3):
                        for col in range(start_col, start_col + 3):
                            if puzzle[row][col] == num:
                                conflicts[row][col] += (count - 1)
    return conflicts

def HC_hill_climbing(puzzle):
    initial_puzzle = HC_generate_initial_solution(puzzle) # gen solution
    max_iterations = 500000 # number of iterations to avoid inf loop
    current_puzzle = copy.deepcopy(initial_puzzle) # create a copy of puzzle

    for iteration in range(max_iterations):
        conflicts_puzzle = HC_count_conficts(current_puzzle) # count conflicts
        max_conflicts = max(max(row) for row in conflicts_puzzle) # find max conflicts on grid

        if max_conflicts == 0:
            return current_puzzle #solution
        
        # get cells with max # of conflicts
        max_conflicts_cells = [(i, j) for i in range(9) for j in range(9) if conflicts_puzzle[i][j] == max_conflicts]

        if len(max_conflicts_cells) < 2: continue # only one cell with max conflicts skip swapping

        # randomly select 2 cells with highest conflicts to swap
        first_cell, second_cell = random.sample(max_conflicts_cells, 2)
        row1, col1 = first_cell
        row2, col2 = second_cell
        current_puzzle[row1][col1], current_puzzle[row2][col2] = current_puzzle[row2][col2], current_puzzle[row1][col1]

        if iteration % 2500 == 0: # random restart to escape local minima
            current_puzzle = copy.deepcopy(HC_generate_initial_solution(puzzle))

    return None # no solution found within max iterations


def HC_print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) for num in row ))

def HC_run(puzzle):
    solved_puzzle = HC_hill_climbing(puzzle)

    if solved_puzzle is not None: return True
    else: return False

"""    if solved_puzzle is not None:
        print("Solved Puzzle With Hill Climbing")
        HC_print_puzzle(solved_puzzle)
    else:
        print("Failed to solve with Hill Climbing.")"""