from tkinter import *
from math import *
#--------------------CONSTANTS-----------------------#
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 10
reps = 0
timer = None

#---------------------TIMER RESET---------------------#
def timer_reset():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    checkmark.config(text="")
    global reps
    reps = 0

#---------------------TIMER MECHANISM---------------------#
def start_timer():
    global reps
    work = WORK_MIN * 60
    short_break = SHORT_BREAK * 60
    long_break = LONG_BREAK * 60

    reps += 1
    if reps == 8:
        countdown(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_break)
        timer_label.config(text="Break", fg=PINK)

#---------------------COUNTDOWN MECHANISM---------------------#
def countdown(count):
    mins = floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f'0{secs}'

    canvas.itemconfig(timer_text, text=f'{mins}:{secs}')
    if count > 0:
        global timer
        timer = canvas.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔️'
        checkmark.config(text=marks)

#---------------------UI SETUP---------------------#
screen = Tk()
screen.title('POMODORO🍅')
screen.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 180, image=tomato_img)
timer_text = canvas.create_text(180, 190, text= '00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW, )
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 12, 'normal'), fg='black', bg=YELLOW, highlightthickness=0, command=start_timer )
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'normal'), fg='black', bg=YELLOW, highlightthickness=0, command=timer_reset )
reset_button.grid(row=2, column=2)

checkmark = Label(fg='green', bg=YELLOW)
checkmark.grid(row=3, column=1)

screen.mainloop()
