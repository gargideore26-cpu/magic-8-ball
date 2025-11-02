import random
import tkinter as tk
from tkinter import messagebox

def shake_magic_8_ball():
    """
    Shakes the 8-Ball and returns a randomly selected fortune.
    """
    responses = [
        "It is certain.",
        "Yes, definitely.",
        "Without a doubt.",
        "Most likely.",
        "You may rely on it.",
        "Ask again later.",
        "Cannot predict now.",
        "Don't count on it.",
        "Very doubtful."
    ]

    return random.choice(responses)


class Magic8BallApp:
    def __init__(self, master):
        self.master = master
        master.title("Magic 8-Ball")
        master.geometry("400x250")  
        master.resizable(False, False) 

        
        self.question_label = tk.Label(master, text="Ask 8-Ball your question:", font=('Arial', 15))
        self.question_label.pack(pady=10)

        self.question_entry = tk.Entry(master, width=50, font=('Arial', 10))
        self.question_entry.pack(pady=5)
        
        
        self.question_entry.bind('<Return>', self.ask_question) 

        
        self.ask_button = tk.Button(master, text="Shake the 8-Ball", command=self.ask_question_click, 
                                    fg='black', font=('Arial',13, 'bold'))
        self.ask_button.pack(pady=20)

        
        self.answer_label = tk.Label(master, text="🔮Type your question and click the button.", 
                                      font=('Arial', 12, 'italic'), fg='white', wraplength=350)
        self.answer_label.pack(pady=10)

    def ask_question_click(self):
        """Method called when the button is clicked."""
        self.ask_question()

    def ask_question(self, event=None):
        """
        Handles the question logic, updates the GUI, and displays the answer.
        """
        question = self.question_entry.get().strip()

        if not question:
           
            messagebox.showwarning("Input Error", "Please enter a question!")
            return

       
        fortune = shake_magic_8_ball()

       
        self.answer_label.config(text=f"\n\n**{fortune}**", 
                                 font=('Arial', 14, 'bold'), fg="#11A41B") 
        
       
        self.question_entry.delete(0, tk.END)




if __name__ == "__main__":
    root = tk.Tk()  
    app = Magic8BallApp(root) 
    root.mainloop() 