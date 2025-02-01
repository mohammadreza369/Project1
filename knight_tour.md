# Knight's Tour Problem using Backtracking

---

#### **Project Title:** Knight's Tour Problem using Backtracking

#### **Student Name:** [Mohammadreza Abedi]

#### **Student ID:** [40234054]

#### **Submission Date:** [1403/11/13]

---

## 1. Introduction

### 1.1. Problem Statement
The Knight's Tour problem is a classic puzzle in which the goal is to find a sequence of moves for a knight on a chessboard such that the knight visits every square exactly once. This problem is a well-known example of a Hamiltonian path problem in graph theory.

### 1.2. Objectives
- Implement a backtracking algorithm to solve the Knight's Tour problem.
- Ensure the solution works for a fixed chessboard size (6x6).
- Provide a clear and efficient implementation of the algorithm.

---

## 2. Methodology

### 2.1. Algorithm Description
The Knight's Tour problem is solved using a backtracking approach. The algorithm explores all possible moves of the knight from a starting position and backtracks when a move leads to a dead end. The process continues until a complete tour is found or all possibilities are exhausted.

### 2.2. Implementation Details
- **Programming Language**: Python
- **Chessboard Size**: Fixed at 6x6.
- **Starting Position**: (0, 0).
- **Backtracking**: If a move leads to a dead end, the algorithm backtracks and tries the next possible move.

---

## 3. Function Documentation

### 3.1. Overview
This section provides detailed explanations of the functions implemented for the Knight's Tour problem.

### 3.2. Functions

#### **Function Name:** `is_safe`
- **Purpose**: Checks if a move is valid on the chessboard.
- **Parameters**:
  - `x`: The x-coordinate of the move.
  - `y`: The y-coordinate of the move.
  - `board`: The current state of the chessboard.
- **Return Value**: `True` if the move is valid, otherwise `False`.
- **Logic**: Ensures the move is within the bounds of the chessboard and the cell is unvisited.

#### **Function Name:** `print_solution`
- **Purpose**: Prints the current state of the chessboard.
- **Parameters**:
  - `board`: The current state of the chessboard.
- **Return Value**: None.
- **Logic**: Iterates through the chessboard and prints each cell with proper formatting.

#### **Function Name:** `solve_kt_util`
- **Purpose**: Recursive utility function to solve the Knight's Tour problem.
- **Parameters**:
  - `x`: Current x-coordinate of the knight.
  - `y`: Current y-coordinate of the knight.
  - `movei`: Current move number.
  - `board`: The current state of the chessboard.
- **Return Value**: `True` if a solution is found, otherwise `False`.
- **Logic**: Tries all possible moves for the knight and backtracks if a move leads to a dead end.

#### **Function Name:** `solve_kt`
- **Purpose**: Initializes the chessboard and starts the Knight's Tour solver.
- **Parameters**: None.
- **Return Value**: `True` if a solution is found, otherwise `False`.
- **Logic**: Initializes the chessboard, sets the starting position, and calls the recursive utility function.

---

## 4. Input and Output

### 4.1. Input Format
- The chessboard size is fixed at 6x6.
- The starting position is always (0, 0).

### 4.2. Output Format
- The solution is printed as a 6x6 chessboard with move numbers indicating the sequence of the knight's moves.

---

## 5. Conclusion
The Knight's Tour problem was successfully solved using a backtracking algorithm. The implementation efficiently explores all possible moves and backtracks when necessary, ensuring that a valid tour is found if one exists. The solution is clear, concise, and ready for further extension or application.