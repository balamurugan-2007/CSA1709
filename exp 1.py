import heapq
def manhattan(state, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    x, y = divmod(index, 3)
    moves = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

    for nx, ny in moves:
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx*3 + ny
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors
def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (0 + manhattan(start, goal), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(pq, (g+1+manhattan(neighbor, goal), g+1, neighbor, path+[neighbor]))

    return None
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

solution = a_star(start_state, goal_state)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution exists.")
