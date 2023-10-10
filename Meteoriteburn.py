import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (0, 0, 0)
METEOR_COLOR = (255, 0, 0)
METEOR_SPEED = 5

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteorite Simulation")

# Create a list to store meteorite positions
meteorites = []

clock = pygame.time.Clock()

def draw_atmosphere_layer():
    # Simple atmosphere layer effect
    pygame.draw.rect(screen, (50, 50, 200), (0, HEIGHT - 100, WIDTH, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add a new meteorite with a random position
    meteor_x = random.randint(0, WIDTH)
    meteor_y = 0
    meteorites.append([meteor_x, meteor_y])

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw atmosphere layer
    draw_atmosphere_layer()

    # Move and draw meteorites
    for meteor in meteorites:
        meteor_x, meteor_y = meteor[0], meteor[1]
        meteor_y += METEOR_SPEED

        # Check if the meteorite has entered the atmosphere layer
        if HEIGHT - 100 <= meteor_y:
            # Simulate burning by changing the color to orange
            pygame.draw.circle(screen, (255, 165, 0), (meteor_x, HEIGHT - 100), 10)
        else:
            pygame.draw.circle(screen, METEOR_COLOR, (meteor_x, meteor_y), 10)  # Adjust meteorite size as needed

        # Update meteor position
        meteor[1] = meteor_y

    # Remove meteorites that are off-screen
    meteorites = [meteor for meteor in meteorites if meteor[1] < HEIGHT]

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
