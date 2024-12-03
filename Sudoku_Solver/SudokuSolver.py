import Backtracking as BT
import HillClimbing as HC
import SimulatedAnnealing as SA
import time

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

def run(puzzles):
    # holder values
    BT_times = []
    BT_solved = 0
    SA_times = []
    SA_solved = 0
    HC_times = []
    HC_solved = 0

    for index, puzzle in enumerate(puzzles):
        if check_initial_puzzle(puzzle):
            print("Puzzle Invaild")
        else:

            
            # calc the Backtracking times
            start_time = time.time()
            value = BT.BT_run(puzzle)
            end_time = time.time()
            BT_times.append(end_time - start_time) # append time taken
            if value == True: BT_solved += 1 # add count if solved"""

            
            # calc the Simulated Annealing times
            start_time = time.time()
            value = SA.SA_run(puzzle)
            end_time = time.time()
            SA_times.append(end_time - start_time) # append time taken
            if value == True: SA_solved += 1 # add count if solved"""

            # calc the Hill Climbing times
            start_time = time.time()
            value = HC.HC_run(puzzle)    
            end_time = time.time()
            HC_times.append(end_time - start_time) # append time take
            if value == True: HC_solved += 1 # add count if solved"""

        print("Puzzle " + str(index) + " done.")
        
    BT_sum = 0
    SA_sum = 0
    HC_sum = 0
    for i in range(10):
        BT_sum += BT_times[i]
        SA_sum += SA_times[i]
        HC_sum += HC_times[i]
    BT_sum = BT_sum / 10
    SA_sum = SA_sum / 10
    HC_sum = HC_sum / 10
    print("Average time for Backtracking is " + str(BT_sum) + " and was solved " + str(BT_solved) + " times.\n")
    print("Average time for Hill Climbing is " + str(HC_sum) + " and was solved " + str(HC_solved) + " times.\n")
    print("Average time for Simulated Annealing is " + str(SA_sum) + " and was solved " + str(SA_solved) + " times.\n")    


puzzle_0 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

puzzle_1 = [
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

puzzle_2 = [
    [0, 8, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 9, 0, 0, 0],
    [7, 6, 0, 0, 4, 0, 0, 5, 0],
    [0, 0, 3, 0, 0, 0, 6, 0, 0],
    [0, 4, 0, 0, 6, 0, 0, 7, 3],
    [0, 0, 0, 6, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 8, 0]
]

puzzle_3 = [
    [8, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 6, 0, 0, 3, 0],
    [0, 4, 0, 0, 9, 0, 5, 0, 0],
    [0, 0, 4, 0, 2, 6, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 9, 4, 0, 8, 0, 0],
    [0, 7, 9, 0, 0, 0, 0, 4, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7]
]

puzzle_4 = [
    [0, 0, 0, 0, 8, 0, 0, 1, 0],
    [0, 2, 0, 4, 0, 0, 7, 0, 0],
    [0, 5, 0, 0, 3, 1, 0, 9, 0],
    [5, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 4, 5, 0, 3, 0, 0, 0],
    [0, 0, 8, 0, 7, 0, 0, 0, 2],
    [0, 9, 0, 2, 4, 0, 1, 0, 0],
    [0, 0, 5, 0, 0, 7, 0, 6, 0],
    [0, 4, 0, 0, 6, 0, 0, 0, 5]
]

puzzle_5 = [
    [0, 0, 8, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 7, 0, 4, 0, 0, 0],
    [5, 0, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 5, 0, 0],
    [3, 0, 0, 0, 5, 0, 0, 0, 8],
    [0, 0, 0, 8, 0, 2, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 4, 0, 0]
]

puzzle_6 = [
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [4, 0, 9, 3, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 7, 0, 3, 9, 4],
    [9, 3, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 7, 9, 0, 3],
    [8, 0, 0, 9, 0, 0, 0, 7, 0],
    [0, 0, 0, 7, 9, 0, 0, 4, 8],
    [0, 9, 0, 4, 0, 0, 1, 3, 0],
    [0, 4, 0, 0, 0, 1, 0, 0, 0]
]

puzzle_7 = [
    [0, 0, 2, 4, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 3, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 5, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 6, 3, 0, 0]
]

puzzle_8 = [
    [0, 0, 0, 2, 0, 0, 0, 0, 9],
    [9, 0, 0, 6, 0, 0, 0, 3, 0],
    [0, 5, 0, 0, 0, 9, 8, 0, 0],
    [0, 0, 5, 0, 3, 0, 0, 0, 0],
    [3, 7, 0, 0, 8, 0, 4, 1, 0],
    [0, 9, 0, 5, 0, 0, 0, 7, 3],
    [0, 0, 9, 0, 7, 0, 0, 8, 0],
    [0, 1, 0, 0, 0, 5, 0, 0, 4],
    [7, 0, 0, 0, 0, 3, 0, 0, 0]
]

puzzle_9 = [
    [0, 0, 0, 2, 0, 0, 0, 0, 9],
    [9, 0, 0, 6, 0, 0, 0, 3, 0],
    [0, 5, 0, 0, 0, 9, 8, 0, 0],
    [0, 0, 5, 0, 3, 0, 0, 0, 0],
    [3, 7, 0, 0, 8, 0, 4, 1, 0],
    [0, 9, 0, 5, 0, 0, 0, 7, 3],
    [0, 0, 9, 0, 7, 0, 0, 8, 0],
    [0, 1, 0, 0, 0, 5, 0, 0, 4],
    [7, 0, 0, 0, 0, 3, 0, 0, 0]
]


puzzles = [puzzle_0, puzzle_1, puzzle_2, puzzle_3, puzzle_4, puzzle_5, puzzle_6, puzzle_7, puzzle_8, puzzle_9]


if __name__ == "__main__":
    run(puzzles)