import tkinter as tk
from gameBoardSubsystem.main import gameBoard
from dbSubsystem.main import dbSubsystem
from displaySubsystem.main import *

def create_checkbox_grid(rows, cols, w):
     checkbox_grid = []
     for i in range(rows):
          row = []
          for j in range(cols):
               var = tk.BooleanVar()
               checkbox = tk.Checkbutton(w, variable=var)
               checkbox.grid(row=i+1, column=j)
               row.append(var)
          checkbox_grid.append(row)
     return checkbox_grid

def launchwithconf(name):
     new_window = tk.Tk()
     new_window.title(f'inferno_launchconf -- configuring \'{name}\'...')

     label = tk.Label(new_window, text="Configure your new game instance: ")
     label.grid(row=0, columnspan=8)
     checkbox_grid = create_checkbox_grid(7, 8, new_window)
     button = tk.Button(new_window, text="LAUNCH", command=(lambda: launch(new_window, name, board=[[int(j.get()) for j in i] for i in checkbox_grid])))
     button.grid(row=8, columnspan=8)

     new_window.mainloop()


def prelaunch():
     name = text_input.get()
     dbs = dbSubsystem()
     if dbs.retrieveGame(name):
          launch(root, name)
     else:
          root.destroy() 
          launchwithconf(name) 

def launch(w, name, board=False):
     w.destroy()
     print('launch called')
     gb = gameBoard(name, board)
     gb.save()
     masterDSub = DisplaySubsystem(512,512,"inferno",'inferno', gb)
     masterDSub.run()



root = tk.Tk()
root.title("inferno_prelaunchassistant")

label = tk.Label(root, text="Create/Retrieve board")
label.pack()

label = tk.Label(root, text="Board name? ")
label.pack()

text_input = tk.Entry(root)
text_input.pack()

button = tk.Button(root, text="LAUNCH", command=prelaunch)
button.pack()

root.mainloop()