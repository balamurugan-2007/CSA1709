def a_star(graph, start, goal, h):
    open_set = set([start])
    came_from = {}
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]
    
    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            print("A* Path:", path)
            print("Total Cost:", g_score[goal])
            return path
        
        open_set.remove(current)
        
        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = g_score[neighbor] + h[neighbor]
                open_set.add(neighbor)
    
    print("Goal not reachable")
    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

h = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

a_star(graph, 'A', 'D', h)
