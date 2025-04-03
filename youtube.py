import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import requests
from io import BytesIO

class YouTubeLinksApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("CyberTube")
        self.geometry("600x400")
        self.configure(bg="white")

        tk.Label(self, text="🎥 CyberTube", font=("Arial", 16, "bold"), bg="white", fg="black").pack(pady=10)

        # YouTube Video List (Title, Link)
        self.videos = [
            ("What is Cybersecurity?", "https://youtu.be/ooJSgsB5fIE?si=w--bIKzCTrRJnN1N"),
            ("Common Cybersecurity Threats!", "https://youtu.be/Dk-ZqQ-bfy4?si=UgeiTC4AxsmPtWUz"),
            ("Why Learn Cybersecurity?", "https://youtu.be/ZLyFt6BdxD4?si=WX2FU_rB8yK6x8vo"),
        ]

        self.display_videos()

    def get_thumbnail(self, video_url):
        """Fetch the YouTube thumbnail using video ID"""
        try:
            video_id = video_url.split("youtu.be/")[-1].split("?")[0]  # Extract video ID
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

            response = requests.get(thumbnail_url)
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((100, 75))  # Resize image
            return ImageTk.PhotoImage(img_data)
        except Exception as e:
            print(f"Error fetching thumbnail: {e}")
            return None

    def display_videos(self):
        for title, link in self.videos:
            frame = tk.Frame(self, bg="white", relief="solid", bd=1)
            frame.pack(pady=5, padx=10, fill="x")

            # Fetch and display thumbnail
            thumbnail = self.get_thumbnail(link)
            if thumbnail:
                img_label = tk.Label(frame, image=thumbnail, cursor="hand2", bg="white")
                img_label.image = thumbnail  # Keep a reference
                img_label.pack(side="left", padx=10)
                img_label.bind("<Button-1>", lambda e, url=link: self.open_link(url))

            # Video Title (Clickable)
            text_label = tk.Label(frame, text=title, fg="blue", font=("Arial", 12, "underline"), bg="white", cursor="hand2", wraplength=400, justify="left")
            text_label.pack(side="left", padx=10)
            text_label.bind("<Button-1>", lambda e, url=link: self.open_link(url))

    def open_link(self, url):
        """Opens the YouTube video in a web browser"""
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = YouTubeLinksApp()
    app.mainloop()
