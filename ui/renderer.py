import pygame
from settings import (
    GRID_WIDTH, GRID_HEIGHT, CELL_SIZE,
    COLOR_BG, COLOR_GRID, COLOR_BASIC_ANT,
    COLOR_FOOD, COLOR_NEST, COLOR_PHEROMONE
)

class Renderer:
    def __init__(self, screen, grid, ants):
        self.screen = screen
        self.grid = grid
        self.ants = ants
        self.font = pygame.font.SysFont('Arial', 16)
        self.iteration = 0

    def draw(self):
        self.screen.fill(COLOR_BG)

        # Draw cells
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                screen_x = x * CELL_SIZE
                screen_y = y * CELL_SIZE

                # Pheromones
                pheromone = self.grid.pheromone[x, y]
                if pheromone > 1:
                    intensity = min(int(pheromone), 255)
                    color = (0, 0, intensity)
                    pygame.draw.rect(self.screen, color, (screen_x, screen_y, CELL_SIZE, CELL_SIZE))

                # Food
                if self.grid.food[x, y] > 0:
                    pygame.draw.rect(self.screen, COLOR_FOOD, (screen_x, screen_y, CELL_SIZE, CELL_SIZE))

                # Nest
                if self.grid.is_nest(x, y):
                    pygame.draw.rect(self.screen, COLOR_NEST, (screen_x, screen_y, CELL_SIZE, CELL_SIZE))

        # Draw ants
        for ant in self.ants:
            ax, ay = ant.get_position()
            ant_x = ax * CELL_SIZE
            ant_y = ay * CELL_SIZE
            pygame.draw.rect(self.screen, COLOR_BASIC_ANT, (ant_x, ant_y, CELL_SIZE, CELL_SIZE))

        # Draw legend
        self.draw_legend()

    def draw_legend(self):
        legend_text = f"N: {len(self.ants)}    T: {self.iteration}    F: {self.grid.nest_food_storage}"
        text_surface = self.font.render(legend_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))  # top-left corner

    def increment_iteration(self):
        self.iteration += 1
