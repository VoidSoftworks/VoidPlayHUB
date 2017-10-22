import tkinter as tk
from tkinter import *
import os.path


root = tk.Tk()

def Encounter_display():
    text1 = Text(root, height=25, width=100)
    photo=PhotoImage(file = os.path.join('images', 'bandit1' + '.GIF'))
    text1.insert(END,'\n')
    text1.image_create(END, image=photo)

    text1.pack(side=LEFT)

    text2 = Text(root, height=25, width=100)
    scroll = Scrollbar(root, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 20, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 25, 'bold'))
    text2.tag_configure('color', foreground='#476042',
    						font=('Tempus Sans ITC', 20, 'bold'))
    text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\nA Stranger Appears\n', 'big')
    quote = """
    A large man covered in animal pelts steps out from behind a rock, brandishing a large steel sword.
    """
    text2.insert(END, quote, 'color')
    text2.insert(END, 'What will you do \n', 'follow')
    text2.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)

    root.mainloop()

if __name__ == "__main__":
    Encounter_display()
