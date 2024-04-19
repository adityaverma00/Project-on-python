import turtle
turtle.bgcolor('black') #Backgorund color
t=turtle.Turtle()
colors=['red','dark red'] #Defining colors list for alternating segments
for number in range(400): #Main loop
    t.forward(number+1)
    t.right(90) #Directiong
    t.pencolor(colors[number%2]) #Lightness

turtle.done()

