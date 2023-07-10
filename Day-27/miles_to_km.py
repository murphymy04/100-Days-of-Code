import tkinter


def conversion():
    num = float(input.get())
    num *= 1.61
    answer = tkinter.Label()
    answer.config(text=f"{num}")
    answer.grid(column=1, row=1)


window = tkinter.Tk()
window.title("Miles to Kilometers Converter")

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal = tkinter.Label(text="is equal to")
is_equal.grid(column=0, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=conversion)
button.grid(column=1, row=3)

window.mainloop()
