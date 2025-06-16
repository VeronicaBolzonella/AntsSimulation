import pygame
from settings import *
from world.grid import Grid
from ants.basic_ant import Ant
from ui.renderer import Renderer

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    ants = [Ant(grid) for _ in range(NUM_ANTS)]
    renderer = Renderer(screen, grid, ants)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update world
        for ant in ants:
            ant.update()

        # Remove dead ants
        ants = [ant for ant in ants if ant.alive]

        grid.evaporate_pheromones()
        
        # Draw
        renderer.increment_iteration()
        renderer.draw()
        pygame.display.flip()
        clock.tick(FPS)
        

    pygame.quit()

if __name__ == "__main__":
    main()
