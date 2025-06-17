class Grid:
    def __init__(self, width, height):
        self.mapW = width
        self.mapH = height
        self.length = self.mapW * self.mapH
        self.map_vals = [0.0 for _ in range(self.length)]

        self.MAX_VAL = 100.0
        self.EVAPORATION_RATE = 0.999

    def step(self):
        # Evaporate pheromones over time
        self.map_vals = [val * self.EVAPORATION_RATE for val in self.map_vals]

    def set_value(self, x, y, val):
        try:
            index = y * self.mapW + x
            old_val = self.map_vals[index]
            if val > old_val:
                self.map_vals[index] = val
        except IndexError:
            # Silently ignore out-of-bounds
            pass

    def get_percentage(self, index):
        return self.map_vals[index] / self.MAX_VAL

    def get_value_by_index(self, index):
        return self.map_vals[index]

    def get_value(self, x, y):
        try:
            return self.map_vals[y * self.mapW + x]
        except IndexError:
            return -1.0

    def get_strongest(self, x, y):
        directions = [
            (-1, -1), (0, -1), (1, -1),  # Top-left, top, top-right
            (-1,  0),         (1,  0),  # Left,       , right
            (-1,  1), (0,  1), (1,  1)   # Bottom-left, bottom, bottom-right
        ]

        strongest = [0, 0]
        strongest_val = -1.0

        for dx, dy in directions:
            val = self.get_value(x + dx, y + dy)
            if val > strongest_val:
                strongest = [dx, dy]
                strongest_val = val

        return strongest
