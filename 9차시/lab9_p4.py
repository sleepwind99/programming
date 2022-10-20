def drawFlower(myturtle,r):
    """R makes a circle with the radius of the circle
and turns the circle by 15 degrees around 360 degrees."""
    myturtle = turtle.getturtle()
    myturtle.speed(0)
    myturtle.color("red")
    myturtle.circle(r)
    myturtle.fillcolor('white')
    
    for e in range(0,361,15):

        myturtle.circle(r)
        myturtle.setheading(e)
        myturtle.stamp()

        
        


       
