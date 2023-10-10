import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
BG_COLOR = (0, 0, 0)
ORBIT_COLOR = (255, 255, 255)
TOUTATIS_COLOR = (255, 0, 0)
ORBIT_RADIUS = 200  # Adjust the orbit radius as needed
TOUTATIS_RADIUS = 10  # Adjust the size of Toutatis as needed

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Toutatis Orbit Visualization")

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Function to draw planet orbits
def draw_orbit():
    pygame.draw.circle(screen, ORBIT_COLOR, (WIDTH // 2, HEIGHT // 2), ORBIT_RADIUS, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    draw_orbit()  # Draw Toutatis's orbit

    # Calculate Toutatis's position based on its orbit
    angle_rad = math.radians(pygame.time.get_ticks() / 10)  # Adjust the speed of rotation
    x = WIDTH // 2 + ORBIT_RADIUS * math.cos(angle_rad)
    y = HEIGHT // 2 + ORBIT_RADIUS * math.sin(angle_rad)

    # Draw Toutatis at its current position
    pygame.draw.circle(screen, TOUTATIS_COLOR, (int(x), int(y)), TOUTATIS_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
