import random
import math
import statistics
import copy

# function to set permanent values
def SA_fix_puzzle_values(puzzle):
    for i in range(9): 
        for j in range(9): 
            if puzzle[i][j] != 0:  
                puzzle[i][j] = 1  # set to 1 if value is not empty (came in orig puzzle)
    return puzzle

# calculate number of errors in puzzle (cost function)
def SA_calculate_number_of_errors(puzzle):
    error_count = 0  
    for i in range(9): 
        error_count += SA_calculate_errors_row_column(i, i, puzzle)  # add errors from cols and rows
    return error_count  # return # of errors

# check to see if duplicates exists in rows and cols
def SA_calculate_errors_row_column(row, column, puzzle):
    unique_row_values = set()  # set to store row values
    unique_column_values = set()  # set to store col values
    for i in range(9):  
        unique_row_values.add(puzzle[i][column])  
        unique_column_values.add(puzzle[row][i])
    error_count = (9 - len(unique_row_values)) + (9 - len(unique_column_values))  # calc error count based on values in the sets
    return error_count 

# create a list for the 3x3 block
def SA_create_list_3x3_blocks():
    final_block_list = [] 
    for r in range(9):
        tmp_list = []  # to store blocks
        block1 = [i + 3 * ((r) % 3) for i in range(3)]
        block2 = [i + 3 * math.trunc((r) / 3) for i in range(3)]
        for x in block1:
            for y in block2:
                tmp_list.append([x, y])
        final_block_list.append(tmp_list)
    return final_block_list

# randomly fill block & avoid conflicsts
def SA_randomly_fill_3x3_blocks(puzzle, block_list):
    for block in block_list:  # loop through 3x3 blocks
        for box in block:  # loop through cells in each block
            if puzzle[box[0]][box[1]] == 0: 
                # create list of values already in block
                current_block = [puzzle[i][j] for i in range(block[0][0], block[-1][0] + 1)
                                 for j in range(block[0][1], block[-1][1] + 1)]
                # randomly choose number to fit in cell
                puzzle[box[0]][box[1]] = random.choice([i for i in range(1, 10) if i not in current_block])
    return puzzle

# calc the sum in each block (for which parts to modify)
def SA_sum_of_one_block(puzzle, one_block):
    final_sum = 0
    for box in one_block:
        final_sum += puzzle[box[0]][box[1]]  # add in value for each cell
    return final_sum

# select 2 values in the boxes that can be swapped
def SA_two_random_boxes_within_block(fixed_puzzle, block):
    while (1):  # loop until boxes are found
        first_box = random.choice(block)  # choose random box
        second_box = random.choice([box for box in block if box is not first_box])  # choose another box, not first
        # check to make sure both boxes can be swapped
        if fixed_puzzle[first_box[0]][first_box[1]] != 1 and fixed_puzzle[second_box[0]][second_box[1]] != 1:
            return [first_box, second_box]

# swap values
def SA_flip_boxes(puzzle, boxes_to_flip):
    proposed_puzzle = copy.deepcopy(puzzle) # create a copy of the puzzle
    
    # swap values
    placeholder = proposed_puzzle[boxes_to_flip[0][0]][boxes_to_flip[0][1]]
    proposed_puzzle[boxes_to_flip[0][0]][boxes_to_flip[0][1]] = proposed_puzzle[boxes_to_flip[1][0]][boxes_to_flip[1][1]]
    proposed_puzzle[boxes_to_flip[1][0]][boxes_to_flip[1][1]] = placeholder
    return proposed_puzzle

# this is the candidate solution to evaluate
def SA_proposed_state(puzzle, fixed_puzzle, block_list):
    random_block = random.choice(block_list)  # randomly choose a block to ensure randomly
    if SA_sum_of_one_block(fixed_puzzle, random_block) > 6: # if sum is high, might indicate a good solution is already in place
        return puzzle, []
    # select two random boxes to flip
    boxes_to_flip = SA_two_random_boxes_within_block(fixed_puzzle, random_block)
    # flip & send proposed new state
    proposed_puzzle = SA_flip_boxes(puzzle, boxes_to_flip)
    return proposed_puzzle, boxes_to_flip

# function to decide whether to accept new state based on cost function
def SA_choose_new_state(current_puzzle, fixed_puzzle, block_list, sigma):
    proposal = SA_proposed_state(current_puzzle, fixed_puzzle, block_list)  # get new proposed state
    new_puzzle = proposal[0]  # new puzzle state
    boxes_to_check = proposal[1]  # boxes are flipped
    
    # if no boxes are flipped (empty list), return the current puzzle
    if not boxes_to_check:
        return current_puzzle, 0
    
    # calc error cost for current and new state
    current_cost = SA_calculate_errors_row_column(boxes_to_check[0][0], boxes_to_check[0][1], current_puzzle) + \
                   SA_calculate_errors_row_column(boxes_to_check[1][0], boxes_to_check[1][1], current_puzzle)
    new_cost = SA_calculate_errors_row_column(boxes_to_check[0][0], boxes_to_check[0][1], new_puzzle) + \
               SA_calculate_errors_row_column(boxes_to_check[1][0], boxes_to_check[1][1], new_puzzle)

    cost_difference = new_cost - current_cost  # calc cost diff
    rho = math.exp(-cost_difference / sigma)  # calc accept. probability
    
    # if new state accepted, return new puzzle and cost diff
    if random.uniform(0, 1) < rho:
        return new_puzzle, cost_difference
    # if not return current puzzle and no cost diff
    return current_puzzle, 0

# choose iteration count based on number of fixed values
def SA_choose_number_of_iterations(fixed_puzzle):
    iterations_count = 0
    for i in range(9):
        for j in range(9):
            if fixed_puzzle[i][j] != 0:  # count fixed values
                iterations_count += 1
    return iterations_count  # return # of iterations

# calculate initial temperature (sigma)
def SA_calculate_initial_sigma(puzzle, fixed_puzzle, block_list):
    differences_list = []  # store # of errors
    temp_puzzle = puzzle 
    for i in range(1, 10):  # loop to propose new state and erros
        temp_puzzle = SA_proposed_state(temp_puzzle, fixed_puzzle, block_list)[0]
        differences_list.append(SA_calculate_number_of_errors(temp_puzzle)) 
    return statistics.pstdev(differences_list)  # return stf of error

# function to run simulated annealing process
def SA_solve_sudoku(puzzle):
    solution_found = False  # if solution found
    max_iterations = 2000  # set max iterations
    iterations = 0  
    while not solution_found and iterations < max_iterations:  # continue unless iteration reached or solution found
        decrease_factor = 0.99  # decrease sigma over time
        stuck_count = 0 
        fixed_puzzle = [row[:] for row in puzzle]  
        SA_fix_puzzle_values(fixed_puzzle)  
        list_of_blocks = SA_create_list_3x3_blocks() 
        temp_puzzle = SA_randomly_fill_3x3_blocks(puzzle, list_of_blocks)  
        sigma = SA_calculate_initial_sigma(puzzle, fixed_puzzle, list_of_blocks) 
        score = SA_calculate_number_of_errors(temp_puzzle)  
        iterations = SA_choose_number_of_iterations(fixed_puzzle)  

        if score <= 0:  # if no errors puzzle solved
            solution_found = True  # set solved flag

        while not solution_found:
            previous_score = score  # store prev score
            for i in range(iterations):  # loop through iterations
                new_state = SA_choose_new_state(temp_puzzle, fixed_puzzle, list_of_blocks, sigma)  # get new state
                temp_puzzle = new_state[0]  # update puzzle with new vals
                score_diff = new_state[1]
                if score_diff < 0:  # if score decrease, update score
                    score += score_diff
                if score <= 0:  # if score <= 0 puzzle solved
                    solution_found = True
                    break
            iterations += 1 
            if iterations >= max_iterations:
                print("Puzzle Failed")
                return None

            sigma *= decrease_factor  # decrease sigma over time
            if score <= 0:  # break loop if puzzle solved
                solution_found = True
                break
            if score >= previous_score:  # track number of time no improvment
                stuck_count += 1
            else:
                stuck_count = 0  # reset if score improves
            if stuck_count > 80:  # if stuck too long, increase sigma to break out of local point
                sigma += 2
            if SA_calculate_number_of_errors(temp_puzzle) == 0: 
                break
    return temp_puzzle  # return puzzle


def SA_print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) for num in row))


def SA_run(puzzle):
    solution = SA_solve_sudoku(puzzle)
    if solution is not None:
        return True 
    else: return False

"""    if solution is not None: # solution found
        print("Puzzle Solved With Simulated Annealing")
        SA_print_puzzle(solution)
    else:
        print("Failed to solve with Simulated Annealing.")"""