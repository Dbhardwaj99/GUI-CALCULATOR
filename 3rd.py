from tkinter import *
root = Tk()

def click():
    my_label = Label(root, text= "Yes, you're racist.")
    my_label.pack()

my_button = Button(root, text= "Are you racist?", command= click, fg= "red", highlightbackground= "blue")
my_button.pack()

root.mainloop()