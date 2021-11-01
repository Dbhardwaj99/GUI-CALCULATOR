# Hello friends.. Lemme show you how this calculator works..
# When you run this file.. A calculator will show up on the screen
# in order to do calculations:-
# Enter the first number
# press command
# Enter the second number
# Then press the sign of what you want to do with those two numbers
# And Done!!!
# Do tell me if you see any error of any kind.

# Importing stuff
from tkinter import *

root = Tk()
root.title("Calculator By DIVYANSH")
# root.configure(bg='black')


e = Entry(root, fg="red", width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    # print(num1)
    cur2 = e.get()
    e.delete(0, END)
    num2 = int(cur2)
    sum_of_it = num1 + num2
    e.insert(0, str(sum_of_it))


def button_sub():
    # print(num1)
    cur2 = e.get()
    e.delete(0, END)
    num2 = int(cur2)
    sub_of_it = num1 - num2
    e.insert(0, str(sub_of_it))


def button_mult():
    # print(num1)
    cur2 = e.get()
    e.delete(0, END)
    num2 = int(cur2)
    prod_of_it = num1 * num2
    e.insert(0, str(prod_of_it))


def button_div():
    # print(num1)
    cur2 = e.get()
    e.delete(0, END)
    num2 = int(cur2)
    div_of_it = num1 / num2
    e.insert(0, str(div_of_it))


def button_command():
    cur1 = e.get()
    global num1
    num1 = int(cur1[:])
    e.delete(0, END)


def clear():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_sum = Button(root, text="+", padx=39, pady=20, command=button_add)
button_diff = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_product = Button(root, text="x", padx=40, pady=20, command=button_mult)
button_division = Button(root, text="/", padx=41, pady=20, command=button_div)
button_equal = Button(root, text="Command", padx=13, pady=20, command=button_command)
button_clear = Button(root, text="C", padx=39, pady=20, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_diff.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sum.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_product.grid(row=4, column=1)
button_division.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
root.mainloop()
