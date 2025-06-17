import random
import math
from settings import GRID_WIDTH, GRID_HEIGHT, NEST_POSITION

class Ant:
    def __init__(self, grid, speed):
        self.grid = grid
        self.x, self.y = NEST_POSITION # start at nest
        self.has_food = False
        self.speed = speed
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.last_x = NEST_POSITION
        self.last_y = NEST_POSITION
        self.bored = 0
        self.state = "FORAGING"

        self.turn_probability = 0.9

    def get_position(self):
        return self.x, self.y
    
    def drop_pherormone(self):
        x = int(self.x)
        y = int(self.y)
        if self.has_food:
            self.grid.pheromone_home[x, y] += 10
        else:
            self.grid.pheromone_food[x, y] += 10

    def update(self):
        int_x = int(self.x)
        int_y = int(self.y)

        # --- Drop pheromone if in new cell ---
        if (int_x != self.last_x) or (int_y != self.last_y):
            self.drop_pherormone()
            self.last_x = int_x
            self.last_y = int_y

        # --- Switch state based on position ---
        if self.has_food and self.grid.is_nest(int_x, int_y):
            self.has_food = False  # Drop food at nest

        if not self.has_food:
            food = self.grid.get_food_at(self.x, self.y)
            if food is not None:
                self.has_food = True
                food.take()

        # --- Pheromone following ---
        if self.bored > 0:
            self.bored -= 1
        else:
            pher_dir = self.grid.get_strongest_direction(int_x, int_y, self.has_food)
            blend_factor = 0.4
            self.dx = (1 - blend_factor) * self.dx + blend_factor * pher_dir[0]
            self.dy = (1 - blend_factor) * self.dy + blend_factor * pher_dir[1]

        # --- Add some random movement (wandering) ---
        if random.random() > 0.1:
            self.dx += random.uniform(-0.3, 0.3)
        if random.random() > 0.1:
            self.dy += random.uniform(-0.3, 0.3)

        if random.random() > 0.99:
            self.bored += int(random.uniform(0, 15))

        # --- Steering toward nest if carrying food ---
        if self.has_food:
            home_dir = self.grid.get_home_direction(self.x, self.y)
            steer_factor = 0.7
            self.dx = (1 - steer_factor) * self.dx + steer_factor * home_dir[0]
            self.dy = (1 - steer_factor) * self.dy + steer_factor * home_dir[1]

        # --- Normalize speed ---
        magnitude = math.hypot(self.dx, self.dy)
        if magnitude > 0:
            self.dx = (self.dx / magnitude) * self.speed
            self.dy = (self.dy / magnitude) * self.speed

        # --- Bounce off walls ---
        if self.x < 2:
            self.dx = abs(self.dx)
        if self.x > GRID_WIDTH - 2:
            self.dx = -abs(self.dx)
        if self.y < 2:
            self.dy = abs(self.dy)
        if self.y > GRID_HEIGHT - 2:
            self.dy = -abs(self.dy)

        # --- Move ---
        self.x += self.dx
        self.y += self.dy
