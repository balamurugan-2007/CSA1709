def vacuum_cleaner():
    rooms = {'A': 'Dirty', 'B': 'Dirty'}
    position = 'A' 
    print("Initial State:", rooms, "Vacuum at:", position)
    while 'Dirty' in rooms.values():
        if rooms[position] == 'Dirty':
            print(f"Vacuum sucks dirt at {position}")
            rooms[position] = 'Clean'
        else:
            print(f"{position} is already clean")
        if position == 'A':
            position = 'B'
            print("Vacuum moves to B")
        else:
            position = 'A'
            print("Vacuum moves to A")
    print("Final State:", rooms, "Vacuum at:", position)
vacuum_cleaner()
