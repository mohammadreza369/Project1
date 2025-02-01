# Project Report

**Course Name:** FCP

**Project Title:** Graph Algorithms: Pathfinding, Knight's Tour, and Strong Connectivity

**Student Name:** Mohammadreza Abedi

**Student ID:** 40234054

**Submission Date:** 1403/11/13

---

## 1. Introduction

### 1.1. Problem Statement
The project focuses on solving three key problems in graph theory:
1. **Pathfinding in Graphs**: Finding the shortest path between two nodes using Depth-First Search (DFS) in both unweighted and weighted graphs.
2. **Knight's Tour Problem**: Finding a sequence of moves for a knight on a chessboard such that it visits every square exactly once.
3. **Strong Connectivity in Directed Graphs**: Determining whether a directed graph is strongly connected, meaning there is a path from every vertex to every other vertex.

These problems are fundamental in computer science and have applications in areas such as network routing, game development, and social network analysis.

### 1.2. Objectives
- Implement DFS to find paths in unweighted and weighted graphs.
- Solve the Knight's Tour problem using backtracking.
- Check for strong connectivity in directed graphs using DFS.
- Provide clear documentation and explanations for each algorithm and function.

---

## 2. Methodology

### 2.1. Algorithm Description
- **DFS for Pathfinding**: 
  - In unweighted graphs, DFS explores all possible paths from the start node to the goal node and returns the shortest path.
  - In weighted graphs, DFS calculates the total cost of each path and returns the path with the least cost.
- **Knight's Tour**:
  - A backtracking algorithm is used to explore all possible moves of a knight on a chessboard until a complete tour is found or determined to be impossible.
- **Strong Connectivity**:
  - DFS is performed from every node in the graph to ensure that all other nodes are reachable, confirming strong connectivity.

### 2.2. Implementation Details
- **Programming Language**: Python
- **Tools and Libraries**: Standard Python libraries (no external dependencies).
- **Assumptions**:
  - For the Knight's Tour, the chessboard size is fixed (6x6).
  - For strong connectivity, the graph is provided in a text file with edges listed as pairs of nodes.

---

## 3. Function Documentation

### 3.1. Overview
This section provides detailed explanations of the functions implemented in the project.

### 3.2. Functions

#### **Function Name:** `dfs_find_paths`
- **Purpose**: Finds the shortest path in an unweighted graph using DFS.
- **Parameters**:
  - `G`: The graph (dictionary).
  - `goal`: The target node.
  - `path`: The current path being explored (default: `['A']`).
  - `found_paths`: List to store all found paths.
- **Return Value**: The shortest path from the start to the goal.
- **Logic**: Explores all possible paths using DFS and returns the one with the fewest steps.
- **Exceptions**: None.

#### **Function Name:** `dfs_find_paths_weighted`
- **Purpose**: Finds the least-cost path in a weighted graph using DFS.
- **Parameters**:
  - `G`: The weighted graph (dictionary with edge costs).
  - `goal`: The target node.
  - `path`: The current path being explored (default: `['A']`).
  - `path_cost`: The total cost of the current path.
  - `found_paths`: List to store all found paths with their costs.
- **Return Value**: The path with the least cost.
- **Logic**: Explores all possible paths using DFS, calculates the total cost, and returns the path with the minimum cost.
- **Exceptions**: None.

#### **Function Name:** `is_safe`
- **Purpose**: Checks if a move is valid in the Knight's Tour problem.
- **Parameters**:
  - `x`: The x-coordinate of the move.
  - `y`: The y-coordinate of the move.
  - `board`: The current state of the chessboard.
- **Return Value**: `True` if the move is valid, otherwise `False`.
- **Logic**: Ensures the move is within the chessboard bounds and the cell is unvisited.
- **Exceptions**: None.

#### **Function Name:** `solve_kt_util`
- **Purpose**: Recursive function to solve the Knight's Tour problem.
- **Parameters**:
  - `x`: Current x-coordinate of the knight.
  - `y`: Current y-coordinate of the knight.
  - `movei`: Current move number.
  - `board`: The current state of the chessboard.
- **Return Value**: `True` if a solution is found, otherwise `False`.
- **Logic**: Tries all possible moves for the knight and backtracks if a move leads to a dead end.
- **Exceptions**: None.

#### **Function Name:** `dfs`
- **Purpose**: Performs DFS traversal on a graph.
- **Parameters**:
  - `graph`: The graph (dictionary).
  - `start`: The starting node for DFS.
  - `visited`: Dictionary to track visited nodes.
- **Return Value**: None.
- **Logic**: Uses a stack to perform DFS and marks all reachable nodes as visited.
- **Exceptions**: None.

#### **Function Name:** `is_strongly_connected`
- **Purpose**: Checks if a directed graph is strongly connected.
- **Parameters**:
  - `graph`: The graph (dictionary).
  - `vertices`: Set of all vertices in the graph.
- **Return Value**: `True` if the graph is strongly connected, otherwise `False`.
- **Logic**: Performs DFS from every node and checks if all nodes are reachable.
- **Exceptions**: None.

---

## 4. Input and Output

### 4.1. Input Format
- **Graph Pathfinding**: The graph is provided as a dictionary in the code.
- **Knight's Tour**: The chessboard size is fixed (6x6), and the starting position is (0, 0).
- **Strong Connectivity**: The graph is provided in a text file (`graph.txt`) with edges listed as pairs of nodes.

### 4.2. Output Format
- **Graph Pathfinding**: Prints all found paths and the best path (shortest or least cost).
- **Knight's Tour**: Prints the solution as a 6x6 chessboard with move numbers.
- **Strong Connectivity**: Prints whether the graph is strongly connected or not.

---

## 5. Conclusion

This project successfully implemented and demonstrated three key graph algorithms:
1. **Pathfinding using DFS** in both unweighted and weighted graphs.
2. **Knight's Tour** using backtracking.
3. **Strong Connectivity** checking in directed graphs.

The algorithms were implemented efficiently, and the project provides clear documentation and explanations for each function. The outcomes align with the objectives, and the code is ready for further extension or application in real-world scenarios.