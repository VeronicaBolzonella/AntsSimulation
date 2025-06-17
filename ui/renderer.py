import pygame
from settings import (
    GRID_WIDTH, GRID_HEIGHT, CELL_SIZE,
    COLOR_BG, COLOR_GRID, COLOR_BASIC_ANT,
    COLOR_FOOD, COLOR_NEST, COLOR_TRAJECTORY_PHEROMONE_FOOD, COLOR_TRAJECTORY_PHEROMONE_HOME, FOOD_LOCATIONS, PHERORMONE_RADIUS
)
from world.food import Food

class Renderer:
    def __init__(self, screen, grid, ants, food=None):
        self.screen = screen
        self.grid = grid
        self.ants = ants if not None else []
        self.font = pygame.font.SysFont('Arial', 16)
        self.iteration = 0


    def draw(self):
        self.screen.fill(COLOR_BG)

        # Draw cells
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                screen_x = x * CELL_SIZE
                screen_y = y * CELL_SIZE

                # Nest
                if self.grid.is_nest(x, y):
                    pygame.draw.rect(self.screen, COLOR_NEST, (screen_x, screen_y, CELL_SIZE, CELL_SIZE))

        # Draw food clusters
        self.draw_food()

        # Draw pherormones
        self.draw_pherormones()

        # Draw ants
        self.draw_ants()


        # Draw legend
        self.draw_legend()

    def draw_legend(self):
        legend_text = f"T: {self.iteration} "
        text_surface = self.font.render(legend_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))  # top-left corner

    def increment_iteration(self):
        self.iteration += 1
        
    def draw_food(self):
        for food in self.grid.food:
            # Intensity of color based on amount (cap at 255)
            if food.amount > 0:
                intensity = max(0, min(255, int((food.amount / 100) * 255)))
                color = (255, intensity, 0)  # fades from bright orange to dark

                for (x, y) in food.get_cells():
                    screen_x = x * CELL_SIZE
                    screen_y = y * CELL_SIZE
                    pygame.draw.rect(self.screen, color, (screen_x, screen_y, CELL_SIZE, CELL_SIZE))


    def draw_ants(self):
        for ant in self.ants:
            ax, ay = ant.get_position()
            ant_x = ax * CELL_SIZE
            ant_y = ay * CELL_SIZE
            pygame.draw.rect(self.screen, COLOR_BASIC_ANT, (ant_x, ant_y, CELL_SIZE, CELL_SIZE))

    def draw_pherormones(self):
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                strength = self.grid.pheromone_food[x, y]

                if strength > 0.01:
                    # Scale intensity to 0–255 (you can adjust this based on max value)
                    intensity = min(255, int(strength * 255))
                    color = COLOR_TRAJECTORY_PHEROMONE_FOOD  # blue channel for pheromone

                    screen_x = x * CELL_SIZE
                    screen_y = y * CELL_SIZE
                    pygame.draw.rect(self.screen, color, (screen_x, screen_y, PHERORMONE_RADIUS, PHERORMONE_RADIUS))
                
                strength = self.grid.pheromone_home[x, y]

                if strength > 0.01:
                    # Scale intensity to 0–255 (you can adjust this based on max value)
                    intensity = min(255, int(strength * 255))
                    color = COLOR_TRAJECTORY_PHEROMONE_HOME # blue channel for pheromone

                    screen_x = x * CELL_SIZE
                    screen_y = y * CELL_SIZE
                    pygame.draw.rect(self.screen, color, (screen_x, screen_y, PHERORMONE_RADIUS, PHERORMONE_RADIUS))