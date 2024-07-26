from ast import Lambda
from tkinter import *

root=Tk()
root.title("Calculator Program")
e = Entry(root, width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
Label = Label(root, text=" Calculator Made by OFV")
Label.grid(row=0, column = 5)

FirstNumber = 0
def button_click(number):
      current = e.get()
      e.delete(0 , END)
      e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)
   
def button_add():
    global FirstNumber 
    FirstNumber = int(e.get())
    button_clear()
    
    
def button_Equal():
    SecondNumber = int(e.get())
    button_clear()
    e.insert(0, str((FirstNumber) + (SecondNumber))) 
    
#Define Buttons
Button1 = Button(root, text="1", padx = 40, pady= 20 ,command=lambda: button_click(1))
Button2 = Button(root, text="2", padx = 40, pady= 20 ,command=lambda: button_click(2))
Button3 = Button(root, text="3", padx = 40, pady= 20 ,command=lambda: button_click(3))
Button4 = Button(root, text="4", padx = 40, pady= 20 ,command=lambda: button_click(4))
Button5 = Button(root, text="5", padx = 40, pady= 20 ,command=lambda: button_click(5))
Button6 = Button(root, text="6", padx = 40, pady= 20 ,command=lambda: button_click(6))
Button7 = Button(root, text="7", padx = 40, pady= 20 ,command=lambda: button_click(7))
Button8 = Button(root, text="8", padx = 40, pady= 20 ,command=lambda: button_click(8))
Button9 = Button(root, text="9", padx = 40, pady= 20 ,command=lambda: button_click(9))
Button0 = Button(root, text="0", padx = 40, pady= 20 ,command=lambda: button_click(0))
buttonAdd = Button(root, text="+", padx = 40, pady= 20 ,command=lambda: button_add())
buttonEqual = Button(root, text="=", padx = 91, pady= 20 ,command=button_Equal)
buttonClear = Button(root, text="Clear", padx = 91, pady= 20 ,command=button_clear)

# Put the buttons on the screen
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)
Button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
root.mainloop()