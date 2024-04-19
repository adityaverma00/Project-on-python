import turtle
import random

class TurtleRacer:
    def __init__(self, color, position): #Constructor to initialize racer attributes
        self.color = color 
        self.turtle = turtle.Turtle(shape="turtle") 
        self.turtle.color(color) #Turtle color
        self.turtle.penup() 
        self.turtle.goto(position) #Setting up starting posting

    def race(self): #Moving the turtle to a random distance
        distance = random.randint(1, 50)
        self.turtle.forward(distance)

#Set up the race
racers = [
    TurtleRacer("red", (-100, 20)),
    TurtleRacer("blue", (-100, -20)), #
    TurtleRacer("green", (-100, -60))
]

#Start the race
for _ in range(10): #Main loop to run the race
    for racer in racers: 
        racer.race()

turtle.done()





