import pygame
import random
from world.grid import Grid
from world.food import Food
from ants.colony import Colony
from ui.renderer import Renderer
from settings import *

# Init
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
clock = pygame.time.Clock()

# Setup
pher_home = Grid(GRID_WIDTH, GRID_HEIGHT)
pher_food = Grid(GRID_WIDTH, GRID_HEIGHT)
food = Food(GRID_WIDTH, GRID_HEIGHT)
colony = Colony(NEST_POSITION[0], NEST_POSITION[1], 50, pher_home, pher_food, GRID_WIDTH, GRID_HEIGHT)
renderer = Renderer(screen, pher_home, pher_food, colony.ants, food, (NEST_POSITION))

# Sprinkle initial food
for _ in range(10):
    fx = int(random.uniform(0, 400))
    fy = int(random.uniform(0, 400))
    food.add_food(fx, fy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        grid_x = mx // CELL_SIZE
        grid_y = my // CELL_SIZE
        food.add_food(grid_x, grid_y)

    # Update ants
    for ant in colony.ants:
        ant.step()

        xi, yi = ant.x, ant.y
        if ant.has_food:
            if colony.x - 2 <= xi <= colony.x + 2 and colony.y - 2 <= yi <= colony.y + 2:
                ant.has_food = False
                ant.home_pherormone = 100
        elif food.get_value(xi, yi):
            ant.has_food = True
            ant.food_pherormone = 100
            food.bite(xi, yi)

    pher_home.step()
    pher_food.step()

    renderer.draw()
    renderer.increment_iteration()

    pygame.display.flip()
    clock.tick(60)
