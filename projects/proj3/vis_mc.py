'''
CIS 210 proj 3 - vis mc
Author: Oliver Boorstein
Credits: N/A
Visualize the Monte Carlo simulation using Turtle graphics
'''

import math
import turtle
import random


def draw_plane(radius, p):
    for _ in range(4):
        p.pu()
        p.goto(0, 0)
        p.pd()
        p.fd(radius)
        p.rt(90)


    # # draw circle
    # p.pu()
    # p.goto(0, -radius)
    # p.pd()
    # p.circle(radius)           

    # # draw square
    # p.pu()
    # p.goto(radius, radius)
    # p.pd()
    # for _ in range(4):
    #     p.rt(90)
    #     p.fd(2 * radius)


def draw_dart(num_darts, radius, p):
    in_circle = 0

    for _ in range(num_darts):    
        x = random.random()
        y = random.random()

        if random.random() < 0.5: # to generate negative x-coordinates half the time
            x = -x

        if random.random() < 0.5: # same for y
            y = -y

        distance = math.sqrt(x**2 + y**2)
        
        if distance <= 1:
            in_circle += 1
            p.color('blue')
        else:
            p.color('red')

        p.pu()
        p.goto(x*radius, y*radius) # multiply each coordinate by radius to keep scale
        p.pd()
        p.dot()
        p.pu

    return in_circle


def mc_vis(num_darts: int):
    '''
    (int) -> None

    Perform the necessary operations to visualize
    the Monte Carlo simulation in 2 dimensional space
    '''

    RADIUS = 200 # radius constant

    p = turtle.Turtle()
    p.speed(0)
    draw_plane(RADIUS, p)
    draw_dart(num_darts, RADIUS, p)

    turtle.done()


if __name__ == "__main__":
    mc_vis(1000)

