import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.right(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(60)
t.forward(100)
t.left(90)
t.circle(100, extent=180)
t.left(90)
t.forward(100)

screen.exitonclick()