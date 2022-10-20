import turtle

def drawSquare(myturtle,x,y,a):
    """It moves according to the user's input and draws a square"""
    myturtle.penup()
    myturtle.setposition(x,y)
    myturtle.pendown()
    myturtle.setposition(x+a,y)
    myturtle.setposition(x+a,y+a)
    myturtle.setposition(x,y+a)
    myturtle.setposition(x,y)


