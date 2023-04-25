from turtle import Turtle, Screen
from time import sleep
import random



with open("HSsnake.txt", "r") as data:
    hs = data.read()


wall_hit = False   
move_by = 20   
Positions = [(0, 0), (-20, 0), (-40, 0)]

apple_locations = []
while len(apple_locations) < 3:
    apple_locations.append(((random.randint(-299,299)),(random.randint(-299,299))))

class Snake:
    
    def __init__(self):
        self.Snakes = []
        self.create_snake()
        self.head = self.Snakes[0]
       
    
    def create_snake(self):
        for pos in Positions:
            self.add_segment(pos)
            
    def add_segment(self, position):
        body = Turtle("square")
        body.penup()
        body.goto(position)
        body.color("green")
        self.Snakes.append(body)
        
    def extend(self):
        self.add_segment(self.Snakes[-1].position())
    

    def Move(self):
        for snake in range(len(self.Snakes) - 1, 0, -1):
            new_x = self.Snakes[snake - 1].xcor()
            new_y = self.Snakes[snake - 1].ycor()
            self.Snakes[snake].goto(new_x, new_y)
        sleep(0.15)
        self.head.forward(move_by)
        
   
    def rotate(self, angle):
        self.head.setheading(angle)
        
    def reset(self):
        for body in self.Snakes:
            body.goto(1000, 1000)
        self.Snakes = self.Snakes[:3]
        self.head.goto(0, 0)


class Apple(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(((random.randint(-285,285)),(random.randint(-285, 285))))
        
        
    def refresh(self):
        self.goto(((random.randint(-285,285)),(random.randint(-285, 285))))
        
    



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = int(hs)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20))
        

        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("HSsnake.txt", "w") as data:
                data.write(str(self.highest_score))
        self.score = 0
        self.goto(0, 0)
        self.write("You Lost =/", align="center", font=("Courier", 40, "bold"))
        self.goto(0,-30)
        self.write(f"Highest Score: {self.highest_score}", align="center", font=("Courier", 20))




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    
 
 
screen.listen() 
screen.onkeypress(lambda: snake.rotate(90), key="Up")
screen.onkeypress(lambda: snake.rotate(270), key="Down")
screen.onkeypress(lambda: snake.rotate(180), key="Left")
screen.onkeypress(lambda: snake.rotate(0), key="Right")

                
                
snake = Snake()
apple = Apple()
score = Scoreboard()


while not wall_hit:
    #Move Snake
    screen.update()
    snake.Move()
    
    for body in snake.Snakes[1:]:
        if snake.head.position() == body.position():
            score.game_over()
            sleep(3)
            snake.reset()
            
        
    # Eat and Grow
    if snake.head.distance(apple) < 15:
        snake.extend()
        score.increase_score()
        apple.refresh()
        
    #Detect wall collusion
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        score.game_over()
        sleep(3)
        snake.reset()
        
        
        
screen.mainloop()
