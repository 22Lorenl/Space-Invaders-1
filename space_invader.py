# print("Hello World")
# Turtle = 500
# Cookies = Turtle
# Turtle + Cookies
from tkinter import *
import time
import random

tk = Tk()
tk.title("Ball Paddle Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update

class Ball: 
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_oval910, 10, 25, 25, fill=color)
    self.canvas.move(self.id, 245, 100)
    starts = [-3, -2, -1, 1, 2, 3]
    random.shuffle(starts)
    self.x = starts[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
  def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)
    if pos [1] <= 0:
      self.y = 3
    if pos [3] >= self.canvas_height:
      self.y = -3
    if pos[0] <= 0:
      self.x = 3
    if pos[2] >= self.canvas_width:
      self.x = -3
 
ball = Ball(canvas, 'blue')

while 1:
  ball.draw()
  tk.update_idletasks()
  tk.update(0
  time.sleep(0.01)
  