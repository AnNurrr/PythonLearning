import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Function to draw the mushroom cap
def draw_mushroom_cap():
    t.color("red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# Function to draw the mushroom stem
def draw_mushroom_stem():
    t.color("brown")
    t.begin_fill()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.end_fill()

# Position the turtle to start drawing the cap
t.penup()
t.goto(0, -50)
t.pendown()

# Draw the mushroom cap
draw_mushroom_cap()

# Position the turtle to start drawing the stem
t.penup()
t.goto(0, -50)
t.pendown()

# Draw the mushroom stem
draw_mushroom_stem()

# Hide the turtle
t.hideturtle()

# Close the turtle graphics window when clicked
screen.exitonclick()
