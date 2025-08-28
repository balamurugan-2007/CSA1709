from collections import deque
def is_valid(m_left, c_left, m_right, c_right):
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True
def missionaries_cannibals():
    start = (3, 3, 'L', 0, 0)
    goal = (0, 0, 'R', 3, 3)
    q = deque([(start, [start])])
    visited = set([start])
    while q:
        (m_left, c_left, boat, m_right, c_right), path = q.popleft()
        if (m_left, c_left, boat, m_right, c_right) == goal:
            return path
        if boat == 'L':
            moves = [(-2, 0), (-1, 0), (0, -2), (-1, -1), (0, -1)]
        else:
            moves = [(2, 0), (1, 0), (0, 2), (1, 1), (0, 1)]
        for m, c in moves:
            if boat == 'L':
                new_state = (m_left + m, c_left + c, 'R', m_right - m, c_right - c)
            else:
                new_state = (m_left + m, c_left + c, 'L', m_right - m, c_right - c) 
            if is_valid(*new_state[:2], *new_state[3:]) and new_state not in visited:
                visited.add(new_state)
                q.append((new_state, path + [new_state]))
    return None
solution = missionaries_cannibals()
for step in solution:
    print(step)
