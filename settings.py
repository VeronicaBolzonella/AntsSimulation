import random 

# --- Window and Grid Settings ---
GRID_WIDTH = 200           # number of cells horizontally
GRID_HEIGHT = 200          # number of cells vertically
CELL_SIZE = 8              # pixel size of each grid cell

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

FPS = 30                   # Frames per second for the GUI

# --- Ant Settings ---
NUM_ANTS = 10
PHEROMONE_DROP_AMOUNT = 5
ANT_VIEW_RADIUS = 1        # How far ants can sense
ANT_SPEED = 1

# --- Pheromone Settings ---
INITIAL_PHEROMONE = 0.0
PHEROMONE_DECAY = 0.02   # evaporation rate per update
PHEROMONE_DIFFUSION = 0.1  # how fast pheromones spread
PHERORMONE_RADIUS = 4

# --- Nest Settings ---
NEST_POSITION = (50, 50)

# --- Food Settings ---
NUMBER_FOOD_CLUSTERS = 4
FOOD_LOCATIONS = [  # (x, y, amount)
    (120, 80, 5),
    (60, 150, 4),
    (160, 40, 6),
]

# --- Colors (RGB) ---
COLOR_BG = (128, 85, 0)
COLOR_GRID = (30, 30, 30)
COLOR_BASIC_ANT = (102, 0, 0)
COLOR_NEST = (0, 255, 0)
COLOR_FOOD = (255, 165, 0)
COLOR_TRAJECTORY_PHEROMONE = (163, 163, 194)
