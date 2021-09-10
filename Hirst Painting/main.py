import random
import turtle
import colorgram

rgb_colors = []
colors = colorgram.extract("Hirst Painting/hirst.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)

a = turtle.Turtle()
turtle.colormode(255)
a.penup()
a.speed("fastest")
a.hideturtle()

for _ in range(10):
    a.goto(-225, -200 + (50*_))
    for x in range(10):
        a.dot(20, random.choice(rgb_colors))
        a.fd(50)






screen = turtle.Screen()
screen.exitonclick()