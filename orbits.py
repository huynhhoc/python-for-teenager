import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Planet data (not to scale)
planet_data = [
    {"name": "Sun", "color": (255, 255, 0), "radius": 50, "distance": 0, "angle": 0, "speed": 0},
    {"name": "Mercury", "color": (169, 169, 169), "radius": 10, "distance": 100, "angle": 0, "speed": 1},
    {"name": "Venus", "color": (255, 69, 0), "radius": 15, "distance": 150, "angle": 0, "speed": 0.75},
    {"name": "Earth", "color": (0, 0, 255), "radius": 15, "distance": 200, "angle": 0, "speed": 0.5},
    {"name": "Mars", "color": (255, 0, 0), "radius": 12, "distance": 250, "angle": 0, "speed": 0.4},
    {"name": "Jupiter", "color": (255, 165, 0), "radius": 30, "distance": 350, "angle": 0, "speed": 0.2},
    {"name": "Saturn", "color": (255, 255, 0), "radius": 25, "distance": 450, "angle": 0, "speed": 0.15},
    {"name": "Uranus", "color": (0, 255, 255), "radius": 20, "distance": 550, "angle": 0, "speed": 0.1},
    {"name": "Neptune", "color": (0, 0, 128), "radius": 18, "distance": 650, "angle": 0, "speed": 0.08},
    # Add more planets here
]

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    for planet in planet_data:
        angle_rad = math.radians(planet["angle"])
        x = WIDTH // 2 + planet["distance"] * math.cos(angle_rad)
        y = HEIGHT // 2 + planet["distance"] * math.sin(angle_rad)
        
        # Draw planet circle
        pygame.draw.circle(screen, planet["color"], (int(x), int(y)), planet["radius"])
        
        # Create a text surface with the planet name
        text_surface = font.render(planet["name"], True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x, y - 25))  # Adjust the vertical position of the text
        
        # Draw planet name above the planet
        screen.blit(text_surface, text_rect)

        planet["angle"] += planet["speed"]

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
