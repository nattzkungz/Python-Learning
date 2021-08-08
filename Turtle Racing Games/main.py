from turtle import Turtle, Screen
from random import randint
import turtle

state = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, green, blue, pink, purple): ")
colors = ["purple", "blue", "green", "yellow", "red"]
turtle_list = []
turtle_count = 0

for color in colors:
    turtle1 = Turtle(shape="turtle")
    turtle1.penup()
    turtle1.color(color)
    turtle1.goto(-240, -100 + turtle_count*50)
    turtle_count += 1
    turtle_list.append(turtle1)

if user_bet:
    state = True

while state:
    for x in turtle_list:
        if x.xcor() > 230:
            state = False
            winning_color = x.pencolor()
            if winning_color == user_bet:
                print(f"You've won, The {winning_color} turtle is the first")
            else:
                print(f"You've lost, The {winning_color} turtle is the first")
        x.fd(randint(0,10))

print(turtle_list)
screen.exitonclick()