import tkinter as tk
import subprocess
from story import StoryGame  
from news import NewsFeed  
from youtube import YouTubeLinksApp 
from usercommunity import UserCommunity

def open_phishing_game():
    subprocess.Popen(["python", "phishing.py"])

def open_story_game():
    StoryGame()  # Open Cybersecurity Story Mode inside main window
    
def open_youtube():
    YouTubeLinksApp()
    
def open_news():
    NewsFeed()

def open_password_game():
    subprocess.Popen(["python", "password.py"])

def open_quiz_game():
    subprocess.Popen(["python", "quiz.py"])

def open_community():
    community_window = UserCommunity()
    community_window.mainloop()


# Main Window
root = tk.Tk()
root.title("Cybersecurity Awareness App")
root.geometry("500x600")
root.configure(bg="LemonChiffon2")

title_label = tk.Label(root, text="Cybersecurity Awareness", font=("Helvetica", 18, "bold"), fg="brown4", bg="beige")
title_label.pack(pady=20)

button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "height": 2,
    "bd": 3,
    "relief": "raised"
}

def on_enter(e):
    e.widget.config(bg="light goldenrod", fg="white")

def on_leave(e):
    e.widget.config(bg="light goldenrod", fg="black")

buttons = [
    ("📚 Cybersecurity Story Mode", open_story_game),
    ("🍣 Phishing Trap Challenge", open_phishing_game),
    ("🎥 CyberTube", open_youtube),
    ("📰 CyberNews", open_news),
    ("🔐 Password Strength Game", open_password_game),
    ("⍰ Cyber Quiz", open_quiz_game),
    ("👥User Community",open_community)
    
]

for text, command in buttons:
    btn = tk.Button(root, text=text, bg="light goldenrod", **button_style, command=command)
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
