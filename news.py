import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import requests
from bs4 import BeautifulSoup
from io import BytesIO

class NewsFeed(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("CyberNews")
        self.geometry("650x500")
        self.configure(bg="white")

        tk.Label(self, text="📰 CyberNews", font=("Arial", 18, "bold"), fg="black", bg="white").pack(pady=10)

        # News articles (Title, URL)
        self.news_data = [
            ("BlackLock Ransomware Exposed", "https://thehackernews.com/2025/03/blacklock-ransomware-exposed-after.html?m=1"),
            ("Govt Strengthens Cybersecurity", "https://www.constructionworld.in/policy-updates-and-economic-news/government-strengthens-cybersecurity-measures-to-protect-critical-infrastructure-and-private-data/71077"),
            ("ClickFix Captcha Technique", "https://cybersecuritynews.com/clickfix-captcha-a-creative-technique/amp/")
        ]

        self.display_news()

    def fetch_thumbnail(self, url):
        """Fetches the thumbnail image from the news article using Open Graph meta tags."""
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            og_image = soup.find("meta", property="og:image")

            if og_image and og_image["content"]:
                return og_image["content"]
        except Exception as e:
            print(f"Error fetching thumbnail: {e}")

        # Default fallback image if no thumbnail is found
        return "https://via.placeholder.com/100x100.png?text=No+Image"

    def display_news(self):
        """Displays all news articles with images, titles, and clickable links."""
        for title, link in self.news_data:
            frame = tk.Frame(self, bg="white", relief="solid", bd=2)
            frame.pack(pady=10, padx=10, fill="x")

            img_url = self.fetch_thumbnail(link)

            try:
                # Load image from URL
                response = requests.get(img_url)
                img_data = Image.open(BytesIO(response.content))
                img_data = img_data.resize((80, 80))  # Resize image
                img = ImageTk.PhotoImage(img_data)

                # Image Label (Clickable)
                img_label = tk.Label(frame, image=img, cursor="hand2", bg="white")
                img_label.image = img  # Keep a reference
                img_label.pack(side="left", padx=10)
                img_label.bind("<Button-1>", lambda e, url=link: self.open_link(url))

            except Exception as e:
                print(f"Error loading image: {e}")

            # Text Label (Title - Clickable)
            text_label = tk.Label(frame, text=title, fg="blue", font=("Arial", 12, "underline"), bg="white", cursor="hand2", wraplength=400, justify="left")
            text_label.pack(side="left", padx=10, fill="x")
            text_label.bind("<Button-1>", lambda e, url=link: self.open_link(url))

    def open_link(self, url):
        """Opens the news link in a web browser."""
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = NewsFeed()
    app.mainloop()
