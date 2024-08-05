import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("425x250")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')

        self.target = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess the number between 1 and 100:", font=('Arial', 12), bg='#f0f0f0')
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=('Arial', 12), justify='center', bd=2)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Submit", command=self.check_guess, font=('Arial', 12), bg='#4caf50', fg='white', activebackground='#45a049')
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="", font=('Arial', 12), bg='#f0f0f0')
        self.result.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.target:
                self.result.config(text="Too low! Try again.", fg='#ff5722')
            elif guess > self.target:
                self.result.config(text="Too high! Try again.", fg='#ff5722')
            else:
                self.result.config(text=f"Congratulations! You've guessed the number in {self.attempts} attempts.", fg='#4caf50')
                self.button.config(state=tk.DISABLED)
        except ValueError:
            self.result.config(text="Please enter a valid number.", fg='#f44336')

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
