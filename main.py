import turtle
import pandas
from tkinter import messagebox

ALIGN = "center"
FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_states = data["state"].to_list()
title = "Guess the state"
answered_state = []
while len(answered_state) < 50:

    answer_state = screen.textinput(title=title, prompt="What's another state name?").title()
    # check if answer is within the correct states. if wrong loop again.

    if answer_state == "Exit":
        break
    if answer_state in correct_states:
        # get x and y of the state
        x_axis = int(data[data["state"] == answer_state].x.values[0])
        y_axis = int(data[data.state == answer_state].y.values[0])
        # use the x and y to turtle goto and write state name
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x_axis, y_axis)
        t.write(arg=answer_state, align=ALIGN, font=FONT)

        # reflect score on title
        answered_state.append(answer_state)
        score = len(answered_state)
        title = f"{score}/50 States Guessed"
    else:
        messagebox.showinfo(title="Wrong answer notification", message="State not found in USA")

# states to learn.csv
to_be_filed = correct_states
for state in answered_state:
    to_be_filed.remove(state)

df = pandas.DataFrame(to_be_filed)
df.to_csv("states_to_learn.csv")
