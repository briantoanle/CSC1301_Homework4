# Student: Toan Le
# CRN: 84165
# Course Name: CSC 1301
# Date: November 2nd, 2022
# Description of Program:
#   draw a house with Turtle graphics in python

from turtle import *
title("Toan Le Homework 4")
import math
import turtle as t
setup(1000 ,720)
def main():

    speed(100)
    drawGround()
    drawHouse()
    drawFrontDoor()
    drawRoof()

    exitonclick()

def drawGround():
    penup()
    goto(-500, -70)
    color("#204912")
    pendown()

    begin_fill()
    for i in range(2):
        forward(1000)
        right(90)
        forward(400)
        right(90)
    end_fill()
# draw house
def drawHouse():

    houseWidth = 300
    houseHeight = 200
    penup()
    pensize(3)
    color('black')
    goto(-150,-100)
    pendown()
    #color((225, 198, 153))
    color('black','#F5F5DC')
    begin_fill()
    left(90)
    forward(houseHeight)
    right(90)
    forward(houseWidth)
    right(90)
    forward(houseHeight)
    right(90)
    forward(houseWidth)
    end_fill()

def drawRoof():
    color('#1867c0')
    goto(-150,100)
    pendown()
    begin_fill()
    left(115)
    forward(166)
    right(50)
    forward(166)
    end_fill()

def drawFrontDoor():
    # door
    doorHeight = 60
    doorWidth = 30
    penup()
    goto(10, 0)
    pendown()
    begin_fill()
    color('black', 'grey')
    right(90)
    forward(doorHeight)
    left(90)
    forward(doorWidth)
    left(90)
    forward(doorHeight)
    end_fill()
    penup()

    #door knob
    goto(2,30)
    pendown()
    dot(5,'black')
    penup()

def drawWindow(locationX,locationY):
    goto(locationX,locationY)
    pendown()
main()