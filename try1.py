from tkinter import *

root = Tk()
root.title("Simple Calculator")

my_label1 = Label(root, text= "Enter the first number:-")
my_label1.pack()

e = Entry(root,fg= "red", width=35, borderwidth=5)
e.pack()

my_label2 = Label(root, text= "Enter the second number:-")
my_label2.pack()

f = Entry(root, highlightbackground= "black",fg= "red",)
f.pack()

def add():
    num1 = int(e.get())
    num2 = int(f.get())
    add = num1 + num2
    my_label1 = Label(root, text="The sum of the two numbers is:- "+str(add))
    my_label1.pack()

def dif():
    num1 = int(e.get())
    num2 = int(f.get())
    diff = num1 - num2
    my_label1 = Label(root, text="The difference of the two numbers is:- "+str(diff))
    my_label1.pack()

def mult():
    num1 = int(e.get())
    num2 = int(f.get())
    multi = num1 * num2
    my_label1 = Label(root, text="The product of the two numbers is:- "+str(multi))
    my_label1.pack()

def div():
    num1 = int(e.get())
    num2 = int(f.get())
    divi = num1 / num2
    my_label1 = Label(root, text="The Quotient of the two numbers is:- "+str(divi))
    my_label1.pack()

add_button = Button(root, text= "Add 'em up!", command=add, fg= "white", highlightbackground= "black")
add_button.pack()

diff_button = Button(root, text= "Subtract 'em", command=dif, fg= "white", highlightbackground= "black")
diff_button.pack()

mult_button = Button(root, text= "Multiply 'em up!", command=mult, fg= "white", highlightbackground= "black")
mult_button.pack()

div_button = Button(root, text= "Divide 'em up!", command=div, fg= "white", highlightbackground= "black")
div_button.pack()

root.mainloop()