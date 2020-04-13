import turtle
import os
import math
import random

si = turtle.Screen()
si.bgcolor("black")
si.title("Space Invaders")
# si.bgpic("Space_invader_Background.gif")

# si.register_shape("alien.gif")
# si.register_shape("ship.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for i in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()


ship = turtle.Turtle()
ship.color("green")
ship.shape("triangle")
ship.penup()
ship.speed(0)
ship.setposition(0, -250)
ship.setheading(90)
ship.speed = 0

score=0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring= "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
def move_left():
    ship.speed = -10
def move_right():
    ship.speed = 10
def move_ship():
    x = ship.xcor()
    x += ship.speed
    if x > 280:
        x = 280
    if x < -280:
        x = -280
    ship.setx(x)
def fire():
    global gunstate
    if gunstate == "passive":
        gunstate="active"
        gun.setposition(ship.xcor(), ship.ycor()+10)
        gun.showturtle()
def isCollision(t1,t2):
    dist = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if dist < 15:
        return True
    else:
        return False

si.listen()
si.onkeypress(move_left, "Left")
si.onkeypress(move_right, "Right")
si.onkeypress(fire, "space")

alien_number = 5
aliens = []
for i in range(alien_number):
    aliens.append(turtle.Turtle())
for alien in aliens:
    alien.color("red")
    alien.shape("circle")
    alien.penup()
    alien.speed(0)
    alien.setposition(random.randint(-250, 250), random.randint(200, 280))

alienspeed=2

gun = turtle.Turtle()
gun.color("yellow")
gun.shape("triangle")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5, 0.5)
gun.hideturtle()
gunspeed=30
gunstate="passive"

while True:
    move_ship()
    for alien in aliens:
        x = alien.xcor()
        x +=alienspeed
        alien.setx(x)

        if x > 280:
            alienspeed *= -1
            for a in aliens:
                a.sety(a.ycor()-40)
                if a.ycor() < ship.ycor():
                    print("!!!GAME OVER!!!")
                    print("Score:"+format(score))
                    quit()
        if x < -280:
            alienspeed *= -1
            for a in aliens:
                a.sety(a.ycor() - 40)
                if a.ycor() < ship.ycor():
                    print("!!!GAME OVER!!!")
                    print("Score:"+format(score))
                    quit()
        if isCollision(gun, alien):
            gun.hideturtle()
            gunstate = "passive"
            gun.setposition(0, -400)
            alien.setposition(random.randint(-250, 250), random.randint(200, 280))
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()
            alienspeed += 0.25 if alienspeed>0 else -0.25


        if isCollision(ship, alien):
            ship.hideturtle()
            print("!!!GAME OVER!!!")
            print("Score:"+format(score))
            quit()


    if gunstate == "active":
        gun.sety(gun.ycor()+gunspeed)

    if gun.ycor() > 280:
        gun.hideturtle()
        gunstate="passive"
