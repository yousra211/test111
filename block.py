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
    directions = ("N", "E", "S", "W")
    for j in range(3):
        for dir in directions:
            self.maze[y + j][x][dir] = True


def horizontal_closed(self, x, y):
    directions = ("N", "E", "S", "W")
    for i in range(3):
        for dir in directions:
            self.maze[y][x + i][dir] = True
