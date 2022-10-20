
# Bouncing Balls Simulation Program

import turtle
import random
import time

def atLeftEdge(ball, screen_width):
    if ball.xcor() < -screen_width / 2:
        return True
    else:
        return False

def atRightEdge(ball, screen_width):
    if ball.xcor() > screen_width / 2:
        return True
    else:
        return False

def atTopEdge(ball, screen_height):
    if ball.ycor() > screen_height / 2:
        return True
    else:
        return False

def atBottomEdge(ball, screen_height):
    if ball.ycor() < -screen_height / 2:
        return True
    else:
        return False

def bounceBall(ball, new_direction):
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading =  360 - ball.heading()

    return new_heading

def createBalls(num_balls):
    balls = []
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)
        #new_ball.penup()
        new_ball.setheading(random.randint(1,359))
        balls.append(new_ball)

    return balls

# ---- main
# program greeting
print('This program simulates bouncing balls in a turtle screen')
print('for a specified number of seconds.')

# init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width,screen_height)

# create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')

# prompt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = int(input('Enter number of balls in simulation: '))

# create balls
balls = createBalls(num_balls)

# set start time
start_time = time.time()

# begin simulation
terminate = False
#Set colormode
turtle.colormode(255)

while not terminate:
    for k in range(0,len(balls)):
        balls[k].forward(15)
        
        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k],'right'))
            a=random.randint(0,255)
            b=random.randint(0,255)
            c=random.randint(0,255)
            #Set balls color randomly
            balls[k].fillcolor(a,b,c)
            balls[k].pencolor(a,b,c)
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k],'left'))
            a=random.randint(0,255)
            b=random.randint(0,255)
            c=random.randint(0,255)
            #Set balls color randomly
            balls[k].fillcolor(a,b,c)
            balls[k].pencolor(a,b,c)
        elif atTopEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k],'down'))
            a=random.randint(0,255)
            b=random.randint(0,255)
            c=random.randint(0,255)
            #Set balls color randomly
            balls[k].fillcolor(a,b,c)
            balls[k].pencolor(a,b,c)
        elif atBottomEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k],'up'))
            a=random.randint(0,255)
            b=random.randint(0,255)
            c=random.randint(0,255)
            #Set balls color randomly
            balls[k].fillcolor(a,b,c)
            balls[k].pencolor(a,b,c)

        if time.time() - start_time > num_seconds:
            terminate = True
        
# exit on close window
turtle.exitonclick()
