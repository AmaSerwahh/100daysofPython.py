from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.60934, 2)
    km_result_label.config(text=f'{km}')

mile_input = Entry(width=7)
mile_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_result_label = Label(text='0')
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text= "Calculate", command=miles_to_km)
button.grid(row=2, column=1)


def click_button():
    print("I got clicked")


window.mainloop()
