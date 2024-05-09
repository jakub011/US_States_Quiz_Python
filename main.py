import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
states_to_learn = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        state = turtle.Turtle()
        state.penup()
        state.color('green')
        state.hideturtle()
        state_data = data[data["state"] == answer_state]
        state.goto(int(state_data.x), int(state_data.y))
        state.write(answer_state)
        guessed_states.append(answer_state)


screen.exitonclick()
