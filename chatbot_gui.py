import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import json

# Load FAQ Data
with open("faq_data.json", "r") as file:
    faq = json.load(file)

# Send Message Function
def send_message():
    user_message = entry.get().strip().lower()

    if user_message == "":
        return

    chat_area.insert(tk.END, "👩 You: " + user_message + "\n")

    # Smart Responses
    if user_message in ["hello", "hi", "hey"]:
        bot_reply = "Hello Vishwa! Welcome to Smart AI Helpdesk Chatbot 😊"

    elif "time" in user_message:
        bot_reply = "⏰ Current Time: " + datetime.now().strftime("%H:%M:%S")

    elif "date" in user_message:
        bot_reply = "📅 Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    elif user_message in faq:
        bot_reply = faq[user_message]

    else:
        bot_reply = "🤖 Sorry, I don't understand that question."

    chat_area.insert(tk.END, "🤖 Bot: " + bot_reply + "\n\n")

    chat_area.see(tk.END)
    entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Smart AI Helpdesk Chatbot")
root.geometry("700x600")
root.configure(bg="#C03750")

# Title
title = tk.Label(
    root,
    text="🤖 Smart AI Helpdesk Chatbot",
    font=("Arial", 18, "bold"),
    bg="#C03750",
    fg="white"
)
title.pack(pady=10)

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    width=80,
    height=25,
    font=("Arial",11),
    bg="#C03750",
    fg="white",
    insertbackground="white"
)
chat_area.pack(padx=10, pady=10)

# Input Frame
frame = tk.Frame(root, bg="#C03750")
frame.pack(pady=10)

# Entry Box
entry = tk.Entry(
    frame,
    width=50,
    font=("Arial",12),
    bg="#2D2D2D",
    fg="white",
    insertbackground="white"
)
entry.pack(side=tk.LEFT, padx=5)

# Send Button
send_btn = tk.Button(
    frame,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=send_message
)
send_btn.pack(side=tk.LEFT)

# Enter Key Support
entry.bind("<Return>", lambda event: send_message())

# Welcome Message
chat_area.insert(
    tk.END,
    "🤖 Welcome to Smart AI Helpdesk Chatbot!\n"
    "Type hello, time, date, internship, department etc.\n\n"
)

root.mainloop()