from tkinter import *
root = Tk()
root.title("Calculator")
icon = PhotoImage(file="D:\\Personalisation\\calculator.png")
root.iconphoto(False, icon)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

class start:
    op = ""

#Functions
def firnum():
    try:
        global n1
        n1 = float(e.get())
        e.delete(0, END)
    except:
        return
def click(num):
    ctn = e.get()
    e.delete(0, END)
    e.insert(0, str(ctn) + str(num))
def add():
    firnum()
    start.op = "sum"
def subtract():
    firnum()
    start.op = "subtract"
def multiply():
    firnum()
    start.op = "multiply"
def divide():
    firnum()
    start.op = "divide"
def clear():
    e.delete(0, END)
def equals():
    n2 = float(e.get())
    e.delete(0, END)
    if start.op == "sum":
        e.insert(0, str(n1 + n2))
    elif start.op == "subtract":
        e.insert(0, str(n1 - n2))
    elif start.op == "multiply":
        e.insert(0, str(n1 * n2))
    else:
        e.insert(0, str(n1 / n2))

#Defining buttons
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
bp = Button(root, text="+", padx=40, pady=20, command=add)
be = Button(root, text="=", padx=140, pady=20, command=equals)
bc = Button(root, text="Clear", padx=30, pady=20, command=clear)
bs = Button(root, text="-", padx=40, pady=20, command=subtract)
bd = Button(root, text="÷", padx=40, pady=20, command=divide)
bm = Button(root, text="×", padx=40, pady=20, command=multiply)

#Locations of buttons
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
bp.grid(row=4, column=1)
be.grid(row=6, column=0, columnspan=3)
bs.grid(row=4, column=2)
bm.grid(row=5, column=0)
bd.grid(row=5, column=1)
bc.grid(row=5, column=2)

root.mainloop()