from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
#setting up the screen
screen = Screen() #create a screen object
screen.setup(width=600, height=600) #dimenesions of screen
screen.bgcolor("black") #background color of the game
screen.title("My Snake Game") #title of the game
screen.tracer(0) #turn off the tracer
# for information
snake = Snake()   #create a snake object
food = Food() #create a food object
scoreboard = Scoreboard()

screen.listen() #listen for key press
screen.onkey(snake.up, "Up") #when key is pressed it will call the function
screen.onkey(snake.down, "Down") #when key is pressed it will call the function
screen.onkey(snake.left, "Left") #when key is pressed it will call the function
screen.onkey(snake.right, "Right") #when key is pressed it will call the function

game_is_on = True 
while game_is_on: #keep the game running
    screen.update() #update the screen
    time.sleep(0.1) #slow the game down
    snake.move()

    #Detect touch with food.
    if snake.head.distance(food) < 15: #if the distance between the head and the food is less than 15 then the food will be refreshed
        food.refresh() 
        snake.extend() 
        scoreboard.increase_score() 

    #Detect touch with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: #if the head is outside the screen then the game is over
        game_is_on = False 
        scoreboard.game_over() #call the game over function

    #Detect touch with tail.
    for segment in snake.segments: #if the head collides with the tail then the game is over
        if segment == snake.head: #if the head is the same as the tail then do nothing
            pass 
        elif snake.head.distance(segment) < 10: #if the head is close to the tail then the game is over
            game_is_on = False #set the game to false
            scoreboard.game_over() #call the game over function


screen.exitonclick() #exit the screen when clicked
