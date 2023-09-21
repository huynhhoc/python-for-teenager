import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
MOONCAKE_SIZE = 30
BASKET_WIDTH = 100
BASKET_HEIGHT = 20
MOONCAKE_SPEED = 0.5
MAX_MOONCAKES = 5
GAME_DURATION = 30  # in seconds

# Initialize Sound
pygame.mixer.init()

# Load Sound Files
catch_sound = pygame.mixer.Sound("catch.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
nhac_tet_trungthu = pygame.mixer.Sound("tettrungthu.mp3")

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mooncake Catcher")

# Load images
background = pygame.image.load("background.jpg")
basket_img = pygame.image.load("basket.png")
mooncake_img = pygame.image.load("mooncake.png")

# Resize images
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))
mooncake_img = pygame.transform.scale(mooncake_img, (MOONCAKE_SIZE, MOONCAKE_SIZE))

# Initialize game variables
basket_x = (WIDTH - BASKET_WIDTH) // 2
basket_y = HEIGHT - BASKET_HEIGHT
mooncakes = []
score = 0
start_time = time.time()
game_over = False  # New game over state

# Font for displaying score
font = pygame.font.Font(None, 36)

# Music and picture variables
play_music = True
pictures = ["tettrungthu1.jpg", "tettrungthu2.jpg", "tettrungthu3.jpg", "tettrungthu4.jpg",
            "tettrungthu5.jpg","tettrungthu6.jpg","tettrungthu7.jpg","tettrungthu8.jpg",
            "tettrungthu9.jpg","tettrungthu10.jpg","tettrungthu11.jpg"]  # Add your picture file paths here
current_picture = 0  # Initialize the current picture index
display_time = 10  # Display each picture for 5 seconds

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the basket with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= MOONCAKE_SPEED
    if keys[pygame.K_RIGHT]:
        basket_x += MOONCAKE_SPEED

    # Keep the basket within the screen boundaries
    basket_x = max(0, min(WIDTH - BASKET_WIDTH, basket_x))

    # Add new mooncakes
    if not game_over and len(mooncakes) < MAX_MOONCAKES and random.random() < 0.1:
        mooncake_x = random.randint(0, WIDTH - MOONCAKE_SIZE)
        mooncake_y = 0
        mooncakes.append([mooncake_x, mooncake_y])

    # Update mooncake positions
    for mooncake in mooncakes:
        mooncake[1] += MOONCAKE_SPEED * 0.7

    # Remove mooncakes that are out of the screen
    mooncakes = [mooncake for mooncake in mooncakes if mooncake[1] < HEIGHT]

    # Check for collisions
    for mooncake in mooncakes:
        if (
            not game_over
            and basket_x < mooncake[0] < basket_x + BASKET_WIDTH
            and basket_y < mooncake[1] < basket_y + BASKET_HEIGHT
        ):
            mooncakes.remove(mooncake)
            score += 1
            catch_sound.play()

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw the basket
    screen.blit(basket_img, (basket_x, basket_y))

    # Draw the mooncakes
    for mooncake in mooncakes:
        screen.blit(mooncake_img, (mooncake[0], mooncake[1]))

    # Draw the score
    score_text = font.render(f"So Banh Trung Thu: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Check for game over
    elapsed_time = time.time() - start_time
    if elapsed_time >= GAME_DURATION and not game_over:
        game_over = True
        game_over_sound.play()  # Play game over sound
        play_music = True  # Set play_music flag to True when the game is over

    # Display game over message and pictures with music
    if game_over:
        if play_music:
            # Play music
            nhac_tet_trungthu.play()
            play_music = False  # Set play_music flag to False to avoid repeating music

        if current_picture < len(pictures):
            # Load and display the current picture
            current_image = pygame.image.load(pictures[current_picture])
            current_image = pygame.transform.scale(current_image, (WIDTH, HEIGHT))
            screen.blit(current_image, (0, 0))

            # Display the text
            game_over_text = font.render("Ba chuc tui con Trung Thu Vui, Ngoan, Cham Chi", True, (255, 255, 0))
            screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, 30))

            pygame.display.flip()

            # Wait for the specified display time
            pygame.time.wait(display_time * 1000)

            # Move to the next picture
            current_picture += 1
        else:
            # If all pictures are displayed, exit the game loop
            running = False

    # Refresh the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
