import tkinter as tkr
from tkinter import *
import sys
import os
import time

WIDTH = 800
HEIGHT = 600
r = 200
showPathChecker = False

class Ball:
  def __init__(self, canvas, radius, color):
    self.canvas = canvas
    self.radius = radius
    self.color = color

  def create_ball(self):
    return canvas.create_oval(self.radius, self.radius, 150, 150, fill = self.color, tag = "ball")

def pushEvent():
  dx = w2.get()
  dy = 0
  ballGravity(dx, dy)

def restartFunc():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def showCoords(pos):
  label_x0.config(text = "Ball Coord x0: " + str(int(pos[0])))
  label_y0.config(text = "Ball Coord y0: " + str(int(pos[1])))
  label_x1.config(text = "Ball Coord x1: " + str(int(pos[2])))
  label_y1.config(text = "Ball Coord y1: " + str(int(pos[3])))

def drawPath(pos):
  x, y = pos[0], pos[1]
  if canvas.old_coords:
    x1, y1 = canvas.old_coords
    canvas.create_line(x, y, x1, y1)
  canvas.old_coords = x, y

def showPathCheckerFunc():
  global showPathChecker
  print(showPathChecker)
  if showPathBtn['text'] == 'True':
    showPathBtn['text'] = 'False'
    showPathChecker = False
  else:
    showPathBtn['text'] = 'True'
    showPathChecker = True

def ballGravity(dx, dy):
  gravity = 3
  friction = 0.5

  while True:
    canvas.move(ball, dx, dy)
    pos = canvas.coords(ball)

    showCoords(pos)

    if showPathChecker:
      drawPath(pos)

    if pos[3] >= HEIGHT and dy <= 2.0:
      dx = 0
      dy = 0
      gravity = 0
      friction = 0
    if pos[3] >= HEIGHT:
      dy *= -1
    if pos[1] <= 1:
      dy *= -1
    if pos[2] >= WIDTH:
      dx = -(dx * friction)
    if pos[0] <= 1:
      dx = -(dx * friction)

    tk.update()

    dy += gravity

    time.sleep(0.025)
     
def onLeftDrag(event):
  print(canvas.coords(ball))
  print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

tk = tkr.Tk()
canvas = tkr.Canvas(tk, width = WIDTH, height = HEIGHT, bg = "white")
canvas.grid()

canvas.old_coords = None

label_x0 = Label(tk, text= "Ball Coord x0: " + "0")
label_y0 = Label(tk, text= "Ball Coord y0: " + "0")
label_x0.place(x = 450, y = 10)
label_y0.place(x = 450, y = 30)

label_x1 = Label(tk, text= "Ball Coord x1: " + "0")
label_y1 = Label(tk, text= "Ball Coord y1: " + "0")
label_x1.place(x = 560, y = 10)
label_y1.place(x = 560, y = 30)

ballExample = Ball(canvas, r, "red")
ball = ballExample.create_ball()

pushBtn = Button(tk, text='PUSH!', width=10,
             height=3, command=pushEvent)

restartBtn = Button(tk, text='RESTART!', width=10,
             height=3, command=restartFunc)

showPathBtn = Button(tk, text='SHOW PATH', width = 10, height = 3, command = showPathCheckerFunc)

w2 = Scale(tk, from_=0, to=30, length=200,tickinterval=10, orient=HORIZONTAL)

canvas.tag_bind('ball', '<B1-Motion>', onLeftDrag)

pushBtn.place(x=225, y=10)
restartBtn.place(x=325, y=10)
showPathBtn.place(x=685, y = 10)
w2.place(x = 10, y = 10)

tk.mainloop()
