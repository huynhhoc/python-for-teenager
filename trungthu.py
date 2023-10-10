import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ đồ họa
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Đêm hội Trung thu")

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


# Khởi tạo danh sách lồng đèn ban đầu với các loại mới
lanterns = [
    (i * 100, random.randint(100, 400), random.choice(["fish", "star", "rabbit", "sun"])) 
    for i in range(8)
]

# Thêm hoàng đạo vào danh sách lồng đèn ban đầu
for zodiac in lantern_shapes["zodiac"].keys():
    lanterns.append((random.randint(0, 700), random.randint(100, 400), zodiac))

# Hàm vẽ một loại lồng đèn cụ thể
def draw_custom_lantern(x, y, shape):
    lantern_shape = lantern_shapes.get(shape)
    if lantern_shape:
        pygame.draw.polygon(screen, YELLOW, [(x + point[0], y + point[1]) for point in lantern_shape])
        pygame.draw.circle(screen, BLUE, (x + 25, y + 50), 15)

# Hàm vẽ đêm hội Trung thu
def draw_trung_thu(lanterns):
    screen.fill(WHITE)
    for lantern in lanterns:
        x, y, shape = lantern
        draw_custom_lantern(x, y, shape)

# Khởi tạo danh sách lồng đèn ban đầu
lanterns = [(i * 100, random.randint(100, 400), random.choice(["fish", "star", "rabbit"])) for i in range(8)]

# Vòng lặp chính
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển lồng đèn từ trái sang phải
    for i in range(len(lanterns)):
        x, y, shape = lanterns[i]
        lanterns[i] = (x + 5, y, shape)
        if x > 800:
            lanterns[i] = (0, random.randint(100, 400), random.choice(["fish", "star", "rabbit"]))

    draw_trung_thu(lanterns)
    pygame.display.update()
    clock.tick(30)

# Kết thúc Pygame
pygame.quit()
sys.exit()
