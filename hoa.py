import turtle

# Tạo một đối tượng Turtle
hua_hue = turtle.Turtle()

# Đặt màu sắc
hua_hue.color("red", "yellow")  # Màu sắc của bông hoa và màu nền

# Bắt đầu fill màu nền
hua_hue.begin_fill()

# Vẽ bông hoa huệ
hua_hue.forward(100)
hua_hue.left(45)
hua_hue.forward(100)
hua_hue.left(135)
hua_hue.forward(100)
hua_hue.left(45)
hua_hue.forward(100)
hua_hue.left(135)

# Kết thúc fill màu nền
hua_hue.end_fill()

# Vẽ cuống hoa
hua_hue.penup()
hua_hue.goto(75, -20)
hua_hue.pendown()
hua_hue.color("green")
hua_hue.setheading(90)
hua_hue.forward(150)

# Đóng cửa sổ khi người dùng nhấn chuột vào nó
turtle.exitonclick()
