# 📺 YouTube Comment Analyzer

This project is a simple web app that helps understand what people are saying in YouTube comments.  
Instead of manually reading hundreds of comments, the app automatically analyzes them and shows useful insights like questions, sentiment, and suggestions.

The app is built using Streamlit, so it runs in a browser and is very easy to use.

---

## ✨ What this project does

When you enter a YouTube video ID and click **Analyze**, the app performs the following steps:

### 1️⃣ Fetches YouTube comments
- Connects to the YouTube Data API
- Collects up to 100 top-level comments from a video

### 2️⃣ Detects questions in comments
- Uses OpenAI (GPT-3.5) to analyze comments
- Extracts only actual questions
- Ignores normal statements and irrelevant text

### 3️⃣ Analyzes sentiment
- Uses a Hugging Face NLP model (DistilBERT)
- Classifies comments as Positive or Negative
- Displays confidence scores and a summary chart

### 4️⃣ Classifies suggestions and feedback
- Categorizes comments into:
  - Suggestions
  - Feedback
  - Other

---

## 🧠 Why this project is useful
- Saves time by summarizing large comment sections
- Helps content creators understand audience mood
- Identifies common viewer questions and suggestions

---

## 🛠️ Technologies used
- Python
- Streamlit
- OpenAI GPT-3.5
- Hugging Face Transformers
- YouTube Data API v3
- Pandas

---

## ▶️ How to run the project

```bash
pip install -r requirements.txt
streamlit run app.py
