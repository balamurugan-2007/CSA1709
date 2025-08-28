def is_safe(region, color, assignment, adjacency):
    for neighbor in adjacency[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(regions, colors, adjacency, assignment={}):
    if len(assignment) == len(regions):
        return assignment
    
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]
    
    for color in colors:
        if is_safe(region, color, assignment, adjacency):
            assignment[region] = color
            result = map_coloring(regions, colors, adjacency, assignment)
            if result:
                return result
            del assignment[region]  
    
    return None

regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
adjacency = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
colors = ['Red', 'Green', 'Blue']

solution = map_coloring(regions, colors, adjacency)
print("Map Coloring Solution:", solution)
