#
# Please save this program to the hard-drive of your computer and run
# it by double-clicking on the file's icon. Running the program from
# the IDLE shell might give different behavior in terms of the event-
# processing loop.
#

import turtle

def square(t, length):
  for s in range(4):
    t.forward(length)
    t.left(90)

def writeText():
  t.penup()
  t.setpos(0, 0)
  #Delete the previously received coordinate axis and output it.
  i.clear()
  i.write(point, font= ('Times New Roman',8,'bold'))
 

def closeDown():
  turtle.bye()

def drawShape(x, y):
  #Store the input coordinate axis as a point.
  global point
  point = '(' + str(int(x)) +',' +str(int(y)) +')'
  t.penup()
  t.setpos(x, y)
  t.pendown()
  t.begin_fill()
  if x <= 100: #Left third:
    t.color("green")
    square(t, 10)
  elif 100 < x <= 200: #Middle third:
    t.color("red")
    t.circle(10)
  else:
    t.color("blue")
    square(t, 10)
  t.end_fill()



   
#
# main:
#

# Set window to be 300 x 200 with the point (0, 0) as the lower-left
# corner and (300, 200) as the upper right corner:
turtle.setup(300, 200)
turtle.screensize(300, 200)
turtle.setworldcoordinates(0, 0, 300, 200)

# Initialize global turtle t variable which will be used inside
# of the handler functions:
t = turtle.getturtle()
t.speed(0) # Set fastest screen update speed for this turtle.
#Defines i turtle
i = turtle.Turtle()
i.setpos(0,0)
point = '(0,0)'
# Draw two vertical lines to divide the window into thirds:
t.penup()
t.setpos(100, 0) #First line
t.pendown()
t.setpos(100, 200)
t.penup()
t.setpos(200, 0) #Second line
t.pendown()
t.setpos(200, 200)


# Register callback for key-press events:
turtle.onkey(writeText, 'Up')
turtle.onkey(closeDown, 'q')
# Register callback for mouse on-click events:
turtle.onscreenclick(drawShape)
# Enter event loop:
turtle.listen()
turtle.mainloop()
