import random

class MazeGenerator:
    def __init__(self, width: int, height: int, seed: int = None, perfect:bool = True) -> None:
        self.width = width
        self.height = height
        self.seed = seed
        self.maze = None
        self.path = None

    def generate(self) -> None:
        if self.seed is not None:
            random.seed(self.seed)
        self.maze = []
        visited = []
        for y in range(self.height):
            row = []
            visit = []
            for x in range(self.width):
                row.append({"N": True, "E": True, "S":True, "W": True})
                visit.append(False)
            self.maze.append(row)
            visited.append(visit)
        self.DFS(0, 0, visited)

        if self.perfect == False:
            removable_walls = []
            for y in range(self.height):
                for x in range (self.width):
                    if self.maze[y][x]["E"] == True and x >= 0 and x < self.width and y >= 0 and y < self.height:
                        removable_walls.append((y, x, "E"))
                    elif self.maze[y][x]["S"] == True and x >= 0 and x < self.width and y >= 0 and y < self.height:
                        removable_walls.append((y, x, "S"))

        
    def DFS(self, x: int, y: int, visited: list[list]) -> None:
        directions = [
            ("N", "S", 0, -1),
            ("S", "N", 0, 1),
            ("E", "W", 1, 0),
            ("W", "E", -1, 0)
        ]
        visited[y][x] = True
        random.shuffle(directions)
        for i in range(4):
            nx = x + directions[i][2]
            ny = y + directions[i][3]
            if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height and visited[ny][nx] == False:
                self.maze[y][x][directions[i][0]] = False
                self.maze[ny][nx][directions[i][1]] = False
                self.DFS(nx, ny, visited)