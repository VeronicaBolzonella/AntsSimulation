import numpy as np
from settings import (
    INITIAL_PHEROMONE,
    PHEROMONE_DECAY_FOOD, PHEROMONE_DECAY_HOME,
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