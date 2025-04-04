import tkinter as tk
from tkinter import messagebox

# Quiz Questions and Answers based on levels
quiz_levels = {
    "Beginner": [
        {"question": "What does HTTPS stand for?", "options": ["Hyper Text Transfer Protocol Secure", "Hackers Target The Protocol Securely", "High Tech Transfer Secure", "Hyper Transfer Text Protocol"], "answer": "Hyper Text Transfer Protocol Secure"},
        {"question": "Which of these is a strong password?", "options": ["mypassword", "P@ssw0rd!", "123456", "qwerty"], "answer": "P@ssw0rd!"},
        {"question": "What should you do if you receive a suspicious email?", "options": ["Open it to check", "Click all links", "Ignore and report it", "Forward it to friends"], "answer": "Ignore and report it"}
    ],
    "Intermediate": [
        {"question": "What is two-factor authentication (2FA)?", "options": ["A single password login", "A security system requiring two different verifications", "A way to hack accounts", "An encryption method"], "answer": "A security system requiring two different verifications"},
        {"question": "Which is the safest way to browse the internet?", "options": ["Using a VPN", "Clicking on random links", "Entering personal data everywhere", "Ignoring security updates"], "answer": "Using a VPN"},
        {"question": "What type of attack is a phishing scam?", "options": ["Physical", "Social Engineering", "Brute Force", "DoS"], "answer": "Social Engineering"}
    ],
    "Advanced": [
    {
        "question": "What does the principle of least privilege imply in cybersecurity?",
        "options": [
            "Giving all users full access rights",
            "Denying access to all users by default",
            "Users only have the minimum access necessary to perform their job",
            "Allowing administrators to bypass security"
        ],
        "answer": "Users only have the minimum access necessary to perform their job"
    },
    {
        "question": "Which of the following attacks can exploit input fields to execute unintended commands on a server?",
        "options": ["Phishing", "XSS", "SQL Injection", "Brute Force"],
        "answer": "SQL Injection"
    },
    {
        "question": "In Public Key Infrastructure (PKI), what is the role of a Certificate Authority (CA)?",
        "options": [
            "Encrypting all network traffic",
            "Verifying the identity of entities and issuing digital certificates",
            "Storing all passwords in a system",
            "Preventing spam emails"
        ],
        "answer": "Verifying the identity of entities and issuing digital certificates"
    }
]

}

# Initializing variables
score = 0
current_question = 0
selected_level = ""
quiz_data = []

# Function to check answer
def check_answer(choice):
    global score, current_question
    if choice == quiz_data[current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question < len(quiz_data):
        load_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Your final score is: {score}/{len(quiz_data)}")
        quiz_root.destroy()

# Function to load questions
def load_question():
    question_label.config(text=quiz_data[current_question]["question"])
    for i, option in enumerate(quiz_data[current_question]["options"]):
        buttons[i].config(text=option, command=lambda o=option: check_answer(o))

# Function to start quiz
def start_quiz(level):
    global quiz_data, selected_level
    selected_level = level
    quiz_data = quiz_levels[level]
    for widget in quiz_root.winfo_children():
        widget.destroy()
    build_quiz_ui()
    load_question()

# Function to create quiz UI
def build_quiz_ui():
    global question_label, buttons
    title_label = tk.Label(quiz_root, text=f"🛡 CyberQuiz - {selected_level} Level", font=("Helvetica", 16, "bold"), fg="white", bg="#2C3E50")
    title_label.pack(pady=10)

    question_label = tk.Label(quiz_root, font=("Arial", 12), fg="white", bg="#2C3E50")
    question_label.pack(pady=5)

    buttons = []
    for _ in range(4):
        btn = tk.Button(quiz_root, font=("Arial", 12), bg="lightgray", width=100, height=2)
        btn.pack(pady=5)
        buttons.append(btn)

# Initial screen with level selection
def build_level_selection():
    title = tk.Label(quiz_root, text="🛡 Welcome to CyberQuiz", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
    title.pack(pady=20)

    subtitle = tk.Label(quiz_root, text="Select Difficulty Level", font=("Helvetica", 14), fg="white", bg="#2C3E50")
    subtitle.pack(pady=10)

    for level in ["Beginner", "Intermediate", "Advanced"]:
        tk.Button(quiz_root, text=level, font=("Arial", 12), bg="skyblue", width=20, height=2,
                  command=lambda l=level: start_quiz(l)).pack(pady=5)

# Quiz Window
quiz_root = tk.Tk()
quiz_root.title("CyberQuiz")
quiz_root.geometry("1000x450")
quiz_root.configure(bg="#2C3E50")

build_level_selection()
quiz_root.mainloop()
