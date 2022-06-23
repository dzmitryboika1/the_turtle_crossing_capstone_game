from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        """move turtle up"""
        self.forward(MOVE_DISTANCE)

    def down(self):
        """move turtle down"""
        self.backward(MOVE_DISTANCE)
