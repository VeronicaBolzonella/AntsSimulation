import random
import math
from settings import GRID_WIDTH, GRID_HEIGHT, NEST_POSITION

class Ant:
    def __init__(self, grid, speed):
        self.grid = grid
        self.x, self.y = NEST_POSITION # start at nest
        self.has_food = False
        self.speed = speed

        self.phi = random.uniform(0, 2*math.pi)
        self.turn_probability = 0.9

    def update(self):
        # change dir with turn probability
        if self.has_food:
            # Compute angle to nest
            nest_x, nest_y = NEST_POSITION
            dx = nest_x - self.x
            dy = nest_y - self.y

            angle = math.atan2(dy, dx)

            # Rotate self.phi a little toward desired_angle
            angle_diff = (angle - self.phi + math.pi) % (2 * math.pi) - math.pi  # shortest rotation
            self.phi += 0.2 * angle_diff 

            if (self.x, self.y) == NEST_POSITION:
                self.has_food = False
        else: 
            if random.random()<self.turn_probability:
                angle_change = random.uniform(-math.pi / 4, math.pi / 4)  # small random turn
                self.phi += angle_change

            food = self.grid.get_food_at(self.x, self.y)
            if food:
                food.take(1)
                self.has_food = True

        # Calculate next step
        dx = round(math.cos(self.phi))
        dy = round(math.sin(self.phi))

        # Try moving
        new_x = self.x + dx**self.speed
        new_y = self.y + dy**self.speed

        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
            self.x = new_x
            self.y = new_y
            self.drop_pherormone()


    def get_position(self):
        return self.x, self.y
    
    def drop_pherormone(self):
        if self.has_food:
            self.grid.pheromone_home[self.x, self.y] += 10
        else:
            self.grid.pheromone_food[self.x, self.y] += 10

