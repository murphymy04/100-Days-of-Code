import tkinter
from tkinter import messagebox
import pandas
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.delete("0", "end")
    password_entry.insert("0", password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(user_entry.get()) == 0 or len(password_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empy!")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(), message=f"These are the details entered: "
                                                                      f"\nEmail: {user_entry.get()}"
                                                                      f"\nPassword: {password_entry.get()} "
                                                                      f"\nIs it ok to save?")
        if is_ok:
            data_dict = {
                "Website": [web_entry.get()],
                "Email/Username": [user_entry.get()],
                "Password": [password_entry.get()]
            }
            data = pandas.DataFrame(data_dict)
            data.to_csv("data.csv", mode="a", index=False, header=False)
            web_entry.delete("0", "end")
            user_entry.delete("0", "end")
            password_entry.delete("0", "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = tkinter.Label(text="Website:")
web_label.grid(row=1, column=0)
web_entry = tkinter.Entry(width=52)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = tkinter.Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=34)
password_entry.grid(row=3, column=1)
pass_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
pass_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
