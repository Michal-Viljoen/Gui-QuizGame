from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain ):
        self.score=0
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("QUIZZLER")
        self.window.config(pady=20,padx=10,bg=THEME_COLOR)

        self.label=Label()
        self.label.config(text=f"Score: {self.score} ",bg=THEME_COLOR,fg='white')
        self.label.grid(row=0,column=1)

        self.canvas=Canvas()
        self.canvas.config(width=300,height=250,bg='white',highlightthickness=0)
        self.question=self.canvas.create_text(150,125,text="Question", font=("Arial",20,"italic"),fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        right = PhotoImage(file="images/true.png")
        self.right_button=Button()
        self.right_button.config(image=right,highlightthickness=0,command=self.is_correct)
        self.right_button.grid(row=2,column=0)

        wrong = PhotoImage(file="images/false.png")
        self.False_button=Button()
        self.False_button.config(image=wrong,highlightthickness=0, command=self.is_wrong)
        self.False_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="All Done")
            self.right_button.config(state="disabled")
            self.False_button.config(state="disabled")


    def is_correct(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def is_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right==True:
            self.score +=1
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.score} ",bg=THEME_COLOR,fg='white')

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)
