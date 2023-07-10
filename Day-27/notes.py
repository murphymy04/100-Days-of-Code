import tkinter

window = tkinter.Tk()
window.title("Notes")
window.minsize(width=500, height=300)

# label
label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "New Text"
label.config(text="New Text")


# Button

def button_clicked():
    label["text"] = "Button Got Clicked"


def input_button():
    label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()


button2 = tkinter.Button(text="Click after Input", command=input_button)
button2.pack()


window.mainloop()
