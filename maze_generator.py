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
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append({"N": True, "E": True, "S":True, "W": True})
            self.maze.append(row)

    def DFS(self, x: int, y: int, visited: list[list]) -> None:
        directions = [
            ("N", "S", 0, -1),
            ("S", "N", 0, 1),
            ("E", "W", 1, 0),
            ("W", "E", -1, 0)
        ]