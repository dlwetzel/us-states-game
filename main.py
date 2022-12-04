import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
df = pandas.read_csv("50_states.csv")
all_states = [state for state in df["state"]]
answered_states = []
score = 0
t = turtle.Turtle()
t.hideturtle()
t.penup()


while len(answered_states) < 50:
    user_answer = screen.textinput(title=f"{len(answered_states)}/50", prompt="Guess another state").title()
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in answered_states]
        missing_states_df = pandas.DataFrame(missing_states)
        missing_data = missing_states_df.to_csv("missing_states.csv")
        break
    elif user_answer in all_states:
        state_x = df[df["state"] == user_answer]["x"]
        state_y = df[df["state"] == user_answer]["y"]
        t.goto(x=int(state_x), y=int(state_y))
        t.write(f"{user_answer}", font=FONT)
        answered_states.append(user_answer)
        score += 1


t.goto(0, 0)
t.write(f"You've completed the quiz. Your final score is {len(answered_states)}/{len(all_states)}", align="center",
        font=FONT)


screen.mainloop()
