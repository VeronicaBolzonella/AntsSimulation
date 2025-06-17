import random
import math
from world.grid import Grid

class Ant:
    def __init__(self, x, y, grid, food_grid, width, height):
        self.x = float(x)
        self.y = float(y)
        self.x = x
        self.y = y
        self.last_x = x
        self.last_y = y
        self.home_x = x
        self.home_y = y

        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

        self.has_food = False
        self.home_pherormone = 100.0
        self.food_pherormone = 100.0
        self.USE_RATE = 0.995
        self.WANDER_CHANCE = 0.92
        self.bored = 0

        self.grid = grid
        self.food_grid = food_grid

        self.width = width
        self.height = height

    def step(self):
        # Wandering randomness
        if random.random() > self.WANDER_CHANCE:
            self.dx += random.uniform(-1, 1)
        if random.random() > self.WANDER_CHANCE:
            self.dy += random.uniform(-1, 1)
        if random.random() > 0.99:
            self.bored += math.floor(random.uniform(0, 15))

        if self.bored > 0:
            self.bored -= 1
        else:
            # Follow pheromone trails
            if self.has_food:
                direction = self.grid.get_strongest(self.x, self.y)
            else:
                direction = self.food_grid.get_strongest(self.x, self.y)

            self.dx += direction[0] * random.uniform(0, 1.5)
            self.dy += direction[1] * random.uniform(0, 1.5)

        # Keep inside bounds
        if self.x < 2: self.dx = 1
        if self.x > self.width - 2: self.dx = -1
        if self.y < 2: self.dy = 1
        if self.y > self.height - 2: self.dy = -1

        # Clamp speed
        self.dx = max(min(self.dx, 1), -1)
        self.dy = max(min(self.dy, 1), -1)

        # Move
        self.x += self.dx
        self.y += self.dy
        self.x = int(self.x)
        self.y = int(self.y)

        # If moved to a new cell
        if self.x != self.last_x or self.y != self.last_y:
            if self.has_food:
                self.food_pherormone *= self.USE_RATE
                self.food_grid.set_value(self.x, self.y, self.food_pherormone)
            else:
                self.home_pherormone *= self.USE_RATE
                self.grid.set_value(self.x, self.y, self.home_pherormone)

        self.last_x = self.x
        self.lastY = self.y
