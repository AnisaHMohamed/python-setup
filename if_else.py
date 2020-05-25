import turtle

anisa_turtle = turtle.Turtle()


def square():
    anisa_turtle.forward(100)
    anisa_turtle.right(90)
    anisa_turtle.forward(100)
    anisa_turtle.right(90)
    anisa_turtle.forward(100)
    anisa_turtle.right(90)
    anisa_turtle.forward(100)


square()
anisa_turtle.forward(100)
square()

elephant_weight = 3000
ant_weight = 100000
if elephant_weight > ant_weight:
    square()
else:
    anisa_turtle.forward(100)
