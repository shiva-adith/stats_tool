from tkinter import *
from Modules import sum, mean

# TODO: Insert a checkbutton or listbox to provide choices b/w multiple functions.

window = Tk()
window.title("Stats Tool")
window.minsize(width=600, height=500)
window.config(padx=150, pady=150)


def calc_mean():
    numbers = [float(num) for num in entry_field.get().split()]
    print(numbers)
    print(type(numbers))
    result = round(mean.mean(numbers), 2)
    display_label.config(text=f"{result}")


# Labels:
entry_label = Label(text="Enter the numbers")
entry_label.config(padx=15, pady=15)
entry_label.grid(column=0, row=0)

indicator_label = Label(text=" = ")
indicator_label.grid(column=2, row=0)

display_label = Label()
display_label.grid(column=3, row=0)

# Entry:
entry_field = Entry(width=20)
entry_field.grid(column=1, row=0)

# Buttons:
calculate_button = Button(text="Calculate", command=calc_mean)
calculate_button.grid(column=1, row=1)

window.mainloop()
