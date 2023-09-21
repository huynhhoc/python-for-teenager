#Ngon ngu lap trinh su dung Python
from turtle import *

# Set up the screen
screen = Screen()
screen.title("Amazing Turtle Adventure")
screen.bgcolor("lightblue")

# Create the turtle
player = Turtle()
player.shape("turtle")
player.color("blue")
player.speed(1)  # Set the turtle's speed

# Create a target
target = Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.goto(100, 200)

# Function to move the turtle forward
def move_forward():
    player.forward(10)
    check_target()

# Function to move the turtle backward
def move_backward():
    player.backward(10)
    check_target()

# Function to turn the turtle left
def turn_left():
    player.left(10)

# Function to turn the turtle right
def turn_right():
    player.right(10)

# Function to check if the turtle reached the target
def check_target():
    if player.distance(target) < 20:
        print("Congratulations! You reached the target!")
        player.goto(0, 0)  # Return the turtle to the starting position
        player.setheading(0)  # Reset the turtle's heading

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Main game loop
mainloop()
