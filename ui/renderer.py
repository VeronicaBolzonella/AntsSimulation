import pygame
from settings import (
    GRID_WIDTH, GRID_HEIGHT, CELL_SIZE,
    COLOR_BG, COLOR_GRID, COLOR_BASIC_ANT,
    COLOR_FOOD, COLOR_NEST, COLOR_TRAJECTORY_PHEROMONE_FOOD, COLOR_TRAJECTORY_PHEROMONE_HOME, FOOD_LOCATIONS, PHERORMONE_RADIUS
)
from world.food import Food

class Renderer:
    def __init__(self, screen, pheromone_home, pheromone_food, ants, food, nest_pos):
        self.screen = screen
        self.pher_home = pheromone_home
        self.pher_food = pheromone_food
        self.ants = ants
        self.food = food
        self.nest_pos = nest_pos  # (x, y)
        self.font = pygame.font.SysFont('Arial', 16)
        self.iteration = 0

    def draw(self):
        self.screen.fill(COLOR_BG)

        self.draw_nest()
        self.draw_food()
        self.draw_pheromones()
        self.draw_ants()
        self.draw_legend()

    def draw_legend(self):
        legend_text = f"T: {self.iteration} "
        text_surface = self.font.render(legend_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))

    def increment_iteration(self):
        self.iteration += 1

    def draw_nest(self):
        x, y = self.nest_pos
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                px = (x + dx) * CELL_SIZE
                py = (y + dy) * CELL_SIZE
                pygame.draw.rect(self.screen, COLOR_NEST, (px, py, CELL_SIZE, CELL_SIZE))

    def draw_food(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.food.get_value(x, y):
                    screen_x = x * CELL_SIZE
                    screen_y = y * CELL_SIZE
                    pygame.draw.rect(self.screen, COLOR_FOOD, (screen_x, screen_y, CELL_SIZE, CELL_SIZE))

    def draw_ants(self):
        for ant in self.ants:
            x, y = ant.x, ant.y
            px = x * CELL_SIZE
            py = y * CELL_SIZE
            color = COLOR_FOOD if ant.has_food else COLOR_BASIC_ANT
            pygame.draw.rect(self.screen, color, (px, py, CELL_SIZE, CELL_SIZE))

    def draw_pheromones(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                food_strength = self.pher_food.get_value(x, y)
                home_strength = self.pher_home.get_value(x, y)

                if food_strength > 0.01:
                    intensity = min(255, int((food_strength / 100) * 255))
                    color = COLOR_TRAJECTORY_PHEROMONE_FOOD
                    px = x * CELL_SIZE
                    py = y * CELL_SIZE
                    pygame.draw.rect(self.screen, color, (px, py, PHERORMONE_RADIUS, PHERORMONE_RADIUS))

                if home_strength > 0.01:
                    intensity = min(255, int((home_strength / 100) * 255))
                    color = COLOR_TRAJECTORY_PHEROMONE_HOME
                    px = x * CELL_SIZE
                    py = y * CELL_SIZE
                    pygame.draw.rect(self.screen, color, (px, py, PHERORMONE_RADIUS, PHERORMONE_RADIUS))
