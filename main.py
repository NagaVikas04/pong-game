import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#TODO - 1 Create the Screen
#TODO - 2 Create and move the paddle
#TODO - 3 create another paddle
#TODO - 4 create ball and make it move
#TODO - 5 Detect collision with wall and bounce
#TODO - 6 Detect collisioin with paddle
#TODO - 7 Detect when paddle misses
#TODO - 8 Keep Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("The Pong Game")
screen.tracer(0)


# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(x=350, y=0)
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #detecting the collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        #ball to bounce
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()



    #detect when paddle misses and add score
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score >= 1 or scoreboard.r_score >= 1:
        ball.move_speed *= 0.3
    else:
        ball.move_speed *= 0.2


    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        game_is_on = False
        if scoreboard.l_score >= 10:
            turtle.write(f"Winner is left player with score {scoreboard.l_score}", align= "center", font=("Courier", 20, "normal") )
        else:
            turtle.write(f"Winner is right player with score {scoreboard.r_score}", align="center",
                         font=("Courier", 20, "normal"))




screen.exitonclick()