from tkinter import *


def convert():
    # 1 mile = 1.60934 km
    miles = float(miles_input.get())
    result = miles * 1.60934
    lab_result.config(text=str(result))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

lab_miles = Label(text="Miles")
lab_miles.grid(row=0, column=2)

lab_equals = Label(text="is equal to")
lab_equals.grid(row=1, column=0)

lab_result = Label(text=miles_input.get())
lab_result.grid(row=1, column=1)

lab_km = Label(text="Km")
lab_km.grid(row=1, column=2)

button_calc = Button(text="Calculate", command=convert)
button_calc.grid(row=2, column=1)

window.mainloop()
