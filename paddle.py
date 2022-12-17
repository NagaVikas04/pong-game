from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(stretch_wid=7, stretch_len=0.6)
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 70
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 70
        self.goto(self.xcor(), new_y)


