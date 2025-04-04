import tkinter as tk
import webview  

class UserCommunity:
    def __init__(self):
        webview.create_window("Cybersecurity Community", "https://www.reddit.com/r/cybersecurity/?rdt=46985")
        webview.start()


if __name__ == "__main__":
    UserCommunity()


