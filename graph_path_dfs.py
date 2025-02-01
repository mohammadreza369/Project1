# Solving Combinatorial Problems by Search
#  Using Depth-First-Search (DFS)
# Path finding in a Graph
#  Path with least steps
#  Path with least weight (cost)


# A graph without cost on its edge
#   (uniform cost for all edges)
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

def dfs_find_paths(G, goal, path=['A'], found_paths=[]):
    cur_node = path[-1]
    if cur_node == goal:
        found_paths.append(path[:])
        return path

    best_path = []
    len_best_path = 100000000
    for next_node in G[cur_node]:
        if next_node not in path:
            path.append(next_node)
            fpath = dfs_find_paths(G, goal, path, found_paths)
            if fpath != [] and len(fpath) < len_best_path:
                best_path = fpath[:]
                len_best_path = len(best_path)
            path.pop()
    return best_path
        

paths = []
best_path = dfs_find_paths(G, 'G', ['C'], paths)
for p in paths:
    print(p)
print('Best path:', best_path)


# A graph with cost/length/time on its edge
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
def dfs_find_paths_weighted(G, goal, path=['A'], path_cost=0, found_paths=[]):
    cur_node = path[-1]
    if cur_node == goal:
        found_paths.append((path[:], path_cost))
        return (path, path_cost)

    best_path = []
    best_path_cost = 100000000
    for next_node in G[cur_node]:
        if next_node not in path:
            cost = G[cur_node][next_node]
            path.append(next_node)
            path_cost += cost
            fpath, fcost = dfs_find_paths_weighted(G, goal, path, path_cost, found_paths)
            if fpath != [] and fcost < best_path_cost:
                best_path = fpath[:]
                best_path_cost = fcost
            path.pop()
            path_cost -= cost
    return (best_path, best_path_cost)
        

paths = []
best_path = dfs_find_paths_weighted(GW, 'A', ['G'], 0, paths)
for p in paths:
    print(p)
print('Shortest path:', best_path)
