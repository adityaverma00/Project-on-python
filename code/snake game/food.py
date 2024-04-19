from turtle import Turtle
import random 


class Food(Turtle): #Inherits from Turtle class

    def __init__(self): 
        super().__init__() #calls the Turtle class constructor
        self.shape("circle") #sets the shape of the turtle
        self.penup() #it wont draw a line
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # makes the food a bit smaller
        self.color("red") #sets the color
        self.speed("fastest") #sets the speed of the turtle
        self.refresh() #calls the refresh method

    def refresh(self): #refreshes the food
        random_x = random.randint(-280, 280) #generates a random x coordinate
        random_y = random.randint(-280, 280) #generates a random y coordinate
        self.goto(random_x, random_y) #moves the turtle to the random coordinates 
