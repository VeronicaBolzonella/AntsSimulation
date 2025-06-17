import random 

# --- Window and Grid Settings ---
GRID_WIDTH = 400           # number of cells horizontally
GRID_HEIGHT = 400          # number of cells vertically
CELL_SIZE = 6              # pixel size of each grid cell

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

FPS = 20                   # Frames per second for the GUI

# --- Ant Settings ---
NUM_ANTS = 10
PHEROMONE_DROP_AMOUNT = 5
ANT_VIEW_RADIUS = 10        # How far ants can sense
ANT_SPEED = 1

# --- Pheromone Settings ---
INITIAL_PHEROMONE = 0.0
PHEROMONE_DECAY_FOOD = 0.04   # evaporation rate per update
PHEROMONE_DECAY_HOME = 0.01   # evaporation rate per update

PHEROMONE_DIFFUSION = 0.1  # how fast pheromones spread
PHERORMONE_RADIUS = 3

# --- Nest Settings ---
NEST_POSITION = (50, 50)

# --- Food Settings ---
NUMBER_FOOD_CLUSTERS = 4
FOOD_LOCATIONS = [  # (x, y, amount)
    (120, 80, 100),
    (60, 150, 40),
    (160, 40, 60),
]

# --- Colors (RGB) ---
COLOR_BG = (128, 85, 0)
COLOR_GRID = (30, 30, 30)
COLOR_BASIC_ANT = (102, 0, 0)
COLOR_NEST = (0, 255, 0)
COLOR_FOOD = (255, 165, 0)
COLOR_TRAJECTORY_PHEROMONE_FOOD = (163, 163, 194)
COLOR_TRAJECTORY_PHEROMONE_HOME = (61, 61, 92)

