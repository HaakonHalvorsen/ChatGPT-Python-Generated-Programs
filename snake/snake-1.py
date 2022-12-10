# Import the turtle module
import turtle

# Set the screen size
turtle.setup(500, 500)

# Create a turtle object for the snake
snake = turtle.Turtle()

# Set the speed of the turtle
snake.speed(0)

# Set the starting position of the snake
snake.penup()
snake.goto(0, 0)

# Set the direction of the snake
direction = "stop"

# Define a function to change the direction of the snake
def move():
  if direction == "up":
    snake.setheading(90)
  elif direction == "down":
    snake.setheading(270)
  elif direction == "left":
    snake.setheading(180)
  elif direction == "right":
    snake.setheading(0)
  elif direction == "stop":
    snake.setheading(snake.heading())

# Define functions to change the direction of the snake based on keyboard input
def go_up():
  global direction
  direction = "up"

def go_down():
  global direction
  direction = "down"

def go_left():
  global direction
  direction = "left"

def go_right():
  global direction
  direction = "right"

# Bind the direction changing functions to the corresponding keyboard keys
turtle.onkeypress(go_up, "Up")
turtle.onkeypress(go_down, "Down")
turtle.onkeypress(go_left, "Left")
turtle.onkeypress(go_right, "Right")

# Set the screen to listen to keyboard input
turtle.listen()

# Main game loop
while True:
  move()
  snake.forward(10)
