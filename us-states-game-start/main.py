import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

# set turtle shape as image
image_bkg = "blank_states_img.gif"
screen.addshape(image_bkg)
turtle.shape(image_bkg)

# get on mouse click coordonates:
#def get_mouse_click_coord(x,y):
    #print(x,y)

#turtle.onscreenclick(get_mouse_click_coord)
#turtle.mainloop()


#____________________________________

# Read state data file
states_data = pandas.read_csv("50_states.csv")
state_list = []
x_list = []
y_list = []

for state in states_data.state:
    state_list.append(state)
print(state_list)

for x in states_data.x:
    x_list.append(x)
print(x_list)

for y in states_data.y:
    y_list.append(y)

guessed_states = []



while len(guessed_states) < 50:

    with open("saving_file.csv", mode="r") as file:
        score = int(file.read())

    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state's name?").title()


    if answer_state == "Exit":
        break
    for answer in state_list:
        if answer == answer_state:
            guessed_states.append(answer)
            with open("saving_file.csv",mode="w") as file:
                file.write(f"{len(guessed_states)}")
            correct_guesses = turtle.Turtle()
            correct_guesses.hideturtle()
            correct_guesses.penup()
            correct_guesses.goto(x_list[state_list.index(answer)], y_list[state_list.index(answer)])
            correct_guesses.write(f"{answer}")
            print(f"{len(guessed_states)}")


screen.mainloop()






























