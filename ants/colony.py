from .ant import Ant

class Colony:
    def __init__(self, x, y, count, pher_home, pher_food, width, height):
        self.x = x
        self.y = y
        self.ants = [
            Ant(x, y, pher_home, pher_food, width, height)
            for _ in range(count)
        ]
