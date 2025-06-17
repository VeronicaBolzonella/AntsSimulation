import pygame
from settings import *
from world.grid import Grid
from ants.ant import Ant
from ui.renderer import Renderer
from world.food import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize world grid with shared food dictionary
    food = [Food(x, y, amount) for (x, y, amount) in FOOD_LOCATIONS]
    grid = Grid(GRID_WIDTH, GRID_HEIGHT, food)

    ants = []
    # Initialize ants
    for ant in range(NUM_ANTS):
        ants.append(Ant(grid, ANT_SPEED))
    
    # Set up renderer
    renderer = Renderer(screen, grid, ants)

    running = True
    while running:
        # Event handling (including click-to-place-food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = mouse_x // CELL_SIZE
                    grid_y = mouse_y // CELL_SIZE

                    new_food = Food(grid_x, grid_y)

                    grid.food.append(new_food)

        for ant in ants:
            ant.update()

        grid.update_pheromones()

        # Draw world
        renderer.increment_iteration()
        renderer.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
