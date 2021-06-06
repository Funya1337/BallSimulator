import turtle
import random

class Ball:
  def __init__(self, turtleClassBall, color, size, speed, pos):
    self.turtleClassBall = turtleClassBall
    self.color = color
    self.size = size
    self.speed = speed
    self.pos = pos

  def createBall(self):
    self.turtleClassBall.shape("circle")
    self.turtleClassBall.color(self.color)
    self.turtleClassBall.shapesize(self.size)
    self.turtleClassBall.penup()
    self.turtleClassBall.speed(self.speed)
    self.turtleClassBall.goto(self.pos, self.pos)
    self.turtleClassBall.dy = 0
    self.turtleClassBall.dx = 2

def checkForCollision(ball):
  if ball.turtleClassBall.xcor() > 300:
    ball.turtleClassBall.dx *= -1

  if ball.turtleClassBall.xcor() < -300:
    ball.turtleClassBall.dx *= -1

def checkForBounce(ball):
  if ball.turtleClassBall.ycor() < -300:
    ball.turtleClassBall.dy *= -1

def ballGravity(ball, wn, gravity):
  while True:
    wn.update()
    
    ball.turtleClassBall.dy -= gravity
    ball.turtleClassBall.sety(ball.turtleClassBall.ycor() + ball.turtleClassBall.dy)

    ball.turtleClassBall.setx(ball.turtleClassBall.xcor() + ball.turtleClassBall.dx)

    checkForCollision(ball)

    checkForBounce(ball)

def main():
  wn = turtle.Screen()
  wn.bgcolor("white")
  wn.title("Bouncing Ball Simulator")
  wn.setup(650, 650)
  gravity = 0.1

  ball = Ball(turtle.Turtle(), "green", 2, 0, 0)
  ball.createBall()

  ballGravity(ball, wn, gravity)
  
  wn.mainloop()

main()
