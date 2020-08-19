from tkinter import *
import tkinter.font as font
root = Tk()
root.title("SIMPLE CALCULATOR")

myFont = font.Font(size=12)

exp = ""
e = Entry(root,width=50,borderwidth=6, fg = 'white', bg = 'black')
#add font() to increase the size but orienatation gets changed so
e.grid(row = 0, column =0 ,columnspan = 5)

#l2=Label(root,text="0",font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
#l2.grid(row=0,column=1,columnspan=4)

def press(num):
    global exp
    exp = exp + str(num)
    e.delete(0,END)
    e.insert(0, exp)


def pressequal():
    global exp
    e.delete(0, END)
    try:
        e.insert(0,str(eval(exp)))
#        l2=Label(root,text=str(eval(exp)),font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
#        l2.grid(row=0,column=1,columnspan=4)
    except:
        e.insert(0,'Error')
#        l2=Label(root,text="Error",font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
#        l2.grid(row=0,column=1,columnspan=4)
    exp =""

def clearall():
    global exp
    exp =""
    e.delete(0, END)
#    l2=Label(root,text="0",font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
#    l2.grid(row=0,column=1,columnspan=4)


#give padx=103.5 for two button length
button_0 = Button(root, text = '0', padx = 30, pady = 20, command = lambda: press(0), bg = 'brown', fg = 'white')
button_1 = Button(root, text = '1',padx = 30, pady = 20, command = lambda: press(1), bg = 'brown', fg = 'white')
button_2 = Button(root, text = '2',padx = 30, pady = 20, command = lambda: press(2), bg = 'brown', fg = 'white')
button_3 = Button(root, text = '3',padx = 30, pady = 20, command = lambda: press(3), bg = 'brown', fg = 'white')
button_4 = Button(root, text = '4',padx = 30, pady = 20, command = lambda: press(4), bg = 'brown', fg = 'white')
button_5 = Button(root, text = '5',padx = 30, pady = 20, command = lambda: press(5), bg = 'brown', fg = 'white')
button_6 = Button(root, text = '6',padx = 30, pady = 20, command = lambda: press(6), bg = 'brown', fg = 'white')
button_7 = Button(root, text = '7',padx = 30, pady = 20, command = lambda: press(7), bg = 'brown', fg = 'white')
button_8 = Button(root, text = '8',padx = 30, pady = 20, command = lambda: press(8), bg = 'brown', fg = 'white')
button_9 = Button(root, text = '9',padx = 30, pady = 20, command = lambda: press(9), bg = 'brown', fg = 'white')
button_dot = Button(root,text = '.',padx = 32.49, pady = 20, command = lambda: press('.'), bg = 'brown', fg = 'white')
button_add = Button(root, text = '+', padx = 30, pady = 55, command = lambda: press('+'), bg = 'brown', fg = 'white')
button_sub = Button(root, text = '-', padx = 32, pady = 20, command = lambda: press('-'), bg = 'brown', fg = 'white')
button_mul = Button(root, text = '*', padx = 31, pady = 20, command = lambda: press('*'), bg = 'brown', fg = 'white')
button_div = Button(root,  text ='/', padx = 32, pady = 20, command = lambda: press('/'), bg = 'brown', fg = 'white')
button_equals = Button(root, text  = '=', padx = 30, pady = 20, command =  pressequal, bg = 'brown', fg = 'white')
button_clear = Button(root, text = 'AC', padx = 104.45, pady = 20, command = clearall, bg = 'brown', fg = 'white')

button_0['font'] = myFont
button_1['font'] = myFont
button_2['font'] = myFont
button_3['font'] = myFont
button_4['font'] = myFont
button_5['font'] = myFont
button_6['font'] = myFont
button_7['font'] = myFont
button_8['font'] = myFont
button_9['font'] = myFont
button_dot['font'] = myFont
button_add['font'] = myFont
button_sub['font'] = myFont
button_mul['font'] = myFont
button_div['font'] = myFont
button_equals['font'] = myFont
button_clear['font'] = myFont


button_0.grid(row = 4,column = 0)
button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)
button_dot.grid(row = 4,column = 1)
button_equals.grid(row = 4, column = 2)
button_clear.grid(row = 5,column = 0, columnspan = 3)
button_add.grid(row = 1, column = 3, rowspan = 2)
button_sub.grid(row = 3, column = 3)
button_mul.grid(row = 4, column = 3)
button_div.grid(row = 5, column = 3)

root.mainloop()
