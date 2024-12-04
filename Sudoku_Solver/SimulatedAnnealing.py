import random
import math
import statistics
import copy

# function to set perm values and crreate lists
def SA_prepare_puzzle(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                puzzle[i][j] = 1 # set to 1 if value is not empty (came in orig puzzle)

    blocks = []
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append([i + r * 3, j + c * 3])
            blocks.append(block)

    return blocks, puzzle

# calculate errors as a cost function
def SA_calculate_errors(puzzle):
    error_count = 0
    for i in range(9):
        error_count += SA_calculate_row_column_errors(i, i, puzzle)
    return error_count  # return # of errors

# check to see if duplicates exists in rows and cols
def SA_calculate_row_column_errors(row, column, puzzle):
    row_values = set() # set to store row values
    col_values = set() # set to store col values
    for i in range(9):
        row_values.add(puzzle[i][column])
        col_values.add(puzzle[row][i])
    return (9 - len(row_values)) + (9 - len(col_values))

# randomly fill block & avoid conflicsts
def SA_randomly_fill_blocks(puzzle, blocks):
    for block in blocks: # loop through 3x3 blocks
        for box in block: # loop through cells in each block
            if puzzle[box[0]][box[1]] == 0:
                # create list of values already in block
                current_values = [puzzle[i][j] for i, j in block]
                puzzle[box[0]][box[1]] = random.choice([i for i in range(1, 10) if i not in current_values])
    return puzzle

# calc the sum in each block (for which parts to modify)
def SA_sum_of_block(puzzle, block):
    return sum(puzzle[box[0]][box[1]] for box in block)  # add in value for each cell

# select 2 values in the boxes that can be swapped
def SA_select_random_boxes(fixed_puzzle, block):
    while True: # loop until boxes are found
        box1, box2 = random.sample(block, 2)
        # check to make sure both boxes can be swapped
        if fixed_puzzle[box1[0]][box1[1]] != 1 and fixed_puzzle[box2[0]][box2[1]] != 1:
            return box1, box2

# swap values
def SA_flip_boxes(puzzle, boxes):
    proposed_puzzle = copy.deepcopy(puzzle) # create a copy of the puzzle
    proposed_puzzle[boxes[0][0]][boxes[0][1]], proposed_puzzle[boxes[1][0]][boxes[1][1]] = \
        proposed_puzzle[boxes[1][0]][boxes[1][1]], proposed_puzzle[boxes[0][0]][boxes[0][1]]
    return proposed_puzzle

# this is the candidate solution to evaluate
def SA_propose_state(puzzle, fixed_puzzle, blocks):
    random_block = random.choice(blocks) # randomly choose a block to ensure randomly
    if SA_sum_of_block(fixed_puzzle, random_block) > 6:  # if sum is high, might indicate a good solution is already in place
        return puzzle, []
    # select two random boxes to flip
    boxes_to_flip = SA_select_random_boxes(fixed_puzzle, random_block)
    proposed_puzzle = SA_flip_boxes(puzzle, boxes_to_flip)
    return proposed_puzzle, boxes_to_flip

# function to decide whether to accept new state based on cost function
def SA_choose_new_state(puzzle, fixed_puzzle, blocks, sigma):
    new_puzzle, boxes_to_check = SA_propose_state(puzzle, fixed_puzzle, blocks)
    
    # if no boxes are flipped (empty list), return the current puzzle
    if not boxes_to_check:
        return puzzle, 0

    # calc error cost for current and new state
    current_cost = sum(SA_calculate_row_column_errors(box[0], box[1], puzzle) for box in boxes_to_check)
    new_cost = sum(SA_calculate_row_column_errors(box[0], box[1], new_puzzle) for box in boxes_to_check)
    
    cost_diff = new_cost - current_cost # calc cost diff
    rho = math.exp(-cost_diff / sigma) # calc accept. probability
    
    # if new state accepted, return new puzzle and cost diff
    if random.random() < rho:
        return new_puzzle, cost_diff
    # if not return current puzzle and no cost diff
    return puzzle, 0

# calculate initial temperature (sigma)
def SA_calculate_initial_sigma(puzzle, fixed_puzzle, blocks):
    differences = [] # store # of errors
    temp_puzzle = puzzle
    for _ in range(9):  # loop to propose new state and errors
        temp_puzzle = SA_propose_state(temp_puzzle, fixed_puzzle, blocks)[0]
        differences.append(SA_calculate_errors(temp_puzzle))
    return statistics.stdev(differences)

# function to run simulated annealing process
def SA_solve_sudoku(puzzle):
    max_iterations = 2000 # set max iterations
    iterations = 0
    solution_found = False # if solution found
    stuck_count = 0 
    fixed_puzzle = copy.deepcopy(puzzle)
    blocks, fixed_puzzle = SA_prepare_puzzle(fixed_puzzle)

    temp_puzzle = SA_randomly_fill_blocks(puzzle, blocks)
    sigma = SA_calculate_initial_sigma(puzzle, fixed_puzzle, blocks)
    score = SA_calculate_errors(temp_puzzle)

    while not solution_found and iterations < max_iterations: # continue unless iteration reached or solution found
        prev_score = score
        for _ in range(100):
            new_state, score_diff = SA_choose_new_state(temp_puzzle, fixed_puzzle, blocks, sigma)
            temp_puzzle = new_state
            score += score_diff
            if score <= 0:
                solution_found = True
                break
        if score <= 0 or iterations >= max_iterations:
            solution_found = True
            break
        
        sigma *= 0.99 
        if score >= prev_score:
            stuck_count += 1
        else:
            stuck_count = 0
        
        if stuck_count > 80:
            sigma += 2  # increase to excape local optima
        iterations += 1

    return temp_puzzle if solution_found else None

# print puzzle
def SA_print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) for num in row))


def SA_run(puzzle):
    solution = SA_solve_sudoku(puzzle)
    if solution:
        #print("Puzzle solved with Simulated Annealing")
        #SA_print_puzzle(solution)
        return True
    else:
        #print("Failed to solve")
        return False
