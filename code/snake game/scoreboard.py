from turtle import Turtle
ALIGNMENT = "center" #left or right
FONT = ("Courier", 24, "normal") #for font, size, and style


class Scoreboard(Turtle): #inherit from turtle class

    def __init__(self): #starting the scoreboard
        super().__init__() #inherit from turtle class
        self.score = 0  #set score to 0
        self.color("white") #set color of text
        self.penup() #no drawing when moving
        self.goto(0, 270) #set position of text
        self.hideturtle() #hide the turtle
        self.update_scoreboard() #updating

    def update_scoreboard(self): #updating the scoreboard
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self): #game over text
        self.goto(0, 0) #position of text
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  #postions

    def increase_score(self): 
        self.score += 1 #increase score by 1
        self.clear() #clear the scoreboard
        self.update_scoreboard() #updating the scoreboard
