from turtle import Turtle, Screen
import time

#Paddle boards 
class Paddle(Turtle):     
   
    #Set the shape 
    def __init__(self, x_loc):
       super().__init__()
       self.shape("square")
       self.shapesize(stretch_len=5)
       self.goto(x_loc, 0)
       self.left(90)
       self.color("white")
       self.penup()
       
       
    #Move up
    def up(self):
        new_y = self.ycor() + 30
        self.sety(new_y)
        if self.ycor() > 300:
            self.sety(-300)
        
    #Move down
    def down(self):
        new_y = self.ycor() - 30
        self.sety(new_y)
        if self.ycor() < -300:
            self.sety(300)
            

#Class Ball
class Ball(Turtle):
    
    #Set the ball
    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_speed = 3
        self.y_speed = 3
        
        
    #Ball move around
    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
    
      
    #Bounce from walls     
    def bounce(self):
        self.y_speed *= -1
    
    #Bounce from the paddles
    def defend(self):
        self.x_speed *= -1
        
    #Reset ball to center   
    def reset(self):
        self.goto(0, 0)
         
#Class scoreboard     
class Scoreboard(Turtle):
    
    #set the score label
    def __init__(self, x_loc):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x_loc, 250)
        self.hideturtle()
        self.update_score()
    
    
    # Update value in screen
    def update_score(self):
        self.write(f"{self.score}", align="center", font=("Courier", 40))
        

    # Increase score
    def increase_score(self):   
        self.score += 1
        self.clear()
        self.update_score()

    #Game Over
    def end(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 40, "bold"))
        

   
        
#Screen       
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=900, height=600)


#Instances 
paddle1 = Paddle(-370)
paddle2 = Paddle(370)
ball = Ball()
scoreA = Scoreboard(30)
scoreB = Scoreboard(-30)


#Arrow keys of keyboard assigned to functions
screen.listen()
screen.onkeypress(fun= paddle1.up, key="Up")
screen.onkeypress(fun= paddle1.down, key="Down")
screen.onkeypress(fun= paddle2.up, key="Right")
screen.onkeypress(fun= paddle2.down, key="Left")



#Run game untill someone reaches 10
game = True
while game:
    ball.move()
    screen.update()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
        
    if ball.distance(paddle1) < 30 or ball.distance(paddle2) < 30 :
        ball.defend()       
        
    if ball.xcor() > 390:    
        scoreB.increase_score()
        ball.reset()
        ball.defend()
        time.sleep(1)
        
        
    if ball.xcor() < -390: 
        scoreA.increase_score()
        ball.reset()
        ball.defend()
        time.sleep(1) 
        
        
    if scoreA.score == 10 or scoreB.score == 10:
        scoreA.end()
        game = False
    
    

screen.mainloop()
