import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    status_label.config(text="Timer")
    timer.config(text="00:00")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def work():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        status_label.config(text="Break", foreground=RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        status_label.config(text="Break", foreground=PINK)
    else:
        count_down(WORK_MIN * 60)
        status_label.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count//60
    seconds = count % 60
    global TIMER
    if seconds < 10:
        seconds = f"0{seconds}"
    timer.config(text=f"{minutes}:{seconds}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        work()
        global reps
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW)
tomato = tkinter.PhotoImage(file="tomato.png")
image_label = tkinter.Label(image=tomato, background=YELLOW)
image_label.grid(column=3, row=3)

timer = tkinter.Label(text="00:00", font=(FONT_NAME, 35, "bold"), background=RED, foreground="white")
timer.grid(column=3, row=3)

check_label = tkinter.Label(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 20))
check_label.grid(column=3, row=4)

start_button = tkinter.Button(text="Start", command=work)
start_button.grid(column=2, row=4)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=4, row=4)

status_label = tkinter.Label(text="Pomodoro Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 35))
status_label.grid(column=3, row=2)

window.mainloop()
