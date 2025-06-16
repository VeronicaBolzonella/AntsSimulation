import numpy as np
from world.food import Food
from settings import (
    INITIAL_PHEROMONE,
    PHEROMONE_DECAY,
    GRID_WIDTH,
    GRID_HEIGHT,
    NEST_POSITION,
    FOOD_LOCATIONS
)

class Grid:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food if food is not None else []
        self.pheromone = np.zeros((width, height), dtype=float)

    def is_nest(self, x, y):
        return (x, y) == NEST_POSITION
    
    def update_pheromones(self):
        self.pheromone *= (1 - PHEROMONE_DECAY)  # decay