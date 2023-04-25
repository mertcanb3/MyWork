import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


freeze = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Corrsy Turtle")
screen.tracer(0)

turtle = Player()
cars = CarManager()
level = Scoreboard()


# Move turtle with space 
screen.listen()
screen.onkeypress(fun= turtle.move, key="space")


game_is_on = True
while game_is_on:
    cars.randomcars()
    cars.move()
    time.sleep(freeze)
    
    
    # Level up 
    if turtle.ycor() == 300:
        level.increase_level()
        freeze -= 0.02 #increase speed of cars
        turtle.reset()
    

    # Detect Crash
    for car in cars.Cars:
        if car.distance(turtle) < 20: 
            level.crash()
            freeze = 0.1   
            turtle.reset()
            level.update_level()
        
    screen.update()
