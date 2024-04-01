import turtle
import pandas

FONT = ("Courier", 16, "normal")

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if answer == "Exit":
        # missing_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states_list:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        x_cor = int(state_data.x.item())
        y_cor = int(state_data.y.item())
        pen.goto(x_cor, y_cor)
        pen.write(f"{answer}", align="center", font=FONT)
