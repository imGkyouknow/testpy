import tkinter as tk
from tkinter import messagebox
import subprocess

class CustomTkinter:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Gesture & Speech Controlled YouTube Player")
        self.root.geometry("1920x1080+0+0")
        self.root.configure(bg="#f5f5f5")

        # Define custom fonts
        self.font_header = ("Helvetica", 26, "bold")
        self.font_section = ("Arial", 20)
        self.font_button = ("Arial", 16, "italic")
        self.font_footer = ("Roboto", 14)

        # Define custom colors
        self.colors = ["#ffd700", "#ff5733", "#ff33a6", "#33a6ff", "#33ff57", "#a633ff", "#ffa633", "#a6ff33", "#3366ff", "#66ff33"]

        # Header
        self.header_frame = tk.Frame(self.root, bg="#333")
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Control YouTube video via Speech and Gesture", font=self.font_header, bg="#333", fg="#ffd700")
        self.header_label.pack(pady=20)

        # Navigation
        self.nav_frame = tk.Frame(self.root, bg="#333")
        self.nav_frame.pack(fill="x")

        self.create_navigation_label("Home", 0)
        self.create_navigation_label("About", 1)
        self.create_navigation_label("Contact", 2)

        # Section
        self.section_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.section_frame.pack(expand=True)

        self.section_label = tk.Label(self.section_frame, text="Control YouTube videos using gestures and speech with our innovative application.", font=self.font_section, bg="#f5f5f5", fg="#333")
        self.section_label.pack(pady=20)

        self.btn_speech = tk.Button(self.section_frame, text="Use Speech", font=self.font_button, bg="green2", fg="grey2", command=self.open_speech_control)
        self.btn_speech.pack(side="left", padx=20)

        self.btn_gesture = tk.Button(self.section_frame, text="Use Gestures", font=self.font_button, bg="cyan2", fg="grey2", command=self.open_gesture_control)
        self.btn_gesture.pack(side="left", padx=20)

        # Footer
        self.footer_frame = tk.Frame(self.root, bg="#333")
        self.footer_frame.pack(side="bottom", fill="x")

        self.footer_label = tk.Label(self.footer_frame, text="© 2024 Gesture & Speech Controlled YouTube Player. All rights reserved.", font=self.font_footer, bg="#333", fg="#fff")
        self.footer_label.pack(pady=10)

        # Change color animation for header label
        self.change_color(self.header_label, self.colors, 0)

    def create_navigation_label(self, text, column):
        nav_label = tk.Label(self.nav_frame, text=text, fg="#fff", bg="#333", font=self.font_footer, cursor="hand2")
        nav_label.grid(row=0, column=column, padx=20)
        nav_label.bind("<Button-1>", lambda event, option=text: self.menu_click(option))

    def open_speech_control(self):
        subprocess.Popen(["python", "Speech_code.py"])

    def open_gesture_control(self):
        subprocess.Popen(["python", "Gesture_code.py"])

    def change_color(self, label, colors, index):
        label.config(fg=colors[index])
        index = (index + 1) % len(colors)
        label.after(500, self.change_color, label, colors, index)

    def menu_click(self, option):
        if option == "Home":
            messagebox.showinfo("Home", "You're already on the Home page!")
        elif option == "About":
            messagebox.showinfo("About", "This application is designed to control YouTube videos using gestures and speech.")
        elif option == "Contact":
            messagebox.showinfo("Contact", "For any inquiries, please email us at uppularakesh4359@gmail.com")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomTkinter(root)
    root.mainloop()
