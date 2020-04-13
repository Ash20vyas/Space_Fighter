import turtle
import math
import random
import winsound
import pygame

pygame.mixer.init()
pygame.mixer.music.load('sounds/background.wav')
pygame.mixer.music.play(100)
si = turtle.Screen()
si.bgcolor("blue")
si.title("Space Invaders")
si.bgpic("images/back.gif")
si.register_shape("images/gun.gif")
si.register_shape("images/alien.gif")
si.register_shape("images/ship.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-315, -315)
border_pen.pendown()
border_pen.pensize(3)
for i in range(4):
    border_pen.forward(630)
    border_pen.left(90)
border_pen.hideturtle()

ship = turtle.Turtle()
ship.shape("images/ship.gif")
ship.penup()
ship.speed(0)
ship.setposition(0, -270)
ship.setheading(90)
ship.speed = 0

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


def move_left():
    ship.speed = -10


def move_right():
    ship.speed = 10


def move_ship():
    x = ship.xcor()
    x += ship.speed
    if x > 278:
        x = 278
    if x < -278:
        x = -278
    ship.setx(x)


def fire():
    global gunstate
    if gunstate == "passive":
        gunstate = "active"
        winsound.PlaySound("sounds/fire.wav", winsound.SND_ASYNC)
        gun.setposition(ship.xcor(), ship.ycor() + 10)
        gun.showturtle()


def isCollision(t1, t2):
    dist = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if dist < 25:
        return True
    else:
        return False
def end():
    quit()
si.listen()
si.onkeypress(move_left, "Left")
si.onkeypress(move_right, "Right")
si.onkeypress(fire, "space")

alien_number = 5
aliens = []
for i in range(alien_number):
    aliens.append(turtle.Turtle())
for alien in aliens:
    alien.shape("images/alien.gif")
    alien.penup()
    alien.speed(0)
    alien.setposition(random.randint(-250, 250), random.randint(200, 280))

alienspeed = 2

gun = turtle.Turtle()
gun.shape("images/gun.gif")
gun.penup()
gun.speed(0)
gun.hideturtle()
gunspeed = 30
gunstate = "passive"

while True:
    move_ship()
    for alien in aliens:
        x = alien.xcor()
        x += alienspeed
        alien.setx(x)

        if x > 280:
            alienspeed *= -1
            for a in aliens:
                a.sety(a.ycor() - 40)
                if a.ycor() < ship.ycor():
                    print("!!!GAME OVER!!!")
                    print("Score:" + format(score))
                    end()
        if x < -280:
            alienspeed *= -1
            for a in aliens:
                a.sety(a.ycor() - 40)
                if a.ycor() < ship.ycor():
                    print("!!!GAME OVER!!!")
                    print("Score:" + format(score))
                    end()
        if isCollision(gun, alien):
            winsound.PlaySound("sounds/explosion.wav", winsound.SND_ASYNC)
            gun.hideturtle()
            gunstate = "passive"
            gun.setposition(0, -400)
            alien.setposition(random.randint(-250, 250), random.randint(200, 280))
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()
            alienspeed += 0.25 if alienspeed > 0 else -0.25

        if isCollision(ship, alien):
            ship.hideturtle()
            print("!!!GAME OVER!!!")
            print("Score:" + format(score))
            end()

    if gunstate == "active":
        gun.sety(gun.ycor() + gunspeed)

    if gun.ycor() > 280:
        gun.hideturtle()
        gunstate = "passive"
