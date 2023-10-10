import turtle
import random
import time

# Set up the screen
window = turtle.Screen()
window.title("Turtle Race")
window.bgcolor("white")

# Create two turtles for racing
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.penup()
turtle1.goto(-200, 20)

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("blue")
turtle2.penup()
turtle2.goto(-200, -20)

# Create the finish line
finish_line = turtle.Turtle()
finish_line.color("black")
finish_line.penup()
finish_line.goto(200, 100)
finish_line.pendown()
finish_line.goto(200, -100)

# Function to move the turtles
def move_turtle(turtle):
    distance = random.randint(2, 5)
    turtle.forward(distance)

# Main game loop
while True: #Vòng lặp
    while True:
        move_turtle(turtle1)
        move_turtle(turtle2)

        # Check if a turtle has crossed the finish line: or hoặc, and: và
        if turtle1.xcor() >= 200 or turtle2.xcor() >= 200:
            if turtle1.xcor() > turtle2.xcor():
                winner = "Red Turtle"
            else:
                winner = "Blue Turtle"
            
            turtle1.goto(-200, 20)
            turtle2.goto(-200, -20)
            
            # Display the winner
            winner_turtle = turtle.Turtle()
            winner_turtle.color("green")
            winner_turtle.penup()
            winner_turtle.hideturtle()
            winner_turtle.goto(0, 0)
            winner_turtle.write(f"The winner is {winner}!", align="center", font=("Arial", 16, "bold"))
            break
    # Delay for a few seconds
    time.sleep(2)
    # Clear the winner message
    winner_turtle.clear()

# Close the window when clicked
window.exitonclick()
