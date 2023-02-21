import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_df = pandas.read_csv("correct_guesses.csv")
correct_guesses_dict = {
    "state": correct_df["state"],
    "x": correct_df["x"],
    "y": correct_df["y"]
}
correct_guesses = correct_guesses_dict["state"].tolist()
correct_guesses_x = correct_guesses_dict["x"].tolist()
correct_guesses_y = correct_guesses_dict["y"].tolist()
print(correct_guesses)
print(correct_guesses_x)
print(correct_guesses_y)


def add_state(answer):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state = data[data["state"] == answer]
    t.goto(int(state.x), int(state.y))
    t.write(f"{answer}")
    correct_guesses.append(str.title(answer))
    correct_guesses_x.append(state.x)
    correct_guesses_y.append(state.y)


for answer in correct_guesses:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state = data[data["state"] == str.title(answer)]
    t.goto(int(state.x), int(state.y))
    t.write(f"{str.title(answer)}")

while len(correct_guesses) < 50:
    try:
        answer = turtle.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt="What's the another state name?").title()
    except:
        break
    if answer == None:
        break
    if answer in states and answer not in correct_guesses:
        print(f"{answer} Found")
        add_state(answer)
    elif answer in correct_guesses:
        print(f"{answer} is already exist")
    else:
        print(f"{answer} Not Found")

if correct_guesses == 50:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write(f"You Won!")
    new_correct_guesses_dict = {
        "state": [],
        "x": [],
        "y": []
    }

    new_data = pandas.DataFrame(new_correct_guesses_dict)
    new_data.to_csv("correct_guesses.csv")
    print("new data saved!")

else:
    new_correct_guesses_dict = {
        "state": correct_guesses,
        "x": correct_guesses_x,
        "y": correct_guesses_y
    }

    new_data = pandas.DataFrame(new_correct_guesses_dict)
    new_data.to_csv("correct_guesses.csv")
    print("new data saved!")

missed_states = []
for state_item in states:
    if state_item not in correct_guesses:
        missed_states.append(state_item)
learn_dict = {
    "missed states": missed_states
}
learn_states = pandas.DataFrame(learn_dict)
learn_states.to_csv("states_to_learn.csv")
print(missed_states)
print(len(missed_states))
screen.mainloop()
