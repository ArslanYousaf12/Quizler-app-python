from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question text", fill=THEME_COLOR, font=("arial", 20 , "italic"))
        self.canvas.grid(row=1, column=0,columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_answer_true)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_answer_false)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        
        
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You reached the End of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def is_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def is_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right:bool):
        if is_right:
            self.green_color()
            self.window.after(1000, self.get_next_question)
        else:
            self.red_color()
            self.window.after(1000, self.get_next_question)
           
            
            
    
    def green_color(self):
        self.canvas.config(bg="Green")
    def red_color(self):
        self.canvas.config(bg="Red")
        
        
        
        
            
