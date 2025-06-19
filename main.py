import pygame
import sys
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS
DEAD_COLOR = (0, 0, 0)        # Black


def get_pulse_color(tick):
    pulse = (math.sin(tick*0.05)+1)/2
    r = int(255)
    g = int(105+pulse*(182-105))
    b = int(180 + pulse * (255-180))
    return (r,g,b)


heart_cells = [
    (13, 12), (13, 13), (13, 16), (13, 17),
    (14, 11), (14, 14), (14, 15), (14, 18),
    (15, 10), (15, 19),
    (16, 10), (16, 19),
    (17, 11), (17, 18),
    (18, 12), (18, 17),
    (19, 13), (19, 16),
    (20, 14), (20, 15),
]

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("cellular automata")

grid = [[0 for _ in range (COLS)] for _ in range(ROWS)]
for r in range(14, 16):
    for c in range(14, 16):
        grid[r][c]=1

for row, col in heart_cells:
    grid[row][col] = 1


def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIVE_COLOR if grid[row][col] else DEAD_COLOR
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

def draw_message():
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("You light up my heart 💖", True, (255, 182, 193))  # light pink
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 40))



#main loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    win.fill(DEAD_COLOR)
    draw_grid()
    draw_message()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
