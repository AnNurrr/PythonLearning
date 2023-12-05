# Ainur
# 12/04/2023

import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        # Draw the trunk (brown)
        t.pensize(10)
        t.pencolor("brown")
        t.forward(branch_length)

        # Draw the first branch (green)
        t.pensize(5)
        t.pencolor("green")
        t.left(45)
        draw_branch(branch_length - 15, t)

        # Return to the original position
        t.right(90)
        draw_branch(branch_length - 15, t)

        # Return to the original position
        t.left(45)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")  # Set background color

    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.speed(2)

    # Lift the pen and move to the starting position
    my_turtle.penup()
    my_turtle.goto(0, -200)
    my_turtle.pendown()

    draw_branch(100, my_turtle)

    screen.exitonclick()

if __name__ == "__main__":
    main()
