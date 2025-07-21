# 🚀 NexDraft-AI-Blog-Generator

**NexDraft** is a lightweight, AI-powered web app that generates clean, structured blog posts from a single topic prompt. It uses Google’s Gemini 1.5 Flash model (via LangChain) to run a three-stage pipeline:

1. Research summary (brief, focused points)
2. Blog draft (intro, body, conclusion)
3. Polish pass (grammar, clarity, concision)

Built with Flask, styled for a modern dark UI, and includes a loading spinner and downloadable blog output. 

---

## ✨ Features

- Enter any topic — get a full blog post in seconds.
- Three-step AI flow: research → write → review (token-controlled prompts).
- Powered by Gemini 1.5 Flash (fast + free-tier friendly).
- Clean dark theme UI with centered layout.
- Real-time spinner while content generates.
- Displays final topic with AI-generated content.
- Download blog as .txt.
- API key loaded securely from .env.

---

## 📸 Screenshots

### 1. Interface UI — shows the homepage and form
<img width="1122" height="1042" alt="image" src="https://github.com/user-attachments/assets/c45c4a7f-bdd8-48e0-a240-4504e88417b6" />

### 2. Generated Blog Output — displays a completed blog with the topic and download button

<img width="1135" height="1042" alt="image" src="https://github.com/user-attachments/assets/73c6acb6-4795-43b0-98ce-9739e9da7e84" />

---

## 📁 Project Structure

NexDraft-AI-Blog-Generator\
- app.py ( Flask app setup and routes )
- agents_logic.py ( LangChain pipeline (research → write → polish) )
-  templates/
    - index.html ( UI: form, spinner, output, download )
-  static/
    - style.css ( Dark theme + animations )
- requirements.txt 
- .env (API key )
- .gitignore ( Files/folders to ignore in Git )
- README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

- git clone https://github.com/your-username/NexDraft-AI-Blog-Generator.git
- cd NexDraft-AI-Blog-Generator

### 2. Create Virtual Environment (optional but recommended)

This or use anaconda prompt
- python -m venv venv
- source venv/bin/activate

Or use Anaconda:
- conda create -n nexdraft python=3.10 -y
- conda activate nexdraft

### 3. Install Requirements

pip install -r requirements.txt

### 4. Setup Gemini API Key

Create a .env file in the root directory:
- GEMINI_API_KEY=your_google_gemini_api_key

### 5. Running the App

python app.py

Then open your browser at:
- http://127.0.0.1:5000

---

## 🧠 How to Use

1. Enter a topic (e.g., Benefits of mindfulness for students).
2. Click Generate Blog.
3. Watch the spinner while the AI builds your post.
4. Review the generated blog under Generated Blog Post.
5. Click Download Blog to save a .txt file.

---

“From idea to publish-ready blog in seconds.”
