"""
CIS 210 proj1 - turtle
Author: Oliver Boorstein
Credits: N/A
Drawing a duck using Turtle graphics
"""

import turtle

t = turtle.Turtle()

t.pu()
# Plan to fill duck with yellow
t.fillcolor('yellow')
t.begin_fill()
# Setup starting position of duck
t.goto(-50,50)
t.pd()
t.rt(90)
# Draw underbelly
t.circle(50, 180, 6)
# Draw neck, and beak.
t.rt(20)
t.fd(30)
t.rt(70)
t.fd(20)
t.lt(160)
t.fd(20)
# Draw circle of head
t.rt(70)
t.circle(20, 180, 6)
# Draw back of neck
t.fd(30)
t.lt(120)
# Draw duck's back
t.circle(120, -25)
t.lt(120)
# Draw tail
t.fd(40)
t.lt(150)
t.fd(30)
# Complete fill
t.end_fill()
# Eye whites color set
t.fillcolor('white')
t.begin_fill()
t.pu()
# Set up to draw eyes
t.goto(35,85)
t.pd()
# Draw outer eye circle
t.circle(10)
t.end_fill()
# Eye pupils color set 
t.fillcolor('black')
t.begin_fill()
# Set up to draw pupil circle
t.pu()
t.lt(90)
t.fd(12)
t.pd()
# Draw pupil
t.circle(4)
# Fill
t.end_fill()
t.pu()
# Get turtle out of way for clear picture
t.goto(100000,10000)
# Prevents tab from auto closing
turtle.mainloop()