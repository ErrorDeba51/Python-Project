import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.speed(0)


n = 90
h = 20

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.left(100)
    t.fd(20)
    for j in range(2):
        t.left(2)
    t.circle(150)

t.hideturtle()
