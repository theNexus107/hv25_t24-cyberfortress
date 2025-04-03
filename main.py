import tkinter as tk
import subprocess
from story import StoryGame  

def open_phishing_game():
    subprocess.Popen(["python", "phishing.py"])

def open_story_game():
    StoryGame()

# Main Window
root = tk.Tk()
root.title("Cybersecurity Awareness App")
root.geometry("500x600")
root.configure(bg="dark cyan")

title_label = tk.Label(root, text="Cybersecurity Awareness", font=("Helvetica", 18, "bold"), fg="white", bg="#121212")
title_label.pack(pady=20)

button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "height": 2,
    "bd": 3,
    "relief": "raised"
}

def on_enter(e):
    e.widget.config(bg="#1E90FF", fg="white")

def on_leave(e):
    e.widget.config(bg="lightgray", fg="black")

buttons = [
    ("📚 Cybersecurity Story Mode", open_story_game),
    ("🍣 Phishing Trap Challenge", open_phishing_game),
]

for text, command in buttons:
    btn = tk.Button(root, text=text, bg="lightgray", **button_style, command=command)
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()