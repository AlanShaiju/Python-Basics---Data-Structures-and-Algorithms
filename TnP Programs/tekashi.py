# Represents the maze as a graph where each room is a node and each door is an edge
maze = {
    'start': ['room1'],
    'room1': ['room2', 'room3', 'room4', 'room5'],
    'room2': ['room6'],
    'room3': ['room7'],
    'room4': ['room8'],
    'room5': ['room9'],
    'room6': ['room10'],
    'room7': ['room10'],
    'room8': ['room10'],
    'room9': ['room10'],
    'room10': ['finish']
}

# Function to perform depth-limited search from a given room
def depth_limited_search(room, limit, visited):
    if room == 'finish':
        return [room]
    
    if limit == 0:
        return None
    
    visited.add(room)
    
    for next_room in maze[room]:
        if next_room not in visited:
            path = depth_limited_search(next_room, limit - 1, visited)
            if path is not None:
                return [room] + path
    
    return None

# Function to perform iterative deepening depth-first search
def iterative_deepening_dfs(start):
    for depth_limit in range(len(maze)):
        visited = set()
        path = depth_limited_search(start, depth_limit, visited)
        if path is not None:
            return path

# Starting the journey from the beginning
start_room = 'start'
path_to_victory = iterative_deepening_dfs(start_room)

if path_to_victory:
    print("Congratulations! You have found the optimal path to victory:")
    print(" -> ".join(path_to_victory))
else:
    print("Sorry, no path to victory found. Please reassess your strategy.")