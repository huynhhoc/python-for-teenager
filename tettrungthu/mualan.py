import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Múa Lân")

# Tải hình ảnh lân
lan_image = pygame.image.load("rong.jpg")
lan_image = pygame.transform.scale(lan_image, (100, 200))

# Tạo danh sách các góc xoay
rotation_angles = [0, 45, 90]

# Tọa độ và tốc độ ban đầu của lân
lan_x = random.randint(0, WIDTH - lan_image.get_width())  # Vị trí x ngẫu nhiên ban đầu
lan_y = 0  # Bắt đầu từ trên cùng
lan_speed_x = random.choice([-5, 5])  # Tốc độ di chuyển ngẫu nhiên theo chiều ngang
lan_speed_y = 2  # Tốc độ di chuyển theo chiều dọc

# Biến đếm để xoay lân
step_count = 4
rotation_count = 3  # Số lần xoay lân
max_steps_before_rotation = 3  # Số bước trước khi xoay lân
rotation_wait_time = 5  # Thời gian chờ trước khi xoay lại (tính bằng số frames)
rotation_wait_count = 3  # Biến đếm thời gian chờ

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill((255, 255, 255))
    pygame.time.wait(100)
    # Di chuyển lân
    lan_x += lan_speed_x
    lan_y += lan_speed_y
    step_count += 1

    # Nếu đã di chuyển đủ số bước trước khi xoay
    if step_count >= max_steps_before_rotation:
        step_count = 0  # Đặt lại biến đếm bước

        # Nếu đang chờ thời gian trước khi xoay lại
        if rotation_wait_count < rotation_wait_time:
            rotation_wait_count += 1
        else:
            rotation_wait_count = 0  # Đặt lại biến đếm thời gian chờ

            # Xoay lân sang góc mới
            rotation_angle = random.choice(rotation_angles)
            lan_image = pygame.transform.rotate(pygame.transform.scale(lan_image, (100, 200)), rotation_angle)

            rotation_count += 1

    # Vẽ lân
    screen.blit(lan_image, (lan_x, lan_y))

    # Kiểm tra nếu lân ra khỏi biên màn hình, thay đổi hướng di chuyển
    if lan_x < 0 or lan_x + lan_image.get_width() > WIDTH:
        lan_speed_x = -lan_speed_x  # Đảo hướng di chuyển ngang ngược lại

    # Nếu lân ra khỏi màn hình ở phía dưới, đặt lại vị trí của nó và hướng di chuyển
    if lan_y > HEIGHT:
        lan_x = random.randint(0, WIDTH - lan_image.get_width())
        lan_y = 0
        lan_speed_x = random.choice([-5, 5])
        lan_speed_y = 5
        rotation_count = 0  # Đặt lại số lần xoay

    # Cập nhật màn hình
    pygame.display.update()

    # Giới hạn tốc độ vòng lặp
    clock.tick(30)

# Kết thúc Pygame
pygame.quit()
sys.exit()
