BG_COLOR = '#B1DDC6'
from tkinter import *
import pandas
import random

data = pandas.read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient='records')
random_word = {}

def translate():
    canvas.itemconfig(canvas_img, image =back_card_img)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(french_word, text= random_word['English'], fill='white')

def generate_word():
    global random_word
    random_word = random.choice(data_dict)
    canvas.itemconfig(canvas_img, image=front_card_img)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(french_word, text=random_word['French'], fill='black')
    screen.after(2000, translate, )

screen = Tk()
screen.config(bg=BG_COLOR, padx=50, pady=50, width=1000, height=1000)
screen.title('Flash Card App')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
front_card_img = PhotoImage(file='./images/card_front.png')
back_card_img = PhotoImage(file='./images/card_back.png')
canvas_img = canvas.create_image(400, 263, image=front_card_img)
title = canvas.create_text(400, 150, text='Title', font= ('Arial', 30, 'italic'), fill='black')
french_word = canvas.create_text(400, 280, text='word', font= ('Arial', 50, 'bold'), fill='black')
canvas.grid(row=0, column=1)

right_button_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_img, highlightthickness=0, bg=BG_COLOR, command=generate_word)
right_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BG_COLOR, command=generate_word)
wrong_button.grid(row=1, column=2)

screen.mainloop()




