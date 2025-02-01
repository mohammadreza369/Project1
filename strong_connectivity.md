# Checking Strong Connectivity in Directed Graphs using DFS

---

#### **Project Title:** Checking Strong Connectivity in Directed Graphs using DFS

#### **Student Name:** [Mohammadreza Abedi]

#### **Student ID:** [40234054]

#### **Submission Date:** [1403/11/13]

---

## 1. Introduction

### 1.1. Problem Statement
A directed graph is said to be strongly connected if there is a path from every vertex to every other vertex. This project aims to implement an algorithm to check whether a given directed graph is strongly connected using Depth-First Search (DFS).

### 1.2. Objectives
- Implement DFS to traverse the graph and check for strong connectivity.
- Ensure the algorithm works for any directed graph provided in a text file.
- Provide a clear and efficient implementation of the algorithm.

---

## 2. Methodology

### 2.1. Algorithm Description
The algorithm checks for strong connectivity by performing DFS from every vertex in the graph. If all vertices are reachable from every starting vertex, the graph is strongly connected. Otherwise, it is not.

### 2.2. Implementation Details
- **Programming Language**: Python
- **Graph Representation**: The graph is read from a text file where edges are listed as pairs of nodes.
- **DFS Traversal**: DFS is used to traverse the graph and mark reachable vertices.

---

## 3. Function Documentation

### 3.1. Overview
This section provides detailed explanations of the functions implemented for checking strong connectivity.

### 3.2. Functions

#### **Function Name:** `dfs`
- **Purpose**: Performs DFS traversal on the graph.
- **Parameters**:
  - `graph`: The graph (dictionary).
  - `start`: The starting node for DFS.
  - `visited`: Dictionary to track visited nodes.
- **Return Value**: None.
- **Logic**: Uses a stack to perform DFS and marks all reachable nodes as visited.

#### **Function Name:** `is_strongly_connected`
- **Purpose**: Checks if the graph is strongly connected.
- **Parameters**:
  - `graph`: The graph (dictionary).
  - `vertices`: Set of all vertices in the graph.
- **Return Value**: `True` if the graph is strongly connected, otherwise `False`.
- **Logic**: Performs DFS from every node and checks if all nodes are reachable.

#### **Function Name:** `read_graph`
- **Purpose**: Reads the graph from a text file.
- **Parameters**:
  - `filename`: The name of the file containing the graph data.
- **Return Value**: A tuple containing the graph and a set of vertices.
- **Logic**: Reads the file, constructs the graph as a dictionary, and collects all vertices.

#### **Function Name:** `main`
- **Purpose**: The main function to read the graph and check for strong connectivity.
- **Parameters**: None.
- **Return Value**: None.
- **Logic**: Reads the graph, checks for strong connectivity, and prints the result.

---

## 4. Input and Output

### 4.1. Input Format
- The graph is provided in a text file (`graph.txt`) where each line represents an edge as a pair of nodes (e.g., `A B`).

### 4.2. Output Format
- The program prints whether the graph is strongly connected or not.

---

## 5. Conclusion
The algorithm successfully checks for strong connectivity in directed graphs using DFS. The implementation is efficient and works for any graph provided in the specified format. The solution is clear, concise, and ready for further extension or application.