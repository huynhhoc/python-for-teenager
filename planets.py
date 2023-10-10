import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1580, 840
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
# Load background image
background = pygame.image.load("universe2.jpg")
# Constants for Đông Chí and Hạ Chí positions
dong_chi_position = (0, -200)
ha_chi_position = (0, 200)

# Moon data (not to scale)
# Adjust the moon's speed for approximately 12 orbits per year
moon_speed = 6.1 #360 / (365 * 24 * 60 * 60 / 12)
print ("Moon speed: ", moon_speed)
moon_data = {"name": "Moon", "color": (169, 169, 169), "radius": 5, "distance": 40, "angle": 0, "speed": moon_speed}

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Function to draw dashed lines
def draw_dashed_line(surface, color, start_pos, end_pos, width=1, dash_length=10):
    distance = end_pos - start_pos
    step = distance / dash_length
    for i in range(int(step)):
        if i % 2 == 0:
            pygame.draw.line(surface, color, (start_pos + i * dash_length), (start_pos + (i + 1) * dash_length), width)

# Function to draw planet orbits
def draw_planet_orbits():
    for planet in planet_data:
        pygame.draw.ellipse(screen, (50, 50, 50), (WIDTH // 2 - planet["distance"], HEIGHT // 2 - planet["distance"], 2 * planet["distance"], 2 * planet["distance"]), 1)

running = True
screen.blit(background, (0, 0))  # Draw the background
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    screen.blit(background, (0, 0))  # Draw the background

    draw_planet_orbits()  # Draw planet orbits

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

        # Update the Moon's position based on its orbital parameters
        moon_angle_rad = math.radians(moon_data["angle"])
        earth_x = WIDTH // 2 + planet_data[3]["distance"] * math.cos(math.radians(planet_data[3]["angle"]))
        earth_y = HEIGHT // 2 + planet_data[3]["distance"] * math.sin(math.radians(planet_data[3]["angle"]))
        moon_x = earth_x + moon_data["distance"] * math.cos(moon_angle_rad)
        moon_y = earth_y + moon_data["distance"] * math.sin(moon_angle_rad)

        # Draw the Moon
        pygame.draw.circle(screen, moon_data["color"], (int(moon_x), int(moon_y)), moon_data["radius"])

    # Create a text surface with the Moon name
    text_surface = font.render(moon_data["name"], True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(moon_x, moon_y - 15))
    screen.blit(text_surface, text_rect)

    moon_data["angle"] += moon_data["speed"]

    # Draw Đông Chí and Hạ Chí points
    pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2 - 200), 10)  # Đông Chí
    pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, HEIGHT // 2 + 200), 10)  # Hạ Chí

    # Add text for Đông Chí and Hạ Chí
    text_surface = font.render("Dong Chi - 21 hoac 22/12", True, (0, 0, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 220))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("Ha Chi - 20 hoac 21/6", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 220))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
