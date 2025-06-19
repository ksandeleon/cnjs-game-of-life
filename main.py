import pygame
import sys
import math
import random

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


class Sparkle:
    def __init__(self, center_x, center_y):
        self.x = center_x + random.randint(-40, 40)
        self.y = center_y + random.randint(-40, 40)
        self.radius = random.randint(6, 12)
        self.life = random.randint(40, 80)
        self.max_life = self.life
        self.dx = random.uniform(-0.3, 0.3)
        self.dy = random.uniform(-0.3, 0.3)

    def update(self):
        self.life -= 1
        self.x += self.dx
        self.y += self.dy

    def is_dead(self):
        return self.life <= 0

    def draw(self, surface):
        alpha = int(200 * (self.life / self.max_life))
        sparkle_color = (255, 255, 255, alpha)
        sparkle_surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(sparkle_surf, sparkle_color, (self.radius, self.radius), self.radius)
        surface.blit(sparkle_surf, (self.x - self.radius, self.y - self.radius))



def draw_grid(tick):
    pulse_color = get_pulse_color(tick)
    for row in range(ROWS):
        for col in range(COLS):
            color = pulse_color if grid[row][col] else DEAD_COLOR
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

def draw_message():
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("You light up my heart :>", True, (255, 182, 193))  # light pink
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 40))



#main loop
running = True
clock = pygame.time.Clock()
tick = 0
sparkles = []

while running:
    clock.tick(60)
    win.fill(DEAD_COLOR)

    draw_grid(tick)

    if random.random() <0.1:
        center_x = 15 * CELL_SIZE
        center_y = 16 * CELL_SIZE
        sparkles.append(Sparkle(center_x, center_y))


    for sparkle in sparkles[:]:
        sparkle.update()
        sparkle.draw(win)
        if sparkle.is_dead():
            sparkles.remove(sparkle)

    draw_message()
    pygame.display.flip()

    tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
