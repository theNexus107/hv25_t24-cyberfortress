import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Story Scenes
game_scenes = [
    {
        "image": "images/image1.jpg",
        "text": "The Suspicious Email\nAn email from 'CEO@techshieldsupport.com' with the subject: 'URGENT! Update Your Credentials!'\n\nAs you check your inbox, you notice an email urging all employees to reset their passwords immediately. Something feels off.",
        "choices": [
            ("Click the link and update your password", False, "The hacker gains access—GAME OVER!"),
            ("Report the email to IT security", True, "Good job! The email is a phishing attempt."),
            ("Ignore the email and continue working", None, "It might still trick someone else!")
        ]
    },
    {
        "image": "images/image2.jpg",
        "text": "The USB Trap\nA mysterious USB labeled 'Project X - Confidential' is found near your desk.\n\nA co-worker hands you a USB drive, saying they found it in the office parking lot.",
        "choices": [
            ("Plug it into your work computer to check its contents", False, "Malware infects the system—GAME OVER!"),
            ("Take it to IT for a malware scan", True, "Smart move! IT detects a Trojan virus inside."),
            ("Throw it away", None, "Someone else might plug it in!")
        ]
    },
    {
        "image": "images/image3.jpg",
        "text": "Firewall Breach\nThe security dashboard shows multiple unauthorized login attempts.\n\nAn alert pops up—someone is trying to force their way into the company network.",
        "choices": [
            ("Disable the firewall to investigate", False, "The hacker gains access—GAME OVER!"),
            ("Notify the IT team and block suspicious IPs", True, "Great choice! You slow down the hacker."),
            ("Ignore the alert; IT will handle it", None, "Delays could be dangerous!")
        ]
    },
    {
        "image": "images/image4.jpg",
        "text": "The CEO’s Call\nYour phone rings—it’s the CEO asking for a password reset.\n\nYour CEO, or so it seems, calls you in a hurry, demanding immediate access to the system.",
        "choices": [
            ("Reset the password and send it via email", False, "It was a scam call—GAME OVER!"),
            ("Verify the request through official channels", True, "Good thinking! The CEO had no idea about this call."),
            ("Ignore the request completely", None, "Better safe than sorry, but verification is best!")
        ]
    }
]

class StoryGame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cybersecurity Story Mode")
        self.geometry("700x800")
        self.configure(bg="beige")

        self.score = 0
        self.current_scene = 0
        self.img_tk = None  # Store image reference

        self.story_label = tk.Label(self, text="Story Overview:\nYou are Alex, a cybersecurity analyst at TechShield Corp.\nToday, you receive an urgent alert—your company is under attack! Your mission is to stop the hacker.", font=("Arial", 14), wraplength=650, justify="left", bg="white")
        self.story_label.pack(pady=20)

        self.proceed_button = tk.Button(self, text="Proceed", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.start_game)
        self.proceed_button.pack(pady=10)
    
    def start_game(self):
        self.proceed_button.destroy()
        self.load_scene()
    
    def load_scene(self):
        if self.current_scene >= len(game_scenes):
            self.show_final_result()
            return
        
        scene = game_scenes[self.current_scene]
        
        # Check if the image exists
        if os.path.exists(scene["image"]):
            img = Image.open(scene["image"]).resize((400, 350))
            self.img_tk = ImageTk.PhotoImage(img)
        else:
            self.img_tk = None

        # Display Image
        if self.img_tk:
            self.img_label = tk.Label(self, image=self.img_tk, bg="beige")
        else:
            self.img_label = tk.Label(self, text="(Image not found)", font=("Arial", 12, "bold"), bg="beige")

        self.img_label.pack()

        # Display Text
        self.story_text = tk.Label(self, text=scene["text"], font=("Arial", 12), wraplength=650, justify="left", bg="white")
        self.story_text.pack(pady=10)

        # Display Choices
        for choice_text, is_correct, feedback in scene["choices"]:
            btn = tk.Button(self, text=choice_text, font=("Arial", 12), width=50, command=lambda c=is_correct, f=feedback: self.process_choice(c, f))
            btn.pack(pady=5)
    
    def process_choice(self, is_correct, feedback):
        if is_correct is False:
            messagebox.showerror("Game Over", feedback)
            self.destroy()
        elif is_correct is True:
            self.score += 1
            messagebox.showinfo("Success", feedback)
        else:
            messagebox.showwarning("Warning", feedback)

        # Move to next scene
        self.current_scene += 1
        self.clear_scene()
        self.load_scene()
    
    def clear_scene(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def show_final_result(self):
        self.clear_scene()
        final_message = "✅ Mission Accomplished!\n Level 1 Completed !!" if self.score == len(game_scenes) else "❌Mission Failed!! \n The hacker wins. Try again!"
        result_label = tk.Label(self, text=final_message, font=("Arial", 14, "bold"), bg="white")
        result_label.pack(pady=20)

if __name__ == "__main__":
    app = tk.Tk()
    app.withdraw()  # Hide main Tk window
    StoryGame(app)
    app.mainloop()