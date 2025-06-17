class Food:
    def __init__(self, x, y, amount = 80, size=3):
        self.x = x
        self.y = y
        self.amount = amount  # total food units
        self.size = size

    def is_depleted(self):
        return self.amount <= 0

    def take(self, amount_taken = 1):
        self.amount = max(0, self.amount - amount_taken)

    def get_cells(self):
        return [
            (self.x + dx, self.y + dy)
            for dx in range(self.size)
            for dy in range(self.size)
        ]
