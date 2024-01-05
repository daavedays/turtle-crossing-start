from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.speed = 0.1

    def move_up(self):
        self.forward(MOVE_DISTANCE)


