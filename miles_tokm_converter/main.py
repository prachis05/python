from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km2 = round(miles * 1.609)
    km_result.config(text=km2)


window = Tk()
window.title("Miles to Kilometer converter")


miles_input = Entry()
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)


# Label
km = Label(text="Km")
km.grid(column=2, row=1)
km.config(padx=20, pady=20)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

# Label
equal_To = Label(text="is equal to")
equal_To.grid(column=0, row=1)
equal_To.config(padx=20, pady=20)


# Button
cal = Button(text="Calculate", command=miles_to_km)
cal.grid(column=1, row=2)
cal.config(padx=10, pady=10)


window.mainloop()