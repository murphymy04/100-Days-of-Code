import time
import tkinter
w = 25


def countdown(t):
    total_seconds = t * 60
    while total_seconds > 0:
        time_left = tkinter.Label()
        minutes = total_seconds//60
        seconds = total_seconds % 60
        time_left.config(text=f"{minutes}:{seconds}")
        time_left.grid(column=3, row=3)
        time.sleep(1)
        total_seconds -= 1


class CountdownTimer:
    def __init__(self):
        pass
