import turtle

def draw_square():

    d = turtle.Turtle()
    d.shape("circle")
    d.shapesize(0.3,0.3)
    d.speed(25)

    for j in range(72):
        for i in range(4):
            d.forward(100)
            d.right(90)
        d.right(5)

def paint():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    draw_square()
    # draw_circle()
    # draw_triangle()

    window.exitonclick()

paint()
