# Student: Toan Le
# CRN: 84165
# Course Name: CSC 1301
# Date: November 2nd, 2022
# Description of Program:
#   draw a house with Turtle graphics in python
import random
# disclaimer: the house does look like a face

from turtle import *
title("Toan Le Homework 4")
setup(1000 ,720)
def main():

    speed(100)
    drawSky()
    drawMountains(-500, -90, '#454745', 300)
    drawMountains(-400,-90,'#6a6d6a',450)

    drawGround()
    drawHouse()
    drawWindow(115,20,45)
    drawWindow(-70, 20, 45)
    drawFrontDoor()
    drawRoof()

    drawClouds(100,220,50)
    drawClouds(-100,180,30)
    drawClouds(-350,240, 15)
    drawClouds(-400, 120, 55)
    drawClouds(400, 100, 20)



    drawGrass(300,-180,12)
    drawGrass(-200,-200,10)
    drawGrass(200, -100, 20)
    drawGrass(150, -330, 25)
    drawGrass(-400, -130, 25)
    drawGrass(-400, -300, 35)

    drawFlower(-200,-300,'blue',10)
    drawFlower(-320,-280,'pink',13)
    drawFlower(200, -170, 'light pink', 12)
    drawFlower(300, -270, 'yellow', 14)
    drawSun()
    exitonclick()

def drawSun():
    penup()
    goto(530,350)
    pendown()
    color('#fefdb1')
    begin_fill()
    circle(100)
    end_fill()

def drawGrass(x,y,height):
    penup()
    goto(x,y)
    #pensize(10)
    color('dark green','dark green')
    pendown()
    begin_fill()
    setheading(0)
    for i in range(10):
        setheading(60)
        forward(height)
        setheading(300)
        forward(height)
    setheading(180)
    forward(10*height)
    end_fill()

def drawFlower(x,y,flowerColor,size):

    penup()
    goto(x,y)
    pendown()
    color('black')
    setheading(90)
    forward(size*4)
    for i in range(6):

        color(flowerColor)
        begin_fill()
        forward(size/4.5)
        circle(size)
        right(60)
        end_fill()


def drawMountains(x,y,colorS,size):
    penup()
    goto(x,y)
    pendown()
    color(colorS)
    begin_fill()
    setheading(65)
    forward(size)
    setheading(295)
    forward(size)
    end_fill()
    setheading(0)
def drawClouds(x,y,size):
    penup()
    goto(x,y)
    color('white')
    begin_fill()
    circle(size/1.5)
    setheading(0)
    forward(size)
    circle(size)
    forward(size * 1.2)
    circle(size / 1.2)
    forward(size * 1.2)
    circle(size / 1.2)

    end_fill()
    penup()
def drawSky():
    penup()
    goto(-500,350)
    color("#63defe")
    pendown()

    begin_fill()
    for i in range(2):
        forward(1000)
        right(90)
        forward(420)
        right(90)
    end_fill()
def drawWindow(x,y,size):
    penup()
    goto(x,y)
    #color('black')
    pendown()
    for i in range(2):
        forward(size)
        right(90)
        forward(size)
        right(90)
    penup()
    goto(x-12,y+7)
    pendown()
    for i in range(2):
        forward(size-25)
        right(90)
        forward(size-25)
        right(90)

def drawGround():
    penup()
    goto(-500, -50)
    color("#49bf57")
    pendown()

    begin_fill()
    for i in range(2):
        forward(1000)
        right(90)
        forward(300)
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
    penup()

def drawRoof():
    color('black','#1867c0')
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
    doorWidth = 40
    penup()
    goto(0, -100)
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
    goto(-10,-70)
    pendown()
    dot(5,'black')
    penup()

main()
