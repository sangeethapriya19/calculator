from tkinter import *

root=Tk()

input=Entry(root, width=75)
input.grid(row=0, column=0, columnspan=4, padx=12, pady=12)

def btnclick(num):
    current=input.get()
    input.delete(0, END)
    input.insert(0, str(current)+str(num))

def add():
    firstnum=input.get()
    global math
    math='addition'
    global f
    f=int(firstnum)
    input.delete(0, END)

def sub():
    firstnum=input.get()
    global math
    math='subtraction'
    global f
    f=int(firstnum)
    input.delete(0, END)

def mul():
    firstnum=input.get()
    global math
    math='multiplication'
    global f
    f=int(firstnum)
    input.delete(0, END)

def div():
    firstnum=input.get()
    global math
    math='division'
    global f
    f=int(firstnum)
    input.delete(0, END)

def clear():
    input.delete(0, END)

def equal():
    secondnum=input.get()
    input.delete(0, END)
    if math=='addition':
        input.insert(0, f+int(secondnum))
    elif math=='subtraction':
        input.insert(0, f-int(secondnum))
    elif math=='multiplication':
        input.insert(0, f*int(secondnum))
    elif math=='division':
        input.insert(0, f/int(secondnum))
    
button_1=Button(root, text="1", padx=50, pady=25, command=lambda:btnclick(1))
button_2=Button(root, text="2", padx=50, pady=25, command=lambda:btnclick(2))
button_3=Button(root, text="3", padx=50, pady=25, command=lambda:btnclick(3))
button_4=Button(root, text="4", padx=50, pady=25, command=lambda:btnclick(4))
button_5=Button(root, text="5", padx=50, pady=25, command=lambda:btnclick(5))
button_6=Button(root, text="6", padx=50, pady=25, command=lambda:btnclick(6))
button_7=Button(root, text="7", padx=50, pady=25, command=lambda:btnclick(7))
button_8=Button(root, text="8", padx=50, pady=25, command=lambda:btnclick(8))
button_9=Button(root, text="9", padx=50, pady=25, command=lambda:btnclick(9))
button_0=Button(root, text="0", padx=50, pady=25, command=lambda:btnclick(0))
button_add=Button(root, text="+", padx=50, pady=24, command=add)
button_sub=Button(root, text="-", padx=50, pady=25, command=sub)
button_mul=Button(root, text="*", padx=50, pady=25, command=mul)
button_div=Button(root, text="/", padx=50, pady=25, command=div)
button_clear=Button(root, text="AC", padx=45, pady=25, command=clear)
button_equal=Button(root, text="=", padx=49, pady=25, command=equal)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)


button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)


root.mainloop()