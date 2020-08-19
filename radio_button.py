from tkinter import *
from PIL import ImageTk,Image

root = Tk()


MODES = [('Pepperoni', 'Pepperoni' ),
          ('cheese', 'cheese'),
          ('panner', 'panner'),
          ('onion', 'onion')
          ]

pizza = StringVar()
pizza.set('Pepperoni')

for text,mode in MODES:
    Radiobutton(root, text = text, variable=pizza, value=mode).pack(anchor=W)

def click(value):
    myLabel = Label(root, text=value).pack()

mybutton=Button(root,text = 'click here!', command=lambda:click(pizza.get())).pack()
mainloop()
