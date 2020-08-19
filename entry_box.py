from tkinter import *
root = Tk()

e=Entry(root)
e.pack()


def click():
    #txt='Hi!'+e.get()
    mylabel=Label(root,text=e.get())
    mylabe.pack()#text=txt will do the same thing

mybutton=Button(root,text='Enter your Name and click!',command=click)
mybutton.pack()

root.mainloop()


from tkinter import *
roo = Tk()
e = Entry(roo,width=50,bg='black',fg='white')
e.pack()
#e.insert(0,'Enter your name')

def myclick():
    label=Label(roo,text=' hello ' + e.get(),bg='black',fg='white')
    label.pack()

myL = Button( roo, text="  Click Me!  ", command=myclick)

myL.pack()
roo.mainloop()
