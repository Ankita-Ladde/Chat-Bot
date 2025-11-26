import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
from PIL import Image, ImageTk
import customtkinter as ctk


# Setup Gemini API

genai.configure(api_key="AIzaSyAC6f2rfE-VLz2_bmdSHaMVirah0JlZ8cU")  # API key
model = genai.GenerativeModel("models/gemini-2.5-flash")

# AI Reply Function

def get_ai_reply(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Error: " + str(e)

#  Send Message

def send_message():
    user_msg = entry.get()

    if not user_msg.strip():
        return

    chat_window.insert(tk.END, "You: " + user_msg + "\n")
    entry.delete(0, tk.END)

    root.update()
    
    # AI Response
    bot_reply = get_ai_reply(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_window.yview(tk.END)


# GUI Setup

root = tk.Tk()
root.title("Gemini AI Chatbot")
root.geometry("520x750")    
root.configure(bg="#D6ECFF")

# IMAGE
img = Image.open("chatbot-avatar.png")
img = img.resize((150, 150))     
image = ImageTk.PhotoImage(img)

image_label = tk.Label(root, image=image, bg="#D6ECFF")
image_label.pack(pady=10)

chat_window = scrolledtext.ScrolledText(root, width=60, height=23, wrap=tk.WORD)
chat_window.pack(pady=(2 ,0))

# ENTRY + BUTTON
input_frame = tk.Frame(root, bg="#D6ECFF")
input_frame.pack(pady=15)

entry = tk.Entry(input_frame, width=40, font=("Arial", 12),             bg="#FFFFFF",
                 bd=0,                                 relief="flat",      
                 highlightthickness=0)
entry.grid(row=0, column=0, padx=5)

send_btn = ctk.CTkButton(
    input_frame,
    text="Send",
    command=send_message,
    width=90,
    height=30,
    corner_radius=20,   # rounded corners
    fg_color="#3A8CFF",
    hover_color="#5CA3FF",
    bg_color="#D6ECFF"
)
send_btn.grid(row=0, column=1, padx=10)

root.mainloop()
