import tkinter as tk
from tkinter import *
from modulefinder import *

action = 0
root = tk.Tk()


def Fight():
    global action
    while action == 0:
        print("You begin a fierce battle that will ultimately leave one of you dead!"'\n''\n')
        action = 1
        print (action)
        root.destroy()

def Flee():
    global action
    while action == 0:
        print("You turn around and run the way you came like a little bitch."'\n''\n')
        action = 2
        print (action)
        root.destroy()
        root.destroy(tk)

Button(text='Flee', command=Flee).pack(fill=X)
Button(text='Fight', command=Fight).pack(fill=X)


if __name__ == "__main__":
    mainloop()
