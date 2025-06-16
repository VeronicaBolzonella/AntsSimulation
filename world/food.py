class Food:
    def __init__(self, x, y, amount = 10):
        self.x = x
        self.y = y
        self.amount = amount  # total food units

    def is_depleted(self):
        return self.amount <= 0

    def take(self, amount_taken = 1):
        self.amount = max(0, self.amount - amount_taken)
