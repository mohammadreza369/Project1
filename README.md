# Graph Algorithms Project

This project demonstrates various graph algorithms, including Depth-First Search (DFS) for pathfinding, the Knight's Tour problem using backtracking, and checking for strong connectivity in a directed graph. Below is a detailed description of each component of the project, including the functions and their purposes.

## Table of Contents

1. [Graph Pathfinding using DFS](#graph-pathfinding-using-dfs)
2. [Knight's Tour Problem](#knights-tour-problem)
3. [Strong Connectivity in Directed Graphs](#strong-connectivity-in-directed-graphs)
4. [How to Run the Code](#how-to-run-the-code)

## Graph Pathfinding using DFS

### Description
This part of the project implements Depth-First Search (DFS) to find paths in a graph. It includes two versions:
- **Unweighted Graph**: Finds the path with the least number of steps.
- **Weighted Graph**: Finds the path with the least weight (cost).

### Files
- **graph_path_dfs.py**: Contains the implementation of DFS for both unweighted and weighted graphs.

### Functions

#### `dfs_find_paths(G, goal, path=['A'], found_paths=[])`
- **Purpose**: Finds all paths from the starting node to the goal node in an unweighted graph using DFS.
- **Parameters**:
  - `G`: The graph represented as a dictionary.
  - `goal`: The target node to reach.
  - `path`: The current path being explored (default starts with `['A']`).
  - `found_paths`: A list to store all found paths.
- **Returns**: The best path (shortest in terms of steps) from the start to the goal.

#### `dfs_find_paths_weighted(G, goal, path=['A'], path_cost=0, found_paths=[])`
- **Purpose**: Finds all paths from the starting node to the goal node in a weighted graph using DFS.
- **Parameters**:
  - `G`: The graph represented as a dictionary with edge weights.
  - `goal`: The target node to reach.
  - `path`: The current path being explored (default starts with `['A']`).
  - `path_cost`: The total cost of the current path.
  - `found_paths`: A list to store all found paths along with their costs.
- **Returns**: The best path (least cost) from the start to the goal.

### Example
```python
# Unweighted Graph
G = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'E', 'H', 'F'],
    'C' : ['D', 'E'],
    'D' : ['C', 'A', 'E'],
    'E' : ['B', 'C', 'D'],
    'F' : ['B', 'E', 'H'],
    'G' : ['F', 'H'],
    'H' : ['G', 'F']
}

# Weighted Graph
GW = {
    'A' : {'B':10, 'C':7, 'D': 4},
    'B' : {'A':10, 'E':5, 'H':11, 'F':17},
    'C' : {'D':3, 'E':6},
    'D' : {'C':3, 'A':4, 'E':6},
    'E' : {'B':5, 'C':6, 'D':6},
    'F' : {'B':17, 'E':7, 'H':4},
    'G' : {'F':8, 'H':3},
    'H' : {'G':3, 'F':4}
}
```
### Knight's Tour Problem

# Description
The Knight's Tour problem is solved using backtracking. The goal is to find a sequence of moves for a knight on a chessboard such that the knight visits every square exactly once.

# Files
- knight_tour.py: Contains the implementation of the Knight's Tour problem.

# Functions
`is_safe(x, y, board)`
- Purpose: Checks if a move is within the bounds of the chessboard and the cell is unvisited.
- Parameters:
    - `x`: The x-coordinate of the move.
    - `y`: The y-coordinate of the move.
    - `board`: The current state of the chessboard.
- Returns: `True` if the move is safe, otherwise `False`.

    `print_solution(board)`

- Purpose: Recursive utility function to solve the Knight's Tour problem using backtracking.

    Parameters:

    - `x`: The current x-coordinate of the knight.

    - `y`: The current y-coordinate of the knight.

    - `movei`: The current move number.

    - `board`: The current state of the chessboard.

- Returns: `True` if a solution is found, otherwise `False`.

`solve_kt()`

- **Purpose**: Initializes the chessboard and starts the Knight's Tour solver.
- **Parameters**: None.
- **Returns**: `True` if a solution is found, otherwise `False`.

Example
```python
# Size of the chessboard
N = 6

# Possible moves for a knight
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
```
### Strong Connectivity in Directed Graphs
# Description
This part of the project checks if a directed graph is strongly connected using DFS. A 
graph is strongly connected if there is a path from every vertex to every other vertex.

# Files

- **strong_connectivity.py**: Contains the implementation to check for strong connectivity.
- **graph.txt**: Contains the graph data in the format of edges.

# Functions
`dfs(graph, start, visited)`
- **Purpose**: Performs DFS traversal starting from a given node.
**Parameters**:
    - `graph`: The graph represented as a dictionary.
    - `start`: The starting node for DFS.
    - `visited`: A dictionary to keep track of visited nodes.

- **Returns**: None.

`is_strongly_connected(graph, vertices)`
- **Purpose**: Checks if the graph is strongly connected by performing DFS from every node.
-**Parameters**:
    - `graph`: The graph represented as a dictionary.
    - `vertices`: A set of all vertices in the graph.

    **Returns**: `True` if the graph is strongly connected, otherwise `False`.

`read_graph(filename)`
- **Purpose**: Reads the graph from a file and constructs the graph representation.
- **Parameters**:
    - `filename`: The name of the file containing the graph data.

    - **Returns**: A tuple containing the graph and a set of vertices.

`main()`
- **Purpose**: The main function to read the graph and check for strong connectivity.
- **Parameters**: None.
- **Returns**: None.

# Example
``` python
# Function to check if the graph is strongly connected
def is_strongly_connected(graph, vertices):
    for node in vertices:
        visited = {v: False for v in vertices}
        dfs(graph, node, visited)
        if not all(visited.values()):
            return False
    return True
```
### How to Run the Code
1- **Graph Pathfinding using DFS**
- Run the `graph_path_dfs.py` script.

- The script will output the paths found and the best path for both unweighted and weighted graphs.

2- **Knight's Tour Problem**
- Run the `knight_tour.py` script.
- The script will output the solution to the Knight's Tour problem on a 6x6 chessboard.

3- **Strong Connectivity in Directed Graphs**
- Ensure the `graph.txt` file is in the same directory as `strong_connectivity.py`.
- Run the `strong_connectivity.py` script.
- The script will output whether the graph is strongly connected or not.

# Dependencies
- Python 3.x
