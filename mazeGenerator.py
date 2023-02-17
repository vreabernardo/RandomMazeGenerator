import pygame
import random
from time import sleep
WIDTH = 400
HEIGHT = 400
W = 40
ROWS = HEIGHT // W
COLS = WIDTH // W

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")


def index(i, j, cols, rows):
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
        return None
    return i + j * cols

def remove_walls(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False

    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False


# Define Cell class
class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def check_neighbours(self):
        neighbours = []

        top = index(self.i, self.j - 1, COLS, ROWS)
        right = index(self.i + 1, self.j, COLS, ROWS)
        bottom = index(self.i, self.j + 1, COLS, ROWS)
        left = index(self.i - 1, self.j, COLS, ROWS)

        if top is not None and not grid[top].visited:
            neighbours.append(grid[top])
        if right is not None and not grid[right].visited:
            neighbours.append(grid[right])
        if bottom is not None and not grid[bottom].visited:
            neighbours.append(grid[bottom])
        if left is not None and not grid[left].visited:
            neighbours.append(grid[left])

        if len(neighbours) > 0:
            r = random.randint(0, len(neighbours) - 1)
            return neighbours[r]
        else:
            return None

    def highlight(self):
        x = self.i * W
        y = self.j * W
        pygame.draw.rect(SCREEN, GREEN, (x, y, W, W))

    def show(self):
        x = self.i * W
        y = self.j * W

        if self.visited:
            pygame.draw.rect(SCREEN, (112, 41, 99), (x, y, W, W))

        if self.walls[0]:
            pygame.draw.line(SCREEN, WHITE, (x, y), (x + W, y))
        if self.walls[1]:
            pygame.draw.line(SCREEN, WHITE, (x + W, y), (x + W, y + W))
        if self.walls[2]:
            pygame.draw.line(SCREEN, WHITE, (x + W, y + W), (x, y + W))
        if self.walls[3]:
            pygame.draw.line(SCREEN, WHITE, (x, y + W), (x, y))


# Create grid of cells
grid = [Cell(i, j) for j in range(ROWS) for i in range(COLS)]
stack = []

current = grid[0]

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw grid
    for cell in grid:
        cell.show()

    # Highlight current cell
    current.visited = True
    current.highlight()

    # Get next cell and modify grid
    #1
    next_cell = current.check_neighbours()
    if next_cell:
        next_cell.visited = True
        #2
        stack.append(current)
        #3
        remove_walls(current, next_cell)
        #4
        current = next_cell

    elif len(stack) > 0:
        current = stack.pop()

    pygame.display.update()

# Remove Pygame on exit
pygame.quit()
