def generate_block(x, y) -> list[list]:
    block = []
    for j in range(3):
        row_j = []
        for i in range(3):
            row_j.append((x + i, y + j))
        block.append(row_j)
    return block

blocks = generate_block(1, 2)
for j in range(3):
    for i in range(3):
        print(blocks[j][i])
    print("\n")



def vertical_closed(self, x, y):
    neighbor_walls = []
    for i in range(3):
        cy = y + i
        for direction in ["N", "E", "S", "W"]:
            self.maze[cy][x][direction] = True

        if cy > 0:
            self.maze[cy-1][x]["S"] = True
            neighbor_walls.append((cy-1, x, "S"))
            if all(self.maze[cy-1][x][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (cy-1, x, wall) not in neighbor_walls:
                        self.maze[cy-1][x][wall] = False
                        break

        if cy < self.height - 1:
            self.maze[cy+1][x]["N"] = True
            neighbor_walls.append((cy+1, x, "N"))
            if all(self.maze[cy+1][x][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (cy+1, x, wall) not in neighbor_walls:
                        self.maze[cy+1][x][wall] = False
                        break

        if x > 0:
            self.maze[cy][x-1]["E"] = True
            neighbor_walls.append((cy, x-1, "E"))
            if all(self.maze[cy][x-1][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (cy, x-1, wall) not in neighbor_walls:
                        self.maze[cy][x-1][wall] = False
                        break

        if x < self.width - 1:
            self.maze[cy][x+1]["W"] = True
            neighbor_walls.append((cy, x+1, "W"))
            if all(self.maze[cy][x+1][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (cy, x+1, wall) not in neighbor_walls:
                        self.maze[cy][x+1][wall] = False
                        break

def horizontal_closed(self, x, y):
    neighbor_walls = []
    for i in range(3):
        cx = x + i
        for direction in ["N", "E", "S", "W"]:
            self.maze[y][cx][direction] = True

        if y > 0:
            self.maze[y-1][cx]["S"] = True
            neighbor_walls.append((y-1, cx, "S"))
            if all(self.maze[y-1][cx][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (y-1, cx, wall) not in neighbor_walls:
                        self.maze[y-1][cx][wall] = False
                        break

        if y < self.height - 1:
            self.maze[y+1][cx]["N"] = True
            neighbor_walls.append((y+1, cx, "N"))
            if all(self.maze[y+1][cx][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (y+1, cx, wall) not in neighbor_walls:
                        self.maze[y+1][cx][wall] = False
                        break

        if cx > 0:
            self.maze[y][cx-1]["E"] = True
            neighbor_walls.append((y, cx-1, "E"))
            if all(self.maze[y][cx-1][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (y, cx-1, wall) not in neighbor_walls:
                        self.maze[y][cx-1][wall] = False
                        break

        if cx < self.width - 1:
            self.maze[y][cx+1]["W"] = True
            neighbor_walls.append((y, cx+1, "W"))
            if all(self.maze[y][cx+1][d] for d in ["N","E","S","W"]):
                for wall in ["N", "E", "S", "W"]:
                    if (y, cx+1, wall) not in neighbor_walls:
                        self.maze[y][cx+1][wall] = False
                        break
