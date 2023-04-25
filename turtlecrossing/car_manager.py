from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
number_of_cars = 35



# Class Car
class CarManager():
    
    
    def __init__(self):
        self.Cars = []
        
      
    def randomcars(self):
        dice = random.randint(1,6)
        if dice == 3:
            car = Turtle("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.goto(-300, random.randint(-230, 230))
            car.color(random.choice(COLORS))
            self.Cars.append(car)
        
    def move(self):
        for car in self.Cars:
            car.forward(STARTING_MOVE_DISTANCE)
        
    def speedup(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

