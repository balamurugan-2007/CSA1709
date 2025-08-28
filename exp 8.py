def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
        
    visited.add(start)
    
    if start == goal:
        print("DFS Path:", path)
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = path + [neighbor]
            result = dfs(graph, neighbor, goal, new_path, visited)
            if result:
                return result
    
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A', 'F')
