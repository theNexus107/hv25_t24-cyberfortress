import tkinter as tk
from tkinter import messagebox

# Quick Checklist Window
def show_checklist():
    checklist_root = tk.Toplevel()
    checklist_root.title("Quick Checklist: How to create strong passwords!!")
    checklist_root.geometry("1000x400")
    checklist_root.configure(bg="#1E1E1E")
    
    checklist_text = """
    A) At least 12 characters long but 14 or more is better.
    
    B) A combination of uppercase letters, lowercase letters, numbers, and symbols.
    
    C) Not a word that can be found in a dictionary or the name of a person, character, product, or organization.
    
    D) Significantly different from your previous passwords.
    
    E) Easy for you to remember but difficult for others to guess. Consider using a memorable phrase like \"6MonkeysRLooking^\".
    """
    
    checklist_label = tk.Label(checklist_root, text=checklist_text, font=("Arial", 12), fg="white", bg="#1E1E1E", justify="left")
    checklist_label.pack(pady=20, padx=20)
    
    proceed_button = tk.Button(checklist_root, text="Proceed", font=("Arial", 12), bg="lightgray", width=20, command=lambda: [checklist_root.destroy(), start_game()])
    proceed_button.pack(pady=20)

# Password Strength Questions and Answers
password_data = [
    {"question": "Which is a strong password?", "options": ["password123", "qwerty", "Str0ng@Pass1", "123456"], "answer": "Str0ng@Pass1"},
    {"question": "Which factor makes a password strong?", "options": ["Length", "Special characters", "Combination of letters, numbers, and symbols", "All of the above"], "answer": "All of the above"},
    {"question": "Which password is the weakest?", "options": ["MyBirthday2023", "P@ssw0rd!", "h4cker$ecure", "abcdefg"], "answer": "abcdefg"},
    {"question": "How often should you change your password?", "options": ["Every week", "Only when hacked", "Regularly, every few months", "Never"], "answer": "Regularly, every few months"},
    {"question": "Which method is safest for storing passwords?", "options": ["Writing in a notebook", "Saving in browser", "Using a password manager", "Memorizing only"], "answer": "Using a password manager"}
]

score = 0
curntqes = 0

def checkpasswrd(ch):
    global score, curntqes
    if ch == password_data[curntqes]["answer"]:
        score += 1
    curntqes += 1
    if curntqes < len(password_data):
        loadques()
    else:
        messagebox.showinfo("Game Over", f"Your final score is: {score}/{len(password_data)}")

def loadques():
    question_label.config(text=password_data[curntqes]["question"])
    for i, option in enumerate(password_data[curntqes]["options"]):
        buttons[i].config(text=option, command=lambda o=option: checkpasswrd(o))

def start_game():
    global question_label, buttons, password_root
    
    password_root = tk.Tk()
    password_root.title("Password Strength Game")
    password_root.geometry("500x400")
    password_root.configure(bg="#1E1E1E")
    
    title_label = tk.Label(password_root, text="🔐 Password Strength Game", font=("Helvetica", 16, "bold"), fg="white", bg="#1E1E1E")
    title_label.pack(pady=10)
    
    question_label = tk.Label(password_root, font=("Arial", 12), fg="white", bg="#1E1E1E")
    question_label.pack(pady=5)
    
    buttons = []
    for _ in range(4):
        btn = tk.Button(password_root, font=("Arial", 12), bg="lightgray", width=40, height=2)
        btn.pack(pady=5)
        buttons.append(btn)
    
    loadques()
    password_root.mainloop()

# Start with the checklist window
root = tk.Tk()
root.withdraw()  # Hide the main root window
show_checklist()
root.mainloop()