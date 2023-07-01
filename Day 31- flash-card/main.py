from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")

# ---------------------------- GENERATE NEW WORD ------------------------------- #


def flip_card(card):
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    cross_button.config(state="normal")
    check_button.config(state="normal")


def new_card():
    next_card = random.choice(words)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=next_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    cross_button.config(state="disabled")
    check_button.config(state="disabled")
    window.after(3000, flip_card, next_card)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black"
)
word_text = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black"
)
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, border=0, command=new_card)
cross_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, border=0, command=new_card)
check_button.grid(column=1, row=1)

new_card()

window.mainloop()
