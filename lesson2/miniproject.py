import turtle

window = turtle.Screen()
d = turtle.Turtle()
d.shape("turtle")
d.speed(0)
ratio = 1.08
num_of_triangles = 36


def circle(size):
    d.penup()
    d.forward(size * 2)
    d.left(42)
    d.pendown()

    for x in range(num_of_triangles):
        for i in range(3):
            d.forward(size)
            d.right(120)
        d.right(360 / num_of_triangles)

    if size < 300:
        circle(size * ratio)


circle(20)
window.exitonclick()
