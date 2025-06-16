import random
from settings import NEST_POSITION, PHEROMONE_DROP_AMOUNT
from utils.helpers import get_neighbors

class Ant:
    def __init__(self, grid):
        # Start all ants at the nest
        self.x, self.y = random.choice(list(grid.nest_area))
        self.grid = grid
        self.food_tick_counter = 10
        self.state = "FORAGING"   
        self.has_food = False

        self.alive = True

    def update(self):
        if not self.alive:
            return

        self.food_tick_counter += 1
        self.try_to_feed_if_in_nest()

        if self.state == "FORAGING":
            self.foraging_behavior()
        elif self.state == "RETURNING":
            self.returning_behavior()

        self.check_starvation()


    def foraging_behavior(self):
        neighbors = get_neighbors(self.x, self.y, self.grid.width, self.grid.height)

        if self.food_tick_counter > 50:
            self.state = "RETURNING"

        # Step 1: look for food nearby
        for nx, ny in neighbors:
            if self.grid.food[nx, ny] > 0:
                took = self.grid.take_food(nx, ny)
                if took:
                    self.food_tick_counter = 0
                    self.has_food = True
                    self.state = "RETURNING"
                    return

        # Step 2: if in nest and no food found, move randomly out
        if self.grid.is_nest(self.x, self.y):
            # Try to leave nest
            non_nest_neighbors = [pos for pos in neighbors if not self.grid.is_nest(*pos)]
            if non_nest_neighbors:
                self.x, self.y = random.choice(non_nest_neighbors)
            return

        # Step 3: if outside nest, follow weak pheromones (exploration)
        next_pos = self.pick_move_by_pheromone(neighbors, seek_high=False)
        if next_pos:
            self.x, self.y = next_pos

    def returning_behavior(self):
        # Drop pheromone
        self.grid.deposit_pheromone(self.x, self.y, PHEROMONE_DROP_AMOUNT)

        # Move toward nest
        neighbors = get_neighbors(self.x, self.y, self.grid.width, self.grid.height)
        next_pos = self.pick_move_toward_nest(neighbors)
        if next_pos:
            self.x, self.y = next_pos

        if self.grid.is_nest(self.x, self.y):
            self.has_food = False
            self.grid.nest_food_storage += 100
            self.state = "FORAGING"

    def try_to_feed_if_in_nest(self):
        if self.grid.is_nest(self.x, self.y):
            if self.food_tick_counter >= 10:
                ate = self.grid.consume_nest_food(1)
                if ate:
                    self.food_tick_counter = 0

    def check_starvation(self):
        if self.food_tick_counter > 100:
            self.alive = False

    def pick_move_by_pheromone(self, neighbors, seek_high=True):
        # Bias toward lowest (for foraging) or highest (for returning) pheromone
        best_val = -float('inf') if seek_high else float('inf')
        candidates = []

        for nx, ny in neighbors:
            level = self.grid.get_pheromone_level(nx, ny)
            if (seek_high and level > best_val) or (not seek_high and level < best_val):
                best_val = level
                candidates = [(nx, ny)]
            elif level == best_val:
                candidates.append((nx, ny))

        return random.choice(candidates) if candidates else None

    def pick_move_toward_nest(self, neighbors):
        # Prefer moves that bring us closer to the nest center
        def distance(pos):
            dx = pos[0] - self.grid.nest_x
            dy = pos[1] - self.grid.nest_y
            return dx*dx + dy*dy

        sorted_moves = sorted(neighbors, key=distance)
        return sorted_moves[0] if sorted_moves else None

    def get_position(self):
        return self.x, self.y
