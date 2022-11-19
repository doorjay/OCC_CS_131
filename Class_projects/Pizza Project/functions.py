import tkinter as tk

window = tk.Tk()
pizzaSize = 'None'

window.geometry("1280x900")
window.minsize(1000, 870)
window.title("Dorje and Kamron's Pizzaria")

textFrame = tk.Frame(window)
textFrame.columnconfigure(0, weight=1)
textFrame.columnconfigure(1, weight=1)
textFrame.columnconfigure(2, weight=1)
textFrame.rowconfigure(0, weight=1)
textFrame.rowconfigure(1, weight=1)
textFrame.rowconfigure(2, weight=1)

name = tk.Label(textFrame, text="Name:", font=("Arial", 18))
name.grid(row=0, column=0, sticky=tk.W + tk.E)
nameBox = tk.Entry(textFrame, width=30)
nameBox.grid(row=0, column=1, sticky=tk.W + tk.E)

address = tk.Label(textFrame, text="Address:", font=("Arial", 18))
address.grid(row=1, column=0, sticky=tk.W + tk.E)
addressBox = tk.Entry(textFrame, width=30)
addressBox.grid(row=1, column=1, sticky=tk.W + tk.E)

phone = tk.Label(textFrame, text="Phone Number:", font=("Arial", 18))
phone.grid(row=2, column=0, sticky=tk.W + tk.E)
phoneBox = tk.Entry(textFrame, width=30)
phoneBox.grid(row=2, column=1, sticky=tk.W + tk.E)

textFrame.pack(fill="x")

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

photoframe = tk.Frame(window)
photoframe.columnconfigure(0, weight=1)
photo = tk.PhotoImage(file="pizza1.gif")
photoLabel = tk.Label(photoframe, image=photo)
photoLabel.grid(row=0, column=0, sticky=tk.W + tk.E)
photoframe.pack(fill="x")


def small():
    global pizzaSize
    pizzaSize = 'Small'


def medium():
    global pizzaSize
    pizzaSize = 'Medium'


def large():
    global pizzaSize
    pizzaSize = 'Large'


btn1 = tk.Button(buttonframe, text="Small", font=('Arial', 18), command=small)
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="Medium", font=('Arial', 18), command=medium)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="Large", font=('Arial', 18), command=large)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill='x')

# Buttons
button1 = tk.IntVar()
button2 = tk.IntVar()
button3 = tk.IntVar()
button4 = tk.IntVar()
button5 = tk.IntVar()
button6 = tk.IntVar()
button7 = tk.IntVar()

checkBoxFrame = tk.Frame(window)
checkBoxFrame.rowconfigure(0, weight=1)
checkBoxFrame.columnconfigure(0, weight=1)
checkBoxFrame.columnconfigure(1, weight=1)
checkBoxFrame.columnconfigure(2, weight=1)
checkBoxFrame.columnconfigure(3, weight=1)
checkBoxFrame.columnconfigure(4, weight=1)
checkBoxFrame.columnconfigure(5, weight=1)
checkBoxFrame.columnconfigure(6, weight=1)

# Add functions later
c1 = tk.Checkbutton(checkBoxFrame, text="Cheese", variable=button1, onvalue=1, offvalue=0, font=('Arial', 18))
c1.select()
c1.grid(row=0, column=0, sticky=tk.W + tk.E)
c2 = tk.Checkbutton(checkBoxFrame, text="Pepperoni", variable=button2, onvalue=1, offvalue=0, font=('Arial', 18))
c2.grid(row=0, column=1, sticky=tk.W + tk.E)
c3 = tk.Checkbutton(checkBoxFrame, text="Sausage", variable=button3, onvalue=1, offvalue=0, font=('Arial', 18))
c3.grid(row=0, column=2, sticky=tk.W + tk.E)
c4 = tk.Checkbutton(checkBoxFrame, text="Mushrooms", variable=button4, onvalue=1, offvalue=0, font=('Arial', 18))
c4.grid(row=0, column=3, sticky=tk.W + tk.E)
c5 = tk.Checkbutton(checkBoxFrame, text="Bacon", variable=button5, onvalue=1, offvalue=0, font=('Arial', 18))
c5.grid(row=0, column=4, sticky=tk.W + tk.E)
c6 = tk.Checkbutton(checkBoxFrame, text="Onions", variable=button6, onvalue=1, offvalue=0, font=('Arial', 18))
c6.grid(row=0, column=5, sticky=tk.W + tk.E)
c7 = tk.Checkbutton(checkBoxFrame, text="Peppers", variable=button7, onvalue=1, offvalue=0, font=('Arial', 18))
c7.grid(row=0, column=6, sticky=tk.W + tk.E)

checkBoxFrame.pack(fill='x')

r1 = tk.IntVar()

radioFrame = tk.Frame(window)
radioFrame.rowconfigure(0, weight=1)
radioFrame.rowconfigure(1, weight=1)
radioFrame.rowconfigure(2, weight=1)
radioFrame.columnconfigure(0, weight=1)

R1 = tk.Radiobutton(radioFrame, text="Thin Crust", variable=r1, value=1, font=('Arial', 18), pady=2)
R1.grid(row=0, column=0)
R2 = tk.Radiobutton(radioFrame, text="Deep Dish", variable=r1, value=2, font=('Arial', 18), pady=2)
R2.grid(row=1, column=0)
R3 = tk.Radiobutton(radioFrame, text="Cheesy Bread", variable=r1, value=3, font=('Arial', 18), pady=2)
R3.grid(row=2, column=0)

radioFrame.pack(fill='x')


def confirmFunc():
    toppings = ''
    crust = ''
    total = 0
    if button1.get() == 1:
        toppings = toppings + 'Cheese '
    if button2.get() == 1:
        toppings = toppings + 'Pepperoni '
        total += 1.25
    if button3.get() == 1:
        toppings = toppings + 'Sausage '
        total += 1.25
    if button4.get() == 1:
        toppings = toppings + 'Mushrooms '
        total += 1.25
    if button5.get() == 1:
        toppings = toppings + 'Bacon '
        total += 1.25
    if button6.get() == 1:
        toppings = toppings + 'Onions '
        total += 1.25
    if button7.get() == 1:
        toppings = toppings + 'Peppers '
        total += 1.25
    if r1.get() == 1:
        crust = 'Thin Crust'
    elif r1.get() == 2:
        crust = 'Deep Dish Crust'
    elif r1.get() == 3:
        crust = 'Cheesy Bread Crust'
    if pizzaSize == 'Small':
        total += 10.99
    elif pizzaSize == 'Medium':
        total += 12.99
    elif pizzaSize == 'Large':
        total += 14.99
    tax = round(total * .0875, 2)
    newTotal = total + tax
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
    finalWindow.configure(state='normal')
    finalWindow.delete(1.0, 'end')
    finalWindow.insert(1.0, alltext)
    finalWindow.configure(state='disabled')


submitButton = tk.Frame(window)
submitButton.columnconfigure(0, weight=1)

confirm = tk.Button(submitButton, text="Submit Order", font=('Arial', 18), command=confirmFunc)
confirm.grid(row=0, column=0)

submitButton.pack(fill='x')

finalFrame = tk.Frame(window)
finalFrame.columnconfigure(0, weight=1)

finalWindow = tk.Text(finalFrame, font=("Arial", 18), width=45, height=10)
finalWindow.grid(row=1, column=0)
finalWindow.configure(state='disabled')


finalFrame.pack(fill='x')

window.mainloop()

'''btn1 = tk.Button(buttonframe, text="Small", height=10, width=10, font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)'''
