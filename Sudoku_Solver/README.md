# Biology-Inspired Sudoku Algorithmic Solutions

This project explores different Biology Inspired Machine Learning Algorithms (Backtracking, Hill Climbing, and Simulated Annealing) to attempt to solve 10 different Sudoku puzzles and compares their performance. The goal is to evaluate how well these algorithms are able to solve the puzzles as well as how quickly. This is to test whether they are a viable solution to solving Sudoku and examing why. 


## Algorithms Implemented:
- **Backtracking Solver**: A depth first search that explores all possible solutions.
- **Hill Climbing**: A local search that iteratively moves to the next best solution.
- **Simulated Annealing**: A probabilistic optimization algorithm that gradually moves towards the optimum.

## Project Objective:
- Compare the performance of each algorithm in time taken and success rate.
- Evaluate why they may or may not have been as effective.

## Technologies Used:
- Python for algorithm implementation.
- Backtracking for exact solution search.
- Hill Climbing and Simulated Annealing for heuristic optimization.
- Time module for measuring and comparing execution times.

## Installation:
Clone the repository and run the SudokuSolver.py

```bash
python SudokuSolver.py
```

## Results:
The algorithms were tested across 10 valid puzzles. The average results from three iterations are as follows:

### Average Results:

- **Backtracking**:
  - **Average Time**: 1.006
  - **Puzzles Solved**: 10 (out of 10)

- **Hill Climbing**:
  - **Average Time**: 58.615
  - **Puzzles Solved**: 1 (out of 10)

- **Simulated Annealing**:
  - **Average Time**: 0.005s
  - **Puzzles Solved**: 10 (out of 10)


## Algorithm Descriptions:

### 1. Backtracking:
Backtracking is a classic algorithmic approach for solving contraint satisfaction problems. It uses depth-first search to explore all possibilities and backtracks when a conflict occurs. This algorithm guarantees that a solution is found if one exists but can often be slow for larger scale puzzles and take more time if intensive recursion is needed.

**Performance Insight**:
Backtracking performed well solving all 10/10 puzzles within a short amount of time. This showing that even in a 9x9 grid with multiple different possibilites, it proved to be a viable algorithm to use for solving the puzzles.

### 2. Hill Climbing:
Hill Climbing is a local search algorithm that works but iteratively selecting the next best step, chooses the step that has the least amount of comflicts given a small subset of options, until it arrives at a solution. It is also very prone to getting stuck at local optima or maximum. 

**Performance Insight**:
In our case, we saw that the Hill Climbing algorithm had the worse time entirely and was only able to solve the puzzle once leading to the assumption that it is not a viable algorithm for solving sudoku. This most likely occured to it getting stuck inside a local optima and was unable to get out.

### 3. Simulated Annealing:
Simulated Annealing is a probablistic algorithm inspired by therodynamics. This follows the same idea as cooling metals which allows for less than optimal moves to be accepted to over come local optima; then as the temperature (alpha) cools, it gradually moves towards finding the global solution.

**Performance Insight**:
Simulated Annealing excelled in this solving all problems in significantly less time than backtracking. It's ability to overcome local optima allowed it to overcome the struggles Hill Climbing faced and cooling function allowed it to explore the search space quickly and easily.

## Conclusion:
- **Simulated Annealing** was the most successful as it solved all of the problems in less than a tenth of time time it took for backtracking to find a solution.
- **Backtracking** performed well and was able to find all solutions in an adequate time leading it to be a great simplistic approach to solving sudoku.
- **Hill Climbing** proved to be a bad solution to solving sudoku as it was prone to getting stuck in local solutions that it was not able to overcome.

### Key Takeaways:
- **Simulated Annealing** is the most effective algorithm for solving Sudoku puzzles.
- **Hill Climbing**, while simple, is not well-suited for Sudoku due to its tendency to get stuck in local solutions.
- **Backtracking** is a reliable approach but may not be the most efficient.