import numpy as np
import math
from settings import (
    INITIAL_PHEROMONE,
    PHEROMONE_DECAY_FOOD, PHEROMONE_DECAY_HOME,
    GRID_WIDTH,
    GRID_HEIGHT,
    NEST_POSITION,
    FOOD_LOCATIONS,
    PHEROMONE_DIFFUSION
)

class Grid:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food if food is not None else []
        self.pheromone_food = np.zeros((width, height), dtype=float)
        self.pheromone_home = np.zeros((width, height), dtype=float)

    def is_nest(self, x, y):
        return (x, y) == NEST_POSITION
    
    def update_pheromones(self):
        self.pheromone_food *= (1 - PHEROMONE_DECAY_FOOD)  # decay of exploring pherormone
        self.pheromone_home *= (1 - PHEROMONE_DECAY_HOME)  # decay of retunring pherormone

    def get_food_at(self, x, y):
        for food in self.food:
            if (x, y) in food.get_cells() and not food.is_depleted():
                return food
        return None
    
    def get_strongest_direction(self, x, y, has_food):
        # Choose the right pheromone map
        pheromone_map = self.pheromone_home if has_food else self.pheromone_food

        # Define relative neighbor positions
        directions = [(-1, -1), (0, -1), (1, -1),
                      (-1,  0),         (1,  0),
                      (-1,  1), (0,  1), (1,  1)]

        strongest_val = -1
        strongest_dir = (0, 0)

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                val = pheromone_map[nx, ny]
                if val > strongest_val:
                    strongest_val = val
                    strongest_dir = (dx, dy)

        return strongest_dir
    
    def get_home_direction(self, x, y):
        nx, ny = NEST_POSITION
        dx = nx - x
        dy = ny - y
        dist = math.hypot(dx, dy)
        if dist == 0:
            return (0, 0)
        return (dx / dist, dy / dist)
    
    
