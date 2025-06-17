class Food:
    def __init__(self, width, height):
        self.mapW = width
        self.mapH = height
        self.length = self.mapW * self.mapH
        self.map_vals = [False for _ in range(self.length)]

    def add_food(self, x, y):
        try:
            for i in range(x, min(x + 10, self.mapW)):
                for j in range(y, min(y + 10, self.mapH)):
                    self.set_value(i, j, True)
        except Exception:
            pass  # Ignore out-of-bounds

    def set_value(self, x, y, val):
        try:
            self.map_vals[y * self.mapW + x] = val
        except IndexError:
            pass  # Ignore out-of-bounds

    def bite(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                self.set_value(x + dx, y + dy, False)

    def get_value_by_index(self, index):
        return self.map_vals[index]

    def get_value(self, x, y):
        try:
            return self.map_vals[y * self.mapW + x]
        except IndexError:
            return False
