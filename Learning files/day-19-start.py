from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()

def forward():
    t.fd(10)

s.onkey(forward, "space")
s.exitonclick()