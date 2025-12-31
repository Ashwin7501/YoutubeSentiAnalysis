📺 YouTube Comment Analyzer

This project is a simple web app that helps understand what people are saying in YouTube comments.
Instead of manually reading hundreds of comments, the app automatically analyzes them and shows useful insights like questions, sentiment, and suggestions.

The app is built using Streamlit, so it runs in a browser and is very easy to use.

✨ What this project does

When you enter a YouTube video ID and click Analyze, the app does the following:

🔹 1. Fetches YouTube comments

Connects to the YouTube Data API

Collects up to 100 top-level comments from a video

🔹 2. Detects questions in comments

Uses OpenAI (GPT-3.5) to scan all comments

Extracts only the comments that are actual questions

Ignores normal statements, usernames, and extra text

Displays all detected questions in one place

👉 This is useful to quickly see what viewers are asking.

🔹 3. Analyzes sentiment

Uses a Hugging Face NLP model (DistilBERT)

Classifies each comment as:

Positive

Negative

Also shows a confidence score

Displays a summary chart to understand overall audience mood

🔹 4. Classifies suggestions and feedback

Uses a transformer-based text classification model

Categorizes comments into:

Suggestions

Feedback

Other

Helps identify improvement ideas from viewers

🧠 Why this project is useful

Saves time by summarizing large comment sections

Helps content creators understand:

What viewers are asking

Whether feedback is positive or negative

What suggestions viewers are giving

Can be used for:

YouTube content analysis

Audience feedback analysis

NLP learning projects

🛠️ Technologies used

Python

Streamlit – Web interface

YouTube Data API v3 – Fetch comments

OpenAI GPT-3.5 – Question detection

Hugging Face Transformers

Sentiment analysis

Comment classification

Pandas – Data handling

▶️ How to run the project
pip install -r requirements.txt
streamlit run app.py


Set your OpenAI key as an environment variable:

export OPENAI_API_KEY="your_api_key"

🔒 Note on API keys

For security reasons:

API keys should not be hard-coded

Always use environment variables

Do not push keys to GitHub

🚀 Future improvements

Support for more than 100 comments (pagination)

Multi-language comment analysis

Question categorization (why / how / what)

Deployment to Streamlit Cloud

🧾 One-line project summary (for GitHub)

A Streamlit web app that analyzes YouTube comments to detect questions, analyze sentiment, and classify viewer feedback using AI.
