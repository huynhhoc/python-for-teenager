import pygame
import sys
import random
import time
# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 1200, 625
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Đêm hội Trung thu")

# Màu sắc
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
# Thêm các biến liên quan đến viên bi
bullet_x = WIDTH // 2
bullet_y = HEIGHT
bullet_speed = 10
bullet_fired = False
# Hình dạng lồng đèn
lantern_shapes = {
    "fish": [
        (0, 50),
        (25, 0),
        (50, 50),
        (25, 100)
    ],
    "star": [
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
message = "Ba chuc tui con choi trung thu vui ve"
message_font = pygame.font.Font(None, 36)
message_color = YELLOW
message_x, message_y = 0, 0
message_visible = True
message_timer = 0

# Add variables for the gun
gun_x = WIDTH // 2
gun_y = HEIGHT - 50
gun_speed = 5
bullets = []  # List to store bullets

# Thêm biến kiểm tra trò chơi kết thúc
game_over = False

# Danh sách bánh trung thu
mooncakes = []

# Thêm hình ảnh bánh trung thu
# Khai báo biến cho màn bánh trung thu
mooncake_wave = 20  # Số lượng bánh trung thu trong mỗi màn
mooncakes = []  # Danh sách bánh trung thu
mooncake_frequency = 2  # Tần suất rơi của bánh trung thu (tùy chỉnh)
monecake_loop = 15 # Số lượt bánh trung thu rơi xuống
mooncake_speed = 2  # Tốc độ rơi của bánh trung thu
mooncake_width = 50  # Your desired width
mooncake_height = 50  # Your desired height
mooncake_image = pygame.image.load("mooncake.png")
mooncake_image = pygame.transform.scale(mooncake_image, (mooncake_width, mooncake_height))


def draw_gun(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), 15)
    pygame.draw.rect(screen, YELLOW, (x - 5, y + 10, 10, 20))

def draw_bullet(x, y):
    pygame.draw.circle(screen, BLUE, (x, y), 5)

# Hàm kiểm tra va chạm giữa viên bi và lồng đèn
def check_collision(bullet_x, bullet_y, lantern_x, lantern_y):
    distance = pygame.math.Vector2(lantern_x - bullet_x, lantern_y - bullet_y).length()
    return distance < 20  # Khoảng cách nhỏ hơn bán kính lồng đèn
  
# Hàm vẽ một loại lồng đèn cụ thể
def draw_custom_lantern(x, y, shape):
    lantern_shape = lantern_shapes.get(shape)
    if lantern_shape:
        if shape == "star":
            pygame.draw.polygon(screen, YELLOW, [(x + point[0], y + point[1]) for point in lantern_shape])
        else:
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
def generate_mooncakes():
    mooncakes = []
    for _ in range(mooncake_wave):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(-100, -50)
        mooncakes.append([x, y])
    return mooncakes
if __name__ == '__main__':
    # Khởi tạo danh sách lồng đèn ban đầu
    lanterns = [(i * 100, random.randint(100, 400), random.choice(["fish", "star", "sun"])) for i in range(20)]
    print("type of lanterns: ", type(lanterns))
    # Thêm lồng đèn con thỏ vào danh sách

    lanterns.append((random.randint(0, 800), random.randint(100, 400), "rabbit"))

    # Thêm hoàng đạo vào danh sách lồng đèn ban đầu
    for zodiac in lantern_shapes["zodiac"].keys():
        lanterns.append((random.randint(0, 800), random.randint(100, 400), zodiac))

    # Khởi tạo nhạc và hình nền
    nhac_tet_trungthu = pygame.mixer.Sound("tettrungthu.mp3")
    nhac_tet_trungthu.set_volume(0.5)  # Adjust the volume level (0.0 to 1.0)
    pygame.mixer.init(frequency=40100, size=-16, channels=2, buffer=4096)
    nhac_tet_trungthu.play()
    # Vòng lặp chính
    running = True
    # Thêm biến để kiểm tra xem còn lồng đèn nào không
    lanterns_remaining = True
    # Thêm biến để kết thúc chương trình
    mooncake_falling = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bullets.append([gun_x, gun_y])  # Add a new bullet position
                elif event.key == pygame.K_LEFT:
                    gun_x -= gun_speed
                elif event.key == pygame.K_RIGHT:
                    gun_x += gun_speed

        current_time = time.time()

        if lanterns_remaining:  # Kiểm tra xem còn lồng đèn nào không
            # Tạo danh sách phụ để lưu trữ các lồng đèn cần loại bỏ
            lanterns_to_remove = []
            for i in range(len(lanterns)):
                x, y, shape = lanterns[i]
                lanterns[i] = (x + 5, y, shape)
                if x > WIDTH:
                    lanterns[i] = (0, random.randint(100, 400), random.choice(["fish", "star", "rabbit","sun"]))
                # Kiểm tra va chạm với đạn
                for bullet in bullets:
                    if check_collision(bullet[0], bullet[1], x + 25, y + 50):
                        lanterns_to_remove.append(i)
                        break
                
            # Loại bỏ các lồng đèn cần loại bỏ
            for index in sorted(lanterns_to_remove, reverse=True):
                lanterns.pop(index)
        else:
            if not game_over:  # Chỉ thực hiện một lần sau khi kết thúc trò chơi
                mooncakes = generate_mooncakes()
                game_over = True

            # Di chuyển bánh trung thu rơi xuống
            for mooncake in mooncakes:
                mooncake[1] += mooncake_speed
                if mooncake[1] > HEIGHT:
                    mooncakes.remove(mooncake)

            # Kiểm tra xem đã đủ thời gian để tạo một màn mới bánh trung thu
            if current_time - message_timer >= mooncake_frequency:
                mooncake_wave += 1
                mooncakes.extend(generate_mooncakes())
                message_timer = current_time
                if mooncake_falling > monecake_loop:
                   break
                else:
                   mooncake_falling +=1

        for bullet in bullets:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        draw_trung_thu(lanterns)
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])

        draw_gun(gun_x, gun_y)

        if not lanterns_remaining and game_over:
            # Vẽ bánh trung thu rơi xuống
            for mooncake in mooncakes:
                screen.blit(mooncake_image, (mooncake[0], mooncake[1]))

        if message_visible:
            message_text = message_font.render(message, True, message_color)
            screen.blit(message_text, (message_x, message_y))

        pygame.display.update()

        # Kiểm tra xem còn lồng đèn nào không
        if not lanterns and not mooncakes:
            lanterns_remaining = False

        clock.tick(30)

    pygame.quit()
    sys.exit()
