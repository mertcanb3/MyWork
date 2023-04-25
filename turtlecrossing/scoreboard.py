from turtle import Turtle
from time import sleep


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-235, 260)
        self.update_level()
        
    def increase_level(self):
        self.level += 1
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.color("black")
        self.goto(-235, 260)
        self.write(f"Level: {self.level}", align="center",font=FONT)
        
    def crash(self):
        self.goto(0,0)
        self.color("red")
        self.write("CRASH!", align="center",font=("Courier", 30, "bold"))
        self.level = 1
        sleep(2)
        self.clear()
        
        