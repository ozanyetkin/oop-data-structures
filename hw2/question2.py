# Ozan Yetkin | 1908227
# Write a recursive function that returns if a given maze is solvable or not

# Initialize a maze that is solvable
maze1 = [[0, 1, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 0, 1, 0, 0, 1, 0],
         [1, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1, 0]]

# Initialize another maze that is not solvable
maze2 = [[0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 1, 1],
         [0, 1, 1, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 1, 0, 0]]

# Initialize the function that takes maze, start, and goal as input
def is_solvable(maze, start, goal):
    current_position = start
    current_value = get_value(current_position, maze)
    neighbors = get_neighbors(current_position, maze)

    path = [current_position]
    for p in path:
        while get_value(p, maze) == 0:
            advance(p, maze, path)
            if p == goal:
                break

    # print(neighbors)


def get_neighbors(position, maze):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbor_candidates = [(position[1] + dir[0], position[0] + dir[1]) for dir in directions]
    neighbor_candidates = list(filter( lambda p: 0 <= p[0] < len(maze[0]), neighbor_candidates))
    neighbors = list(filter( lambda p: 0 <= p[1] < len(maze), neighbor_candidates))

    return neighbors

# print(get_neighbors((7, 7), maze1))

def get_value(position, maze):
    return maze[position[1]][position[0]]

# print(get_value((4,0), maze1))

def advance(position, maze, path):
    if get_value(position, maze) == 1:
        return
    path.append(position)
    for n in get_neighbors(position, maze):
        return advance(n, maze, path)

# Test cases for solvable and not solvable mazes
print(is_solvable(maze1, (0,0), (7,7)))
# should print True

print(is_solvable(maze2, (0,0), (7,7)))
# should print False