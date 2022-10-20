import turtle
#Make 800x600 window screen
turtle.setup(800,600)
window = turtle.Screen()
#Set title
window.title('Marking x Window')
x_turtle = turtle.getturtle()
#Draw x to the given condition
x_turtle.penup()
x_turtle.setposition(-400,300)
x_turtle.pendown()
x_turtle.setposition(400,-300)
x_turtle.penup()
x_turtle.setposition(400,300)
x_turtle.pendown()
x_turtle.setposition(-400,-300)
