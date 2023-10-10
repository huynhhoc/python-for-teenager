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
METEOR_RADIUS = 10
METEOR_SPEED = 5
# Load background image
background = pygame.image.load("universe2.jpg")
# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteorite Simulation")

# Create a list to store meteorite positions
meteorites = []

clock = pygame.time.Clock()

def draw_atmosphere_layers():
    # Define the colors for different atmosphere layers
    atmosphere_colors = [(50, 50, 200), (100, 100, 255), (150, 150, 255)]
    atmosphere_heights = [100, 200, 300]

    for i in range(len(atmosphere_colors)):
        pygame.draw.rect(screen, atmosphere_colors[i], (0, HEIGHT - atmosphere_heights[i], WIDTH, atmosphere_heights[i]))

def draw_meteorite_burning(meteor_x, meteor_y, burn_percent):
    # Calculate the radius based on burn_percent
    radius = int(METEOR_RADIUS * (1 - burn_percent))
    if radius < 1:
        return  # The meteorite is completely burned

    # Calculate the color based on burn_percent
    color = (255, int(255 - 255 * burn_percent), 0)

    pygame.draw.circle(screen, color, (meteor_x, meteor_y), radius)

running = True
screen.blit(background, (0, 0))  # Draw the background
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add a new meteorite with a random position
    meteor_x = random.randint(0, WIDTH)
    meteor_y = 0
    meteor_burn_percent = 0.0
    meteor_speed = METEOR_SPEED

    meteorites.append([meteor_x, meteor_y, meteor_burn_percent, meteor_speed])

    # Clear the screen
    screen.fill(BG_COLOR)
    screen.blit(background, (0, 0))  # Draw the background
    # Draw atmosphere layers
    draw_atmosphere_layers()

    # Move and draw meteorites
    for meteor in meteorites:
        meteor_x, meteor_y, meteor_burn_percent, meteor_speed = meteor[0], meteor[1], meteor[2], meteor[3]
        meteor_y += meteor_speed

        # Check if the meteorite has entered an atmosphere layer
        if HEIGHT - 100 <= meteor_y < HEIGHT:
            # Calculate burn_percent based on altitude within the atmosphere layer
            burn_percent = (meteor_y - (HEIGHT - 100)) / 100
            meteor_burn_percent = min(meteor_burn_percent + 0.005, 1.0)  # Increase burn_percent gradually
            meteor_speed *= 0.98  # Gradually reduce speed

        draw_meteorite_burning(meteor_x, meteor_y, meteor_burn_percent)

        # Update meteor position and attributes
        meteor[1] = meteor_y
        meteor[2] = meteor_burn_percent
        meteor[3] = meteor_speed

    # Remove meteorites that are off-screen
    meteorites = [meteor for meteor in meteorites if meteor[1] < HEIGHT]

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
