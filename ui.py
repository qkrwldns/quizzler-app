import tkinter
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.label = Label(text="Score:0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.label.grid(column=1, row=0)

        self.canvas_main = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas_main.grid(column=0, row=1, columnspan=2, pady=50)

        self.text = self.canvas_main.create_text(150, 125,
                                                 text="Texts",
                                                 font=("Arial", 20, "italic"),
                                                 fill=THEME_COLOR,
                                                 width= 280
                                                 )

        button_ok_img = PhotoImage(file="./images/true.png")
        self.button_ok = Button(self.window,
                                image=button_ok_img,
                                bd=0,
                                highlightthickness=0,
                                command=lambda: self.check("True"))
        self.button_ok.grid(column=0, row=2)

        button_no_img = PhotoImage(file="./images/false.png")
        self.button_no = Button(self.window,
                                image=button_no_img,
                                bd=0,
                                highlightthickness=0,
                                command=lambda: self.check("False"))
        self.button_no.grid(column=1, row=2)
        self.get_next_q()
        self.window.mainloop()


    def get_next_q(self):
        q_text = self.quiz.next_question()
        self.canvas_main.itemconfig(self.text,text=q_text)

    def check(self, user_answer):
        correct_answer = self.quiz.current_question.answer
        if user_answer == correct_answer:
            self.quiz.score += 1
            self.label["text"] = f"Score:{self.quiz.score}"
            self.canvas_main.configure(bg="Green")
        else:
            self.canvas_main.configure(bg="red")
        self.window.after(500, lambda: self.canvas_main.configure(bg="white"))
        if self.done():
            self.done()

    def done(self):
        if self.quiz.still_has_questions():
            self.get_next_q()
        else:
            self.canvas_main.itemconfig(self.text,text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.button_no.config(state='disabled')
            self.button_ok.config(state='disabled')
            #  self.button_no.configure(command='')
            #  self.button_ok.configure(command='') <<<< 이것도 가능