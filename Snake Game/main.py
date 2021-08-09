from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = []

for _ in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(_*-20, 0)
    snakes.append(snake)

screen.update()
game_status = True

while game_status:
    screen.update()
    for pos in snakes:
        pos.fd(20)

screen.exitonclick()