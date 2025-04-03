import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PhishingTrapGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Phishing Trap Challenge")
        self.geometry("1000x900")
        self.configure(bg="white")

        self.images = ["images/img1.jpg", "images/img2.jpg", "images/img3.jpg"]
        self.correct_answers = ["Phishing Email", "Genuine Email", "Phishing Email"]
        self.current_index = 0
        self.score = 0

        self.show_checklist()

    def show_checklist(self):
        """Displays the phishing checklist before the game starts."""
        checklist_text = """Quick Checklist: Signs of a Phishing Email!!
        
A) Examine the sender:
1. Does the email come from a public domain (e.g. @gmail.com) while claiming to be from a company?
2. Does the sender’s domain contain misspellings (e.g. “paypl” instead of “PayPal”)?
3. Does the sender’s address differ from the organisation’s usual email format?

B) Review content & style:
1. Does the message contain grammatical errors or unusual phrasing?
2. Does the email create artificial urgency (e.g. “Act now”, “Account suspension imminent”)?
3. Does the writing style differ from the organisation’s normal tone?

C) Check links & attachments:
1. Does the hover-over link URL differ from the displayed text?
2. Does the email ask you to download unexpected files?
3. Does the message include generic action buttons (e.g. “Click Here”, “Log in now”)?

D) Look for security red flags:
1. Does the email request sensitive information (e.g. passwords, account details)?
2. Does the message pressure you to bypass standard security procedures?
3. Does it threaten negative consequences if you don’t act immediately?
"""

        self.checklist_frame = tk.Frame(self, bg="white", padx=10, pady=10)
        self.checklist_frame.pack(expand=True, fill="both")

        checklist_label = tk.Label(self.checklist_frame, text=checklist_text, font=("Arial", 11), bg="white", justify="left", wraplength=550)
        checklist_label.pack(pady=10)

        proceed_button = tk.Button(self.checklist_frame, text="Proceed to Game", font=("Arial", 12, "bold"), bg="green", fg="white",
                                   command=self.start_game, padx=10, pady=5)
        proceed_button.pack(pady=10)

    def start_game(self):
        """Starts the phishing identification game."""
        self.checklist_frame.destroy()
        self.display_email()

    def display_email(self):
        """Displays email images for users to identify phishing or genuine emails."""
        if self.current_index < len(self.images):
            img_path = self.images[self.current_index]

            # Load and display the image
            self.image_frame = tk.Frame(self, bg="white")
            self.image_frame.pack(expand=True, fill="both")

            image = Image.open(img_path)
            image = image.resize((500,550))  # Resize image
            img_tk = ImageTk.PhotoImage(image)

            img_label = tk.Label(self.image_frame, image=img_tk, bg="white")
            img_label.image = img_tk  # Keep a reference
            img_label.pack(pady=10)

            question_label = tk.Label(self.image_frame, text="Is this email Phishing or Genuine?", font=("Arial", 13, "bold"), bg="white")
            question_label.pack(pady=5)

            # Buttons
            phishing_btn = tk.Button(self.image_frame, text="Phishing Email", font=("Arial", 12, "bold"), bg="red", fg="white",
                                     command=lambda: self.check_answer("Phishing Email"))
            phishing_btn.pack(side="left", padx=20, pady=10, expand=True)

            genuine_btn = tk.Button(self.image_frame, text="Genuine Email", font=("Arial", 12, "bold"), bg="blue", fg="white",
                                    command=lambda: self.check_answer("Genuine Email"))
            genuine_btn.pack(side="right", padx=20, pady=10, expand=True)
        else:
            self.show_results()

    def check_answer(self, selected_answer):
        """Checks if the user's answer is correct."""
        correct = self.correct_answers[self.current_index]

        if selected_answer == correct:
            self.score += 1
        else:
            messagebox.showwarning("Incorrect!", f"Oops! The correct answer was: {correct}")

        self.current_index += 1
        self.image_frame.destroy()  # Remove the previous image
        self.display_email()  # Show next image

    def show_results(self):
        """Displays the final score at the end of the game."""
        self.image_frame.destroy()

        result_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        result_frame.pack(expand=True, fill="both")

        result_text = f"Game Over! 🎯\nYour final score: {self.score}/{len(self.images)}"
        result_label = tk.Label(result_frame, text=result_text, font=("Arial", 14, "bold"), bg="white")
        result_label.pack(pady=10)

        restart_button = tk.Button(result_frame, text="🔄Play Again", font=("Arial", 12, "bold"), bg="orange", fg="white",
                                   command=self.restart_game)
        restart_button.pack(pady=5)

        exit_button = tk.Button(result_frame, text="❌ Exit", font=("Arial", 12, "bold"), bg="red", fg="white",
                                command=self.quit)
        exit_button.pack(pady=5)

    def restart_game(self):
        """Restarts the game from the beginning."""
        self.current_index = 0
        self.score = 0
        self.checklist_frame.destroy()
        self.start_game()

if __name__ == "__main__":
    app = PhishingTrapGame()
    app.mainloop()