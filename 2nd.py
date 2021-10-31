from tkinter import *

root = Tk()

# creating the thing
my_label1 = Label(root, text="Hello World!")
my_label2 = Label(root, text="     7     ")
my_label3 = Label(root, text="    7      ")
my_label4 = Label(root, text="My name is divansh.")

# shoving it onto screen
my_label1.grid(row= 0, column= 0)
my_label3.grid(row= 1, column= 1)
my_label2.grid(row= 1, column= 2)
my_label4.grid(row= 1, column= 3)

root.mainloop()

