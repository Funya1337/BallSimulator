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
  wn.bgcolor("black")
  wn.title("Bouncing Ball Simulator")
  wn.setup(650, 650)
  gravity = 0.1

  balls = []

  #for _ in range(10):
  #  balls.append(Ball(turtle.Turtle(), "green", 2, 0, random.randint(-290, 290)))

  #for i in range(len(balls)):
  #  balls[i].createBall()

  ball = Ball(turtle.Turtle(), "green", 2, 0, random.randint(-290, 290))
  ball.createBall()

  #for i in range(len(balls)):
  #  ballGravity(balls[i], wn, gravity)

  ballGravity(ball, wn, gravity)
  
  wn.mainloop()

main()
