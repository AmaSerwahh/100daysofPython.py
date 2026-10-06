from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.config(bg=THEME_COLOR, padx=20, pady=20, )#width=500, height=500)

        self.score_label = Label(text=f'Score: 0', highlightthickness=0, bg=THEME_COLOR, fg='white', font=('arial', 15, 'bold'))
        self.score_label.grid(row=2, column=1)

        self.canvas = Canvas(width=300, height=250, background='white',)
        self.question = self.canvas.create_text(150, 125, width=280, text='Text', font=('Arial', 15, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)

        wrong_btn_img = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=wrong_btn_img,highlightthickness=0,command=self.is_correct)
        self.wrong_button.grid(row=3, column=0)
        correct_btn_img = PhotoImage(file='./images/true.png')
        self.correct_button = Button(image=correct_btn_img,highlightthickness=0,command=self.is_wrong)
        self.correct_button.grid(row=3, column=1)

        self.get_next_question()

        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz🥳🚀🙂‍↕️", fill="black")
            self.wrong_button.config(state='disabled')
            self.correct_button.config(state='disabled')

    def is_correct(self):
        answer = self.quiz.check_answer("True")
        self.feedback(answer)

    def is_wrong(self):
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.screen.after(1000, self.get_next_question)
