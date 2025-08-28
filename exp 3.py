from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    q = deque([(0, 0)])  
    
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        print(f"Jug1: {x}, Jug2: {y}")
        visited.add((x, y))
        if x == target or y == target:
            print("\nTarget reached!")
            return True
        next_states = [
            (cap1, y),  
            (x, cap2),  
            (0, y),     
            (x, 0),    
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),  
            (x + min(y, cap1 - x), y - min(y, cap1 - x)) 
        ]
        
        for state in next_states:
            if state not in visited:
                q.append(state)
    return False
water_jug_bfs(4, 3, 2)
