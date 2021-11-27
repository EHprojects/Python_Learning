from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}


# --------------------------- Import Data  ----------------------------- #
try:
    word_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = word_data.to_dict(orient="records")
# word_dict slice: [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]


# ------------------------ Control Functions  --------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)  # example: {'French': 'car', 'English': 'because'}
    word = current_card["French"]
    canvas.itemconfig(bg_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(bg_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI Setup  ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
bg_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# title_label = Label(text="Title", bg="white", font=("Arial", 40, "italic"))
# title_label.place(x=400, y=150, anchor="center")
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

# word_label = Label(text="Word", bg="white", font=("Arial", 60, "bold"))
# word_label.place(x=400, y=263, anchor="center")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
