from tkinter import *

root = Tk()
root.title("Calculator")
# root.configure(bg='black')


e = Entry(root, fg="red", width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady= 10)

def button_click(number):
    e.insert(0, number)

def clear():
    e.delete(0, END)


buttoon_1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
buttoon_2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
buttoon_3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
buttoon_4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
buttoon_5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
buttoon_6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
buttoon_7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
buttoon_8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
buttoon_9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))
buttoon_0 = Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
buttoon_add = Button(root, text="+", padx=39, pady=20, command=lambda : button_click())
buttoon_equal = Button(root, text="=", padx=180, pady=20, command=lambda : button_click())
buttoon_clear = Button(root, text="C", padx=39, pady=20, command=clear)

buttoon_1.grid(row= 3,column= 0)
buttoon_2.grid(row= 3,column= 1)
buttoon_3.grid(row= 3,column= 2)
buttoon_0.grid(row= 3,column= 3)

buttoon_4.grid(row= 2,column= 0)
buttoon_5.grid(row= 2,column= 1)
buttoon_6.grid(row= 2,column= 2)
buttoon_add.grid(row=2,column=3)

buttoon_7.grid(row= 1,column= 0)
buttoon_8.grid(row= 1,column= 1)
buttoon_9.grid(row= 1,column= 2)
buttoon_clear.grid(row=1,column=3)

buttoon_equal.grid(row=4,column=0,columnspan=4)
root.mainloop()