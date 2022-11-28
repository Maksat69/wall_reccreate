from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

is_on = True
screen = Screen()
screen.title("Wall game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

score_le = Score((-100, 200))
score_ry = Score((100, 200))

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.go_up()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.miss_shot()
        score_le.increase_score()

    if ball.xcor() < -380:
        ball.miss_shot()
        score_ry.increase_score()
screen.exitonclick()
