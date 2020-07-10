import tkinter as tk
import random

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()
    
  def create_widgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there["text"] = "Hello!\n(Click me!)"
    self.hi_there["command"] = self.say_hi
    self.hi_there.pack(side="top")

    self.im_bored = tk.Button(self)
    self.im_bored["text"] = "I'm bored!"
    self.im_bored["command"] = self.say_bored
    self.im_bored.pack(side="left")

    self.roll = tk.Button(self)
    self.roll["text"] = "Roll!"
    self.roll["command"] = self.roll_number
    self.roll.pack(side="right")
    
    self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    self.quit.pack(side="bottom")
    
  def say_hi(self):
    print("Hello too from me!")

  def say_bored(self):
    print("Me too!")

  def roll_number(self):
    print("You rolled : {:f}".format(random.random()))
    

root = tk.Tk()
app = Application(master=root)
app.mainloop()
