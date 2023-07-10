from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.title("U.S States Game")
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

answer = screen.textinput("", "Name a State:")
screen.mainloop()

if answer in all_states:
    t = Turtle()
    t.hideturtle()
    t.pu()
    state_data = data[data.state == answer]
    t.goto(state_data.x, state_data.y)
    t.write(state_data.state)