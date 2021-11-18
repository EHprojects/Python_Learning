import turtle
import pandas, name_writer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

name_writer = name_writer.NameWriter()

states_data = pandas.read_csv("50_states.csv")

state_names = states_data.state.to_list()
correct_answers = []

while True:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's "
                                                                                              "name?")
    answer_state = answer_state.title()
    if answer_state in state_names and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        x_coord = int(states_data[states_data["state"] == answer_state].x)
        y_coord = int(states_data[states_data["state"] == answer_state].y)
        name_writer.write_name(name=answer_state, x=x_coord, y=y_coord)

