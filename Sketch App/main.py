from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()
t.setheading(90)

def forward():
    t.fd(10)

def backward():
    t.bk(10)

def turnleft():
    t.lt(10)

def turnright():
    t.rt(10)

def clear():
    s.reset()

s.onkey(key="w", fun=forward)
s.onkey(key="s", fun=backward)
s.onkey(key="a", fun=turnleft)
s.onkey(key="d", fun=turnright)
s.onkey(key="c", fun=clear )

s.exitonclick()
