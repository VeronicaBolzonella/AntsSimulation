import numpy as np
from settings import GRID_WIDTH, GRID_HEIGHT, INITIAL_PHEROMONE, FOOD_LOCATIONS, FOOD_AMOUNT, NEST_POSITION, INITIAL_FOOD_STORAGE, NEST_SIZE


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nest_food_storage = INITIAL_FOOD_STORAGE

        # Initialize pheromone and food maps
        self.pheromone = np.full((width, height), INITIAL_PHEROMONE, dtype=np.float32)
        self.food = np.zeros((width, height), dtype=np.int32)

        # Nest setup (3x3 centered on NEST_POSITION)
        self.nest_x, self.nest_y = NEST_POSITION

        # Create 3x3 nest area centered on (nest_x, nest_y)
        half_size = NEST_SIZE//2
        self.nest_area = set()
        for dx in range(-half_size, half_size + 1):
            for dy in range(-half_size, half_size + 1):
                x, y = self.nest_x + dx, self.nest_y + dy
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.nest_area.add((x, y))

        # Place food at specified locations
        for fx, fy in FOOD_LOCATIONS:
            self.food[fx, fy] = FOOD_AMOUNT
        
    def evaporate_pheromones(self, decay_rate=0.01):
        """Evaporate pheromones slightly at each cell."""
        self.pheromone *= (1 - decay_rate)
        self.pheromone = np.clip(self.pheromone, 0, 255)

    def deposit_pheromone(self, x, y, amount):
        """Ants call this to leave a trail."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pheromone[x, y] += amount

    def get_pheromone_level(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pheromone[x, y]
        return 0

    def take_food(self, x, y):
        """Called by an ant to take one unit of food if available."""
        if self.food[x, y] > 0:
            self.food[x, y] -= min(self.food[x, y], 100)
            return True
        return False

    def is_nest(self, x, y):
        return (x, y) in self.nest_area
    
    def consume_nest_food(self, amount=1):
        if self.nest_food_storage >= amount:
            self.nest_food_storage -= amount
            return True
        return False