import turtle
import pandas

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

guesses = []
score = 0
guess_over = False
while not guess_over:
    guess = screen.textinput(title=f"Guess the state....{score}/50 states correct.", prompt="Guess another state name").title()
    if guess == "Quit":
        unguessed_states = [state for state in states if state not in guesses]
        #for state in states:
            #if state not in guesses:
                #unguessed_states.append(state)
        new_data = pandas.DataFrame(unguessed_states).to_csv("states_to_learn.csv")
        break

    for state in states:
        if guess == state:
            x = int(data[data['state'] == guess].x)
            y = int(data[data['state'] == guess].y)
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            tim.goto(x, y)
            tim.write(guess)
            guesses.append(state)
            score += 1



