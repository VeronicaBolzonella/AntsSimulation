import numpy as np
from settings import (
    INITIAL_PHEROMONE,
    PHEROMONE_DECAY,
    GRID_WIDTH,
    GRID_HEIGHT,
    NEST_POSITION,
)

class Grid:
    def __init__(self, width, height, food_list):
        self.width = width
        self.height = height
        self.food_list = food_list

    def is_nest(self, x, y):
        return (x, y) == NEST_POSITION