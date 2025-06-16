import pygame
from settings import *
from world.grid import Grid
from ants.basic_ant import Ant
from ui.renderer import Renderer

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize world grid with shared food dictionary
    grid = Grid(GRID_WIDTH, GRID_HEIGHT, FOOD_LOCATIONS)

    
    # Set up renderer
    renderer = Renderer(screen, grid)

    running = True
    while running:
        # Event handling (including click-to-place-food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw world
        renderer.increment_iteration()
        renderer.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
