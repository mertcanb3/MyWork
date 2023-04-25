from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Class for turtle
class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.left(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.goto(STARTING_POSITION)
        
    def move(self):
        self.forward(MOVE_DISTANCE)   
    
    def reset(self):
        self.sety(-280)