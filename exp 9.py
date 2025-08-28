from itertools import permutations

def tsp(distance_matrix):
    cities = list(range(len(distance_matrix)))
    start = cities[0]
    min_path = None
    min_distance = float('inf')
    
    for perm in permutations(cities[1:]):
        path = [start] + list(perm) + [start]
        distance = 0
        for i in range(len(path) - 1):
            distance += distance_matrix[path[i]][path[i+1]]
        if distance < min_distance:
            min_distance = distance
            min_path = path
            
    print("Shortest Path:", min_path)
    print("Minimum Distance:", min_distance)

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(distance_matrix)
