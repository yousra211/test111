import random

class MazeGenerator:
    def __init__(self, width: int, height: int, seed: int = None, perfect:bool = True) -> None:
        self.width = width
        self.height = height
        self.seed = seed
        self.maze = None
        self.path = None
        self.perfect = perfect

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
            self.imperfect()
        self.pattern_42()

    def pattern_42(self):
        if self.width >= 12 and self.height >= 9:
            self.vertical_closed((self.width // 2) - 3, (self.height // 2) - 2)
            self.vertical_closed((self.width // 2) - 1, (self.height // 2))
            self.vertical_closed((self.width // 2) + 1, (self.height // 2))
            self.vertical_closed((self.width // 2) + 3, (self.height // 2) - 2)

            self.horizontal_closed((self.width // 2) - 3, (self.height // 2))
            self.horizontal_closed((self.width // 2) + 1, (self.height // 2) - 2)
            self.horizontal_closed((self.width // 2) + 1, (self.height // 2))
            self.horizontal_closed((self.width // 2) + 1, (self.height // 2) + 2)


    def vertical_closed(self, x, y):
        directions = [
            ("N", "S", 0, -1),
            ("S", "N", 0, 1),
            ("E", "W", 1, 0),
            ("W", "E", -1, 0)
        ]
        for i in range(3):
            for j in range(4):
                nx = x + directions[j][2]
                ny = y + directions[j][3]
                if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height and visited[ny][nx] == False:
                    self.maze[y + i][x][directions[j][0]] = True
                    self.maze[ny + i][nx][directions[j][1]] = True

    def horizontal_closed(self, x, y):
        directions = [
            ("N", "S", 0, -1),
            ("S", "N", 0, 1),
            ("E", "W", 1, 0),
            ("W", "E", -1, 0)
        ]
        for i in range(3):
            for j in range(4):
                nx = x + directions[j][2]
                ny = y + directions[j][3]
                if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height and visited[ny][nx] == False:
                    self.maze[y][x + i][directions[j][0]] = True
                    self.maze[ny][nx + i][directions[j][1]] = True

    def check_open_area(self, x: int, y: int) -> bool:
        for bx in range(x - 2, x + 1):
            for by in range (y - 2, y + 1):
                if bx >= 0 and bx + 2 < self.width and by >= 0 and by + 2 < self.height:
                    close = False
                    for j in range(3):
                        for i in range(3):
                            if (self.maze[by + j][bx + i]["E"] == True and i != 2) or (self.maze[by + j][bx + i]["S"] == True and j != 2):
                                close = True
                                break
                        else:
                            continue
                        if close == True:
                            break
                        else:
                            return True
        return False

    def imperfect(self):
        removable_walls = []
        for y in range(self.height):
            for x in range (self.width):
                if self.maze[y][x]["E"] == True and x + 1 < self.width:
                    removable_walls.append((y, x, "E"))
                if self.maze[y][x]["S"] == True and y + 1 < self.height:
                    removable_walls.append((y, x, "S"))
        random.shuffle(removable_walls)
        for i in range(self.height * self.width * 10 // 100):

            y_remove = removable_walls[i][0]
            x_remove = removable_walls[i][1]
            direct = removable_walls[i][2]

            self.maze[y_remove][x_remove][direct] = False

            if direct == "E":
                self.maze[y_remove][x_remove + 1]["W"] = False

            elif direct == "S":
                self.maze[y_remove + 1][x_remove]["N"] = False

            if self.check_open_area(x_remove, y_remove) == True:
                self.maze[y_remove][x_remove][direct] = True
                if direct == "E":
                    self.maze[y_remove][x_remove + 1]["W"] = True

                elif direct == "S":
                    self.maze[y_remove + 1][x_remove]["N"] = True


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





# test
    def print_maze(self):

        # top border
        print("+" + "---+" * self.width)

        for y in range(self.height):

            row_mid = ""
            row_bot = ""

            for x in range(self.width):

                # west wall
                row_mid += "|" if self.maze[y][x]["W"] else " "

                # check if fully closed
                if all(self.maze[y][x][d] for d in ("N","E","S","W")):
                    row_mid += " X "
                else:
                    row_mid += "   "

                # bottom walls
                row_bot += "+"
                row_bot += "---" if self.maze[y][x]["S"] else "   "

            # east wall of last cell
            row_mid += "|" if self.maze[y][self.width-1]["E"] else " "

            row_bot += "+"

            print(row_mid)
            print(row_bot)


gen = MazeGenerator(16, 16, seed=42)
gen.generate()
gen.print_maze()