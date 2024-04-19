from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # starting positions of the snake
MOVE_DISTANCE = 20 # distance the snake moves
UP = 90 #degrees
DOWN = 270 #degrees
LEFT = 180 #degrees
RIGHT = 0 #degrees


class Snake:

    def __init__(self): #initializing the snake
        self.segments = [] #list of the segments of the snake
        self.create_snake()  
        self.head = self.segments[0] #head of the snake 

    def create_snake(self): 
        for position in STARTING_POSITIONS: 
            self.add_segment(position) #adding the segments to the list

    def add_segment(self, position):
        new_segment = Turtle("square") #shape of the snake
        new_segment.color("white") #color of the snake
        new_segment.penup() #snake does not draw 
        new_segment.goto(position) #position of the snake 
        self.segments.append(new_segment) #append the segment to the list 

    def extend(self): 
        self.add_segment(self.segments[-1].position()) #adding the segment to the list 

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): 
            new_x = self.segments[seg_num - 1].xcor() #new x position of the snake 
            new_y = self.segments[seg_num - 1].ycor() #new y position of the snake
            self.segments[seg_num].goto(new_x, new_y) #moving the snake to the new position (new x and new y)
        self.head.forward(MOVE_DISTANCE) #moving the snake forward (forward is 0 degrees)

    def up(self):
        if self.head.heading() != DOWN: #if the snake is not moving down
            self.head.setheading(UP) #moving the snake up (up is 90 degrees)

    def down(self):
        if self.head.heading() != UP: #if the snake is not moving up
            self.head.setheading(DOWN) #moving the snake down (down is 270 degrees)

    def left(self):
        if self.head.heading() != RIGHT: #if the snake is not moving right
            self.head.setheading(LEFT) #moving the snake left (left is 180 degrees)

    def right(self):
        if self.head.heading() != LEFT: #if the snake is not moving left
            self.head.setheading(RIGHT) #moving the snake right (right is 0 degrees)
