# تابع برای انجام جستجوی عمق‌اول (DFS)
def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

# تابع برای بررسی اینکه گراف به شدت متصل است یا نه
def is_strongly_connected(graph, vertices):
    for node in vertices:
        visited = {v: False for v in vertices}
        dfs(graph, node, visited)
        if not all(visited.values()):
            return False
    return True

# تابع برای خواندن گراف از یک فایل
def read_graph(filename):
    graph = {}
    vertices = set()
    with open(filename, 'r') as file:
        for line in file:
            u, v = line.strip().split()
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            vertices.add(u)
            vertices.add(v)
    return graph, vertices

# تابع اصلی
def main():
    filename = 'graph.txt'  # نام فایل را جایگزین کنید
    graph, vertices = read_graph(filename)
    if is_strongly_connected(graph, vertices):
        print("The graph is strongly connected.")
    else:
        print("The graph is not strongly connected.")

# اجرای برنامه
main()
