## Python3 Snake game built using turtle module

# turtle module that is built in to allow for games
import turtle
# specifically for mac to interact with the sounds
import os

## this is what creates the window for the game
window = turtle.Screen()
window.title("Python Snake")
window.bgcolor("black")
window.setup(width=700, height=500)
window.tracer(0)

# keep and modify the score
score = 0

# creating the snake 
snake = turtle.Turtle()
# speed of animation
snake.speed(0)
# creates the shape of the snake
snake.shape("square")
snake.color("white")
snake.penup()
snake.dx = 0
snake.dy = 3

# creating the score card (pen)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white");
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Score: 0", align="center", font=("Courier", 20, "normal"))

# creating the "food" for the snake

# functions to allow the pieces to move
def snake_up():
     # need to first get the y-coordinate from the turtle module
    y = snake.ycor()
    y += 1;
    # this is what changes the direction of the snake
    snake.dy = 3;
    snake.sety(y + 20)

def snake_down():
    # need to first get the y-coordinate from the turtle module
    y = snake.ycor()
    y -= 1;
    # this is what changes the direction of the snake
    snake.dy = -3;
    # updates y to be the new coordinate set
    snake.sety(y - 20)

def snake_left():
    # need to first get the y-coordinate from the turtle module
    x = snake.xcor()
    x -= 1;
    # this is what changes the direction of the snake
    snake.dx = -3;
    # updates y to be the new coordinate set
    snake.setx(x - 20)

def snake_right():
    # need to first get the y-coordinate from the turtle module
    x = snake.xcor()
    x += 1;
    # this is what changes the direction of the snake
    snake.dx = 3;
    # updates y to be the new coordinate set
    snake.setx(x + 20)

# listens for the keyboard input
window.listen()
# listens specifically for lowercase "w" input
window.onkeypress(snake_up, "w")
# listens specifically for lowercase "s" input
window.onkeypress(snake_down, "s")
# listens specifically for lowercase "s" input
window.onkeypress(snake_left, "a")
# listens specifically for lowercase "s" input
window.onkeypress(snake_right, "d")

## main game loop
# this is what runs the game continuously
while True:
    window.update()

    # this is what allows the snake to move around
    # this controls and moves the x-coordinate to update and move
    # snake.setx(snake.xcor() + snake.dx)
    # this controls and moves the y-coordinate to update and move
    # snake.sety(snake.ycor() + snake.dy)

    snake_down()
    snake_left()
    snake_right()
    snake_up()

