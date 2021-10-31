from tkinter import *
root = Tk()

e = Entry(root, highlightbackground= "black",fg= "red",)
e.pack()

def click():
    my_label = Label(root, text= "Hello "+e.get())
    my_label.pack()

my_button = Button(root, text= "Enter your name:-", command= click, fg= "white", highlightbackground= "black")
my_button.pack()

root.mainloop()