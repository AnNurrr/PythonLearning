import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.fillcolor("orange")
t.begin_fill()
t.right(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(60)
t.end_fill()
t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.left(90)
t.circle(100, extent=180)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.goto(0, 50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(50, 50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.goto(-50, 50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(50, 30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.goto(-6, 20)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(0, 70)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()



screen.exitonclick()