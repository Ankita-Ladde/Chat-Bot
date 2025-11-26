# Chat-Bot
Python AI Chatbot project (Tkinter + Gemini)
# 🧠 AI Chatbot (Python + Tkinter + Google Gemini)

This project is a **desktop AI chatbot application** built using **Python**, **Tkinter/CustomTkinter**, and **Google Gemini API**.
It provides a clean, modern UI with rounded elements, transparent backgrounds, and smooth user interaction.


## 🚀 Features

### **✨ Modern GUI**

* Clean chat window layout
* Customizable colors (sky-blue theme)
* White rounded input box
* Stylish send button
* Optional background image support

### **🤖 AI-Powered Conversations**

* Uses **Google Gemini API** to generate intelligent responses
* Handles general questions, conversations, and assistance
* Real-time communication with typing simulation

### **🖼️ UI Enhancements**

* Remove unwanted backgrounds around widgets
* Floating-style input box
* Rounded buttons (if using CustomTkinter)
* Smooth layout spacing

### **📦 Technology Stack**

| Component                   | Used For                                 |
| --------------------------- | ---------------------------------------- |
| **Python 3**                | Main application                         |
| **Tkinter / CustomTkinter** | Graphical User Interface                 |
| **Pillow (PIL)**            | Image loading (if background image used) |
| **Google Gemini API**       | AI text generation                       |

---

## 📁 Project Structure

```
project/
│── chatbot.py       # Main application file
│── assets/          # Background images (optional)
│── README.md        # Project documentation
│── requirements.txt # Dependencies
```

---

## 🔧 Setup & Installation

### 1️⃣ Install dependencies

```bash
pip install google-generativeai customtkinter pillow
```

### 2️⃣ Add your Gemini API key

Inside `chatbot.py`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## ▶️ Run the Application

```bash
python chatbot.py
```

---

## 📝 How It Works

1. The user types a message in the **white input box**.
2. The message appears in the chat window.
3. It is sent to **Google Gemini** for processing.
4. The AI response is displayed in real time.

---

## 🎯 Goals of This Project

* Build a lightweight and beautiful desktop chatbot
* Showcase how Tkinter and AI can work together
* Provide an easy template for beginners to create AI apps

---

## 📌 Future Improvements (Optional)

* Voice input & output
* Chat history saving
* Dark mode
* Using richer UI with CTkScrollableFrame
* Model switching (Gemini Flash, Pro, etc.)

