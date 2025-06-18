import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS
LIVE_COLOR = (255, 105, 180)  # Hot pink
DEAD_COLOR = (0, 0, 0)        # Black

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("cellular automata")

grid = [[0 for _ in range (COLS)] for _ in range(ROWS)]
for r in range(14, 16):
    for c in range(14, 16):
        grid[r][c]=1

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIVE_COLOR if grid[row][col] else DEAD_COLOR
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))


#main loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    win.fill(DEAD_COLOR)
    draw_grid()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
