import pygame
import sys
import random
import time
# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 1200, 625
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid-Autumn Festival")

# Màu sắc
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Hình dạng lồng đèn
lantern_shapes = {
    "fish": [
        (0, 50),
        (25, 0),
        (50, 50),
        (25, 100)
    ],
    "star": [
        (0, 50),
        (25, 0),
        (50, 50),
        (25, 100),
        (0, 50),
        (50, 50)
    ],
    "rabbit": [
        (0, 50),
        (25, 0),
        (50, 50),
        (25, 100),
        (0, 50),
        (50, 50),
        (0, 0),
        (50, 0)
    ],
    "sun": [  # Thêm điểm cụ thể cho lồng đèn mặt trời
        (25, 0),
        (0, 50),
        (25, 100),
        (50, 50),
        (25, 25),
        (50, 0),
        (0, 0),
        (50, 100),
        (0, 100)
    ],
    "zodiac": {
        "Pisces": [  # Thêm điểm cụ thể cho lồng đèn Song Ngư
            (0, 25),
            (25, 0),
            (50, 25),
            (25, 50)
        ],
        "Aries": [  # Thêm điểm cụ thể cho lồng đèn Bạch Dương
            (0, 0),
            (50, 0),
            (25, 25),
            (50, 50),
            (0, 50)
        ],
        # Thêm điểm cụ thể cho các biểu tượng hoàng đạo khác ở đây
    }
}
# Message variables
message = "Happy Mid-Autumn Festival"
message_font = pygame.font.Font(None, 36)
message_color = YELLOW
message_x, message_y = 0, 0
message_visible = True
message_timer = 0

def show_message():
    global message_x, message_y, message_visible, message_timer
    message_x = random.randint(0, WIDTH - 200)
    message_y = random.randint(0, HEIGHT - 50)
    message_visible = True
    message_timer = time.time()
    
# Khởi tạo danh sách lồng đèn ban đầu với các loại mới
lanterns = [
    (i * 100, random.randint(100, 300), random.choice(["fish", "star", "rabbit", "sun"])) 
    for i in range(8)
]

# Thêm hoàng đạo vào danh sách lồng đèn ban đầu
for zodiac in lantern_shapes["zodiac"].keys():
    lanterns.append((random.randint(0, 800), random.randint(100, 400), zodiac))

# Hàm vẽ một loại lồng đèn cụ thể
def draw_custom_lantern(x, y, shape):
    lantern_shape = lantern_shapes.get(shape)
    if lantern_shape:
        pygame.draw.polygon(screen, YELLOW, [(x + point[0], y + point[1]) for point in lantern_shape])
        pygame.draw.circle(screen, BLUE, (x + 25, y + 50), 15)

# Load background image
background = pygame.image.load("tettrungthu14.jpg")

# Hàm vẽ đêm hội Trung thu
def draw_trung_thu(lanterns):
    screen.blit(background, (0, 0))  # Draw the background first
    for lantern in lanterns:
        x, y, shape = lantern
        draw_custom_lantern(x, y, shape)

if __name__ == '__main__':
    # Khởi tạo danh sách lồng đèn ban đầu
    lanterns = [(i * 100, random.randint(100, 400), random.choice(["fish", "star", "rabbit", "sun"])) for i in range(8)]
    # Khởi tạo nhạc và hình nền
    nhac_tet_trungthu = pygame.mixer.Sound("tettrungthu.mp3")
    nhac_tet_trungthu.set_volume(0.5)  # Adjust the volume level (0.0 to 1.0)
    pygame.mixer.init(frequency=40100, size=-16, channels=2, buffer=4096)
    nhac_tet_trungthu.play()
    # Vòng lặp chính
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        current_time = time.time()

        if message_visible and current_time - message_timer >= 15:
            message_visible = False
            wait_time = random.randint(0, 1)  # Wait for 0 to 1 seconds
            time.sleep(wait_time)
            show_message()
        # Di chuyển lồng đèn từ trái sang phải
        for i in range(len(lanterns)):
            x, y, shape = lanterns[i]
            lanterns[i] = (x + 5, y, shape)
            if x > WIDTH:
                lanterns[i] = (0, random.randint(100, 400), random.choice(["fish", "star", "rabbit"]))
        
        draw_trung_thu(lanterns)

        if message_visible:
           message_text = message_font.render(message, True, message_color)
           screen.blit(message_text, (message_x, message_y))
            
        pygame.display.update()
        clock.tick(30)

    # Kết thúc Pygame
    pygame.quit()
    sys.exit()
