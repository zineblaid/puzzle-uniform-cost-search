# -Puzzle Solver Using Uniform Cost Search

## Overview

This project implements the Uniform Cost Search (UCS) algorithm in Python to solve the 8-puzzle problem.

The puzzle consists of a 3×3 board containing eight numbered tiles and one empty space, represented by `0`. The objective is to transform an initial configuration into a target configuration while minimizing the total movement cost.

Unlike algorithms that assign the same cost to every move, this implementation uses different costs for each movement direction.

## Features

- Represents puzzle states as tuples.
- Generates valid successor states.
- Uses a priority queue to explore states by cumulative path cost.
- Assigns different costs to movement directions.
- Tracks parent states and actions.
- Reconstructs the solution path.
- Displays the actions, individual movement costs, and total cost.

## Technologies

- Python 3
- `heapq` for priority queue management

No external libraries are required.

## Movement Costs

| Action | Cost |
|---|---:|
| UP | 9 |
| DOWN | 2 |
| LEFT | 4 |
| RIGHT | 3 |

The costs are assigned according to the direction in which the empty tile moves.

## Algorithm

1. Initialize the priority queue with the starting state and a cost of zero.
2. Remove the state with the lowest cumulative cost.
3. Check whether the state matches the goal configuration.
4. Generate all valid successor states.
5. Update the best-known cost and parent information whenever a cheaper path is found.
6. Continue until the goal is reached or no states remain to explore.
7. Reconstruct the sequence of actions and calculate the total solution cost.

## Example

### Initial State

```text
2 8 3
1 6 4
7 0 5
```

### Goal State

```text
1 2 3
8 0 4
7 6 5
```

The program searches for a minimum-cost sequence of moves connecting the initial state to the goal state.

## How to Run

1. Install Python 3.
2. Save the code in a file named `main.py`.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

The program prints the solution actions, the cost of each action, and the total path cost.

## Learning Objectives

- Understand uninformed search algorithms.
- Implement Uniform Cost Search using a priority queue.
- Represent states and transitions in a search problem.
- Track cumulative costs and reconstruct solution paths.
- Explore cost-sensitive pathfinding.

## Limitations

- The movement costs are predefined in the code.
- The implementation does not include a visual interface.
- No explicit solvability check is performed before the search.

## Possible Improvements

- Add a function to display the board after every move.
- Allow users to enter custom initial and goal states.
- Add a solvability check.
- Compare UCS with Breadth-First Search and A*.
- Report the number of explored states and execution time.

## License

Add a license file if you want to specify how others can use, modify, and distribute this project.
