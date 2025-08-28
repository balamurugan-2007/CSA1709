from collections import deque
def bfs(graph, start, goal):
    visited = []
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            visited.append(node)  
            if node == goal:
                print("BFS Path:", path)
                return path
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    print("Goal not reachable")
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A', 'F')
