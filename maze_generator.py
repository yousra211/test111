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

