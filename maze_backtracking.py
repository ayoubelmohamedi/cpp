
maze = [
    "#######",
    "#S....#",
    "###.#.#",
    "#..##.#",
    "#.###.#",
    "#.#...#",
    "#.#.###",
    "#...G.#",
    "#######"
]

def find_path(maze,curr_pos, path):
    x, y = curr_pos

def find_start(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if (maze[x][y] == 'S'):
                return (x,y)

print(find_path(maze, find_start(maze), ))


