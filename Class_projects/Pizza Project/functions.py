# --------------------------
# Names: Dorje Pradhan, Kamron Swingle
# Date: November 19, 2022
# Assignment: Project 2, Pizza Gui
# Description: Pizza ordering GUI, Has buttons, radio buttons, and checkboxes
# ---------------------------

import tkinter as tk
from functions import *

# main window
window = tk.Tk()
pizzaSize = 'None'  # test later
bgHex = "#f7f3ba"

# size of window and title, minumum shrinkable size
window.geometry("1280x1000")
window.minsize(1000, 870)
window.title("Dorje and Kamron's Pizzaria")

window['background'] = bgHex


# top frame for name, address, and phone number
# grid for side by side label and text box
textFrame = tk.Frame(window)
textFrame['background'] = bgHex

# configure rows and columns
for i in range(0, 2):
    textFrame.columnconfigure(i, weight=1)
    textFrame.rowconfigure(i, weight=1)

# define each textbox with name and empty text box -------------------------
# sticky changes the sizing to "stick" to the sides

# define name label and entry box
name = tk.Label(textFrame, text="Name:", font=("Verdana", 18), foreground="black")
name.grid(row=0, column=0, sticky=tk.W + tk.E)
name['background'] = bgHex

nameBox = tk.Entry(textFrame, width=30)
nameBox.grid(row=0, column=1, sticky=tk.W + tk.E)

# define address Label and entry box
address = tk.Label(textFrame, text="Address:", font=("Verdana", 18), foreground="black")
address.grid(row=1, column=0, sticky=tk.W + tk.E)
address['background'] = bgHex

addressBox = tk.Entry(textFrame, width=30)
addressBox.grid(row=1, column=1, sticky=tk.W + tk.E)

# define phone label and entry box
phone = tk.Label(textFrame, text="Phone Number:", font=("Verdana", 18), foreground="black")
phone.grid(row=2, column=0, sticky=tk.W + tk.E)
phone['background'] = bgHex

phoneBox = tk.Entry(textFrame, width=30)
phoneBox.grid(row=2, column=1, sticky=tk.W + tk.E)

# pack the Frane containing the text boxes
textFrame.pack(fill="x")

# create frame for the small med and large buttons
buttonframe = tk.Frame(window)
for i in range(0, 3):
    buttonframe.columnconfigure(i, weight=1)
buttonframe['background'] = bgHex

# creating a frame for the photo
photoframe = tk.Frame(window)
photoframe.columnconfigure(0, weight=1)
photoframe['background'] = bgHex

# import the photo
photo = tk.PhotoImage(file="pizza1.gif")

# Create a label under the photo, sticks to sides
photoLabel = tk.Label(photoframe, image=photo)
photoLabel.grid(row=0, column=0, sticky=tk.W + tk.E)
photoLabel['background'] = bgHex

# pack in the frame
photoframe.pack(fill="x")


# small medium and large function ( to use as parameters )
def small():
    global pizzaSize
    pizzaSize = 'Small'


def medium():
    global pizzaSize
    pizzaSize = 'Medium'


def large():
    global pizzaSize
    pizzaSize = 'Large'


# small, med, and large buttons
# sets pizzaSize to small med or large accordingly
btn1 = tk.Button(buttonframe, text="Small", font=('Verdana', 18), command=small, foreground="black")
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="Medium", font=('Verdana', 18), command=medium,foreground="black")
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="Large", font=('Verdana', 18), command=large, foreground="black")
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

# pack the buttons
buttonframe.pack(fill='x')

# Integer varaibles to store info when check boxes are selected
cheeseCheckBox = tk.IntVar()
pepperoniCheckBox = tk.IntVar()
sausageCheckBox = tk.IntVar()
mushCheckBox = tk.IntVar()
baconCheckBox = tk.IntVar()
onionCheckBox = tk.IntVar()
peppersCheckBox = tk.IntVar()

# Frame for check boxes
checkBoxFrame = tk.Frame(window)
for i in range(0, 7):
    checkBoxFrame.columnconfigure(i, weight=1)
checkBoxFrame['background'] = bgHex

# define each checkbox with respective topping variable
# formatted to be all in one line
c1 = tk.Checkbutton(checkBoxFrame, text="Cheese", variable=cheeseCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18),foreground="black")
c1.select() # default select cheese
c1.grid(row=0, column=0, sticky=tk.W + tk.E)
c1['background'] = bgHex

c2 = tk.Checkbutton(checkBoxFrame, text="Pepperoni", variable=pepperoniCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18), foreground="black")
c2.grid(row=0, column=1, sticky=tk.W + tk.E)
c2['background'] = bgHex

c3 = tk.Checkbutton(checkBoxFrame, text="Sausage", variable=sausageCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18), foreground="black")
c3.grid(row=0, column=2, sticky=tk.W + tk.E)
c3['background'] = bgHex

c4 = tk.Checkbutton(checkBoxFrame, text="Mushrooms", variable=mushCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18), foreground="black")
c4.grid(row=0, column=3, sticky=tk.W + tk.E)
c4['background'] = bgHex

c5 = tk.Checkbutton(checkBoxFrame, text="Bacon", variable=baconCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18), foreground="black")
c5.grid(row=0, column=4, sticky=tk.W + tk.E)
c5['background'] = bgHex

c6 = tk.Checkbutton(checkBoxFrame, text="Onions", variable=onionCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18), foreground="black")
c6.grid(row=0, column=5, sticky=tk.W + tk.E)
c6['background'] = bgHex

c7 = tk.Checkbutton(checkBoxFrame, text="Peppers", variable=peppersCheckBox, onvalue=1, offvalue=0, font=('Verdana', 18), foreground="black")
c7.grid(row=0, column=6, sticky=tk.W + tk.E)
c7['background'] = bgHex

# pack in the check boxes
checkBoxFrame.pack(fill='x')

# variable to stor info from the radio buttons
r1 = tk.IntVar()

# creaete a frame for the radio buttons
radioFrame = tk.Frame(window)
radioFrame.columnconfigure(0, weight=1) # need this to center radio buttons
for i in range(0, 2) :
    radioFrame.rowconfigure(i, weight=1)
radioFrame['background'] = bgHex

# defininng each radio button (thin, deep, and cheesy crusts)
R1 = tk.Radiobutton(radioFrame, text="Thin Crust", variable=r1, value=1, font=('Verdana', 18), pady=2, foreground="black")
R1.grid(row=0, column=0)
R1['background'] = bgHex

R2 = tk.Radiobutton(radioFrame, text="Deep Dish", variable=r1, value=2, font=('Verdana', 18), pady=2, foreground="black")
R2.grid(row=1, column=0)
R2['background'] = bgHex

R3 = tk.Radiobutton(radioFrame, text="Cheesy Bread", variable=r1, value=3, font=('Verdana', 18), pady=2, foreground="black")
R3.grid(row=2, column=0)
R3['background'] = bgHex

# pack in the radio buttons
radioFrame.pack(fill='x')


# confirmFunc
def checkToppingsPrintTotal():
    toppings = ''
    crust = ''
    total = 0

    # check each check box for the toppings
    if cheeseCheckBox.get() == 1:
        toppings = toppings + 'Cheese '
    if pepperoniCheckBox.get() == 1:
        toppings = toppings + 'Pepperoni '
        total += 1.25
    if sausageCheckBox.get() == 1:
        toppings = toppings + 'Sausage '
        total += 1.25
    if mushCheckBox.get() == 1:
        toppings = toppings + 'Mushrooms '
        total += 1.25
    if baconCheckBox.get() == 1:
        toppings = toppings + 'Bacon '
        total += 1.25
    if onionCheckBox.get() == 1:
        toppings = toppings + 'Onions '
        total += 1.25
    if peppersCheckBox.get() == 1:
        toppings = toppings + 'Peppers '
        total += 1.25

    # check which radio button is selected (only one at a time)
    if r1.get() == 1:
        crust = 'Thin Crust'
    elif r1.get() == 2:
        crust = 'Deep Dish Crust'
    elif r1.get() == 3:
        crust = 'Cheesy Bread Crust'

    # checks which pizza size is selected (one size, don't add)
    if pizzaSize == 'Small':
        total += 10.99
    elif pizzaSize == 'Medium':
        total += 12.99
    elif pizzaSize == 'Large':
        total += 14.99

    # calculate the tax and total bill
    tax = round(total * .0875, 2)
    newTotal = total + tax

    # formatted string output
    #   contains name, address, phone number
    #   Pizza size and crust
    #   toppings, tax, and total
    alltext = f'''
    Your Information Is:
    {nameBox.get()}
    {addressBox.get()} 
    {phoneBox.get()}

    Your Order is:
    {pizzaSize} Pizza
    {crust}
    Your toppings are: {toppings}

    Your tax is: ${format(tax, ".2f")}
    Your total cost is: ${format(newTotal, ".2f")}'''

    #   create a new window to insert the text
    finalWindow.configure(state='normal')
    finalWindow.delete(1.0, 'end')
    finalWindow.insert(1.0, alltext)
    finalWindow.configure(state='disabled')


# submit button
submitButton = tk.Frame(window)
submitButton.columnconfigure(0, weight=1)
confirm = tk.Button(submitButton, text="Submit Order", font=('Verdana', 18), command=checkToppingsPrintTotal, foreground="black")
confirm.grid(row=0, column=0)
submitButton.pack(pady = 10, fill='x')
submitButton['background'] = bgHex

# Frame for the text box
finalFrame = tk.Frame(window)
finalFrame.columnconfigure(0, weight=1)
finalFrame['background'] = bgHex

finalWindow = tk.Text(finalFrame, font=("Verdana", 14), width=85, height=11)
finalWindow.grid(row=1, column=0)
finalWindow.configure(state='disabled')


finalFrame.pack(fill='x')

# main loop ( end of info )
window.mainloop()
