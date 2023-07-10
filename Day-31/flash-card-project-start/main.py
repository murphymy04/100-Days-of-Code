import tkinter
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
num = random.randint(0, 100)

# Flashcard Creation
try:
    data = pd.read_csv("data/words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")


# Pick a random French word and flip card after 3 seconds
def rand_french():
    global num, flip_timer
    screen.after_cancel(flip_timer)
    num = random.randint(0, 100)
    french_word = data_dict[num].get("French")
    title_label.config(text="French", fg="black", bg="white")
    word_label.config(text=french_word, fg="black", bg="white")
    flashcard.itemconfig(flashcard_img, image=card_front)
    flip_timer = screen.after(3000, func=flip)


# correct function
def correct():
    global num
    new_dict = data_dict
    del new_dict[num]
    new_data = pd.DataFrame.from_records(new_dict)
    new_data.to_csv("data/words_to_learn.csv", mode="w", index=False)
    rand_french()


# flip card
def flip():
    global num
    title_label.config(text="English", fg="white", bg=BACKGROUND_COLOR)
    word_label.config(text=data_dict[num].get("English"), fg="white", bg=BACKGROUND_COLOR)
    flashcard.itemconfig(flashcard_img, image=card_back)


# UI Setup
screen = tkinter.Tk()
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
screen.title("Flashcards")
flip_timer = screen.after(ms=3000, func=flip)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
flashcard = tkinter.Canvas(height=526, width=800)
flashcard_img = flashcard.create_image(410, 260, image=card_front)
flashcard.grid(column=0, row=0, columnspan=2)

check_button_img = tkinter.PhotoImage(file="images/right.png")
x_button_img = tkinter.PhotoImage(file="images/wrong.png")
check_button = tkinter.Button(image=check_button_img, command=correct)
check_button.grid(column=1, row=1)
wrong_button = tkinter.Button(image=x_button_img, command=rand_french)
wrong_button.grid(column=0, row=1)

title_label = tkinter.Label(text="French", font=("Ariel", 40, "italic"), bg="white")
title_label.place(x=400, y=150, anchor="center")
word_label = tkinter.Label(text=data_dict[num].get("French"), font=("Ariel", 60, "bold"), bg="white")
word_label.place(x=400, y=263, anchor="center")

screen.mainloop()
