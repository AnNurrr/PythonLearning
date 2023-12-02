# Ainur
# # 11/30/2023
import turtle

def draw_circle(radius, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_cloud():
    turtle.circle(50, "white", 0, 30)
    draw_circle(40, "white", -40, 30)
    draw_circle(35, "white", 40, 30)

    turtle.hideturtle()

    turtle.done()



