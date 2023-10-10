import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (0, 0, 0)
METEOR_COLOR = (255, 0, 0)
METEOR_SPEED = 5
# Load background image
background = pygame.image.load("universe2.jpg")
# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteorite Simulation")

# Create a list to store meteorite positions
meteorites = []

clock = pygame.time.Clock()

running = True
screen.blit(background, (0, 0))  # Draw the background
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
    screen.blit(background, (0, 0))  # Draw the background
    # Move and draw meteorites
    for meteor in meteorites:
        meteor[1] += METEOR_SPEED
        pygame.draw.circle(screen, METEOR_COLOR, (meteor[0], meteor[1]), 10)  # Adjust meteorite size as needed

    # Remove meteorites that are off-screen
    meteorites = [meteor for meteor in meteorites if meteor[1] < HEIGHT]

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
