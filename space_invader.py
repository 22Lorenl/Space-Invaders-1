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

class Paddle:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_rectangle(20, 20, 100, 20, fill=color)
    self.x = 0
    self.canvas_width = self.canvas.winfo_width()
    self.canvas.bind_all('KeyPress-a>', self.turn_left)
    self.canvas.bind_all('KeyPress-d>', self.turn_right)
    self.canvas.bind_all('KeyPress-s>', self.forward)
    self.canvas.bind_all('KeyPress-d>', self.backwards)
   def draw(self):
    self.canvas.move(self.id, self.x, 0)
    pos = self.canvas.coords(self.id)
    if pos [0] <=0:
      self.x = 0
    elif pos [2] >= self.canvas_width:
      self.x = 0
   def turn_left(self, evt):
    self.x = -2
   def turn_right(self, evt):
    self.x = 2
   def forward(self, evt):
    self.y = 2
   def forward(self, evt):
    self.y = -2

    #Some trouble
r = random.randint(0,255)
b = random.randint(0,255)
g = random.randint(0,255)

ball = Ball(canvas, (r,g,b) )

while 1:
  ball.draw()
  tk.update_idletasks()
  tk.update(0
  time.sleep(0.01)
  
