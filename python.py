# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd

# # Load the sentiment analysis model
# @st.cache_resource
# def load_model():
#     return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# sentiment_pipeline = load_model()

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
    
#     comments = []
    
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
    
#     return comments

# # Function to perform sentiment analysis
# def analyze_sentiment(comments):
#     if len(comments) == 0:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
    
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")
    
#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment Analysis")

#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")

#                     st.dataframe(sentiment_data)  # Make the DataFrame scrollable vertically

#                     # Display summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)
# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd

# # Load the sentiment analysis model
# @st.cache_resource
# def load_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# # Load the custom suggestion model
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         # Replace with your actual Hugging Face model
#         return pipeline("text-classification", model="distilbert-base-uncased")  
#     except Exception as e:
#         st.error(f"Error loading suggestion model: {e}")
#         return None

# sentiment_pipeline = load_model()
# suggestion_pipeline = load_suggestion_model()

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to perform sentiment analysis
# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']
#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment and Suggestion Analysis")

#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)  # Scrollable DataFrame

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()
# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd

# # Load the sentiment analysis model
# @st.cache_resource
# def load_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# # Load the custom suggestion model
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         # Replace with your fine-tuned model for better classification
#         return pipeline("text-classification", model="distilbert-base-uncased")
#     except Exception as e:
#         st.error(f"Error loading suggestion model: {e}")
#         return None

# sentiment_pipeline = load_model()
# suggestion_pipeline = load_suggestion_model()

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to perform sentiment analysis
# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']

#             # Map the labels to meaningful names
#             if suggestion_type == "LABEL_0":
#                 suggestion_type = "Suggestion"
#             elif suggestion_type == "LABEL_1":
#                 suggestion_type = "Feedback"
#             else:
#                 suggestion_type = "Other"

#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment Analysis")

#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)  # Scrollable DataFrame

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()

# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd
# import requests

# # Hugging Face API details for the Mistral model
# HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
# HF_API_TOKEN = "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"  # Replace with your Hugging Face API key

# # Function to query the Hugging Face API
# def query_huggingface_api(payload):
#     headers = {
#         "Authorization": f"Bearer {HF_API_TOKEN}",
#         "Content-Type": "application/json",
#     }
#     response = requests.post(HF_API_URL, headers=headers, json={"inputs": payload})
#     if response.status_code != 200:
#         raise Exception(f"API Error: {response.status_code}, {response.text}")
#     try:
#         response_data = response.json()
#         return response_data
#     except Exception as e:
#         st.error(f"Error parsing API response: {e}")
#         raise

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to detect questions in comments using the Mistral model via API
# def detect_questions_via_api(comments):
#     if not comments:
#         st.warning("No comments available for question detection.")
#         return pd.DataFrame(columns=['Comment', 'Is Question'])

#     questions = []
#     for comment in comments:
#         try:
#             result = query_huggingface_api(comment)
#             is_question = "Yes" if "Question" in result[0].get("label", "") else "No"
#             questions.append((comment, is_question))
#         except KeyError as e:
#             st.error(f"Key error in response: {e}")
#         except Exception as e:
#             st.error(f"Error detecting questions via API: {e}")

#     return pd.DataFrame(questions, columns=['Comment', 'Is Question'])

# # Function to perform sentiment analysis
# @st.cache_resource
# def load_sentiment_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# sentiment_pipeline = load_sentiment_model()

# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         return pipeline("text-classification", model="distilbert-base-uncased")
#     except Exception as e:
#         st.error(f"Error loading suggestion classification model: {e}")
#         return None

# suggestion_pipeline = load_suggestion_model()

# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']

#             # Map the labels to meaningful names
#             if suggestion_type == "LABEL_0":
#                 suggestion_type = "Suggestion"
#             elif suggestion_type == "LABEL_1":
#                 suggestion_type = "Feedback"
#             else:
#                 suggestion_type = "Other"

#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment and Question Detection")

#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Detecting questions..."):
#                     question_data = detect_questions_via_api(comments)

#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)  # Scrollable DataFrame

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

#                 if not question_data.empty:
#                     st.subheader("Question Detection")
#                     st.dataframe(question_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()

###Only question part
# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd
# import requests

# # Hugging Face API details for the Mistral model
# HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
# HF_API_TOKEN = "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"  # Replace with your Hugging Face API key

# # Function to query the Hugging Face API

# def query_huggingface_api(prompt):
#     headers = {
#         "Authorization": f"Bearer {HF_API_TOKEN}",
#         "Content-Type": "application/json",
#     }
#     response = requests.post(HF_API_URL, headers=headers, json={"inputs": prompt})
#     if response.status_code != 200:
#         st.error(f"API Error: {response.status_code}, {response.text}")
#         raise Exception(f"API Error: {response.status_code}, {response.text}")
#     try:
#         return response.json()
#     except Exception as e:
#         st.error(f"Error parsing API response: {e}")
#         raise

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to detect questions in comments using the Mistral model

# def detect_questions(comments):
#     if not comments:
#         st.warning("No comments available for question detection.")
#         return []

#     questions = []
#     for comment in comments:
#         try:
#             result = query_huggingface_api(comment)
#             if 'generated_text' in result[0]:
#                 questions.append(comment)
#         except KeyError as e:
#             st.error(f"Key error in response: {e}")
#         except Exception as e:
#             st.error(f"Error detecting questions via API: {e}")

#     return questions

# # Function to perform sentiment analysis
# @st.cache_resource
# def load_sentiment_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# sentiment_pipeline = load_sentiment_model()

# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         return pipeline("text-classification", model="distilbert-base-uncased")
#     except Exception as e:
#         st.error(f"Error loading suggestion classification model: {e}")
#         return None

# suggestion_pipeline = load_suggestion_model()

# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']

#             # Map the labels to meaningful names
#             if suggestion_type == "LABEL_0":
#                 suggestion_type = "Suggestion"
#             elif suggestion_type == "LABEL_1":
#                 suggestion_type = "Feedback"
#             else:
#                 suggestion_type = "Other"

#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment and Question Detection")

#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Detecting questions..."):
#                     questions = detect_questions(comments)

#                 if questions:
#                     st.subheader("Questions Detected in Comments")
#                     for question in questions:
#                         st.write(f"- {question}")

#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)  # Scrollable DataFrame

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()
# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd
# import requests

# # Hugging Face API details for the Mistral model
# HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
# HF_API_TOKEN = "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"  # Replace with your Hugging Face API key

# # Define the template for questions
# # TEMPLATE = ("Questions typically start with words like who, what, when, where, why, or how, "
# #             "and end with a question mark (?). Analyze the given comment and determine if it matches this template. "
# #             "Return only the comments that contain a question and explicitly include a question mark (?). Ignore all other content.")
# # TEMPLATE = ("Questions typically start with interrogative words like who, what, when, where, why, or how, "
# #             "and must include a question mark (?). Analyze the provided comment to determine if it is a valid question. "
# #             "If it is, return only the question verbatim without additional content. Ensure the response is precise and concise.")
# # TEMPLATE = ("Questions typically start with interrogative words like who, what, when, where, why, or how, "
# #             "and must include a question mark (?). Analyze the provided comment to determine if it explicitly asks a question. "
# #             "Return only the question itself verbatim, without any additional content or explanation. Ensure the output is clean and concise.")
# # TEMPLATE = (
# #     "Analyze the provided text and extract only the question if it exists. "
# #     "A question is defined as a sentence that starts with words like who, what, when, where, why, how, or other interrogative words, "
# #     "and ends with a question mark (?). "
# #     "Exclude all other content, such as statements, explanations, or additional text. "
# #     "Return only the question verbatim, preserving its original wording, punctuation, and formatting, including the question mark."
# # )
# # TEMPLATE = (
# #     "Extract and return only the questions from the provided text. "
# #     "Ignore everything else, including statements, explanations, or irrelevant content. "
# #     "A question is identified as a sentence that begins with interrogative words like who, what, when, where, why, or how, "
# #     "and ends with a question mark (?). "
# #     "Display only the questions verbatim, preserving their original structure, punctuation, and formatting, including the question mark."
# # )
# TEMPLATE = (
#     "Extract only the sentences that are questions from the provided text. "
#     "A question starts with words like who, what, when, where, why, or how, and ends with a question mark (?). "
#     "Ignore all other content, including statements or non-question sentences. "
#     "Return only the questions verbatim, preserving their exact wording, punctuation, and formatting, with nothing else in the output."
# )






# # Function to query the Hugging Face API

# def query_huggingface_api(prompt):
#     headers = {
#         "Authorization": f"Bearer {HF_API_TOKEN}",
#         "Content-Type": "application/json",
#     }
#     response = requests.post(HF_API_URL, headers=headers, json={"inputs": prompt})
#     if response.status_code != 200:
#         st.error(f"API Error: {response.status_code}, {response.text}")
#         raise Exception(f"API Error: {response.status_code}, {response.text}")
#     try:
#         return response.json()
#     except Exception as e:
#         st.error(f"Error parsing API response: {e}")
#         raise

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to detect questions and question marks in comments using the Mistral model

# def detect_questions(comments):
#     if not comments:
#         st.warning("No comments available for question detection.")
#         return []

#     questions = []
#     for comment in comments:
#         try:
#             # result = query_huggingface_api(comment)
#             # if '?' in comment or 'question' in result[0].get('generated_text', '').lower():
#             #     questions.append(comment)
            
#             # prompt = f"Analyze the following comment and determine if it is a question. If it is, return the comment: '{comment}'"
#             # prompt = f"Read the following comments carefully and determine if it is a question. Analyze the full context and include whether a question mark is present. Only return the comment verbatim if it is a question:.Dont return anything else other than the question part make it restricted to questions '{comment}'"

#             # result = query_huggingface_api(prompt)
#             # if 'generated_text' in result[0]:
#             #     questions.append(result[0]['generated_text'])
#             # prompt = f"{TEMPLATE} Comment: '{comment}'"
#             # result = query_huggingface_api(prompt)
#             # if 'generated_text' in result[0]:
#             #     questions.append(result[0]['generated_text'])
#             prompt = f" {TEMPLATE} Comment: '{comment}'"
#             result = query_huggingface_api(prompt)
#             if 'generated_text' in result[0]:
#                 questions.append(result[0]['generated_text'])
#         except KeyError as e:
#             st.error(f"Key error in response: {e}")
#         except Exception as e:
#             st.error(f"Error detecting questions via API: {e}")

#     return questions

# # Function to perform sentiment analysis
# @st.cache_resource
# def load_sentiment_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# sentiment_pipeline = load_sentiment_model()

# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         return pipeline("text-classification", model="distilbert-base-uncased")
#     except Exception as e:
#         st.error(f"Error loading suggestion classification model: {e}")
#         return None

# suggestion_pipeline = load_suggestion_model()

# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']

#             # Map the labels to meaningful names
#             if suggestion_type == "LABEL_0":
#                 suggestion_type = "Suggestion"
#             elif suggestion_type == "LABEL_1":
#                 suggestion_type = "Feedback"
#             else:
#                 suggestion_type = "Other"

#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment and Question Detection")
#     # st.markdown(f"### Question Detection Template:{TEMPLATE}")

#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Detecting questions..."):
#                     questions = detect_questions(comments)

#                 if questions:
#                     st.subheader("Questions Detected in Comments")
#                 #     highlighted_questions = "".join([f"<span style='color:white; font-weight:bold;'>{question}</span>" for question in questions])  # Highlight in blue bold text
#                 # st.markdown(f"<div style='overflow-y:scroll; height:300px;'>{highlighted_questions}</div>", unsafe_allow_html=True)
#                     st.text_area("", "\n".join(questions), height=300, disabled=True)

#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)  # Scrollable DataFrame

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()
# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd
# import requests
# import openai

# # OpenAI API key
# OPENAI_API_KEY = "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"  # Replace with your OpenAI API key
# openai.api_key = OPENAI_API_KEY

# # Define the template for extracting questions
# TEMPLATE = (
#     "Extract only the sentences that are questions from the provided text. "
#     "A question starts with words like who, what, when, where, why, or how, and ends with a question mark (?). "
#     "Ignore all other content, including statements or non-question sentences. "
#     "Return only the questions verbatim, preserving their exact wording, punctuation, and formatting, with nothing else in the output."
# )

# # Function to query the OpenAI API
# def query_openai_api(prompt):
#     try:
#         response = openai.Completion.create(
#             model="text-davinci-003",  # Use OpenAI's text-davinci model
#             prompt=prompt,
#             max_tokens=500,
#             temperature=0.2,
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         st.error(f"OpenAI API Error: {e}")
#         raise

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to detect questions using OpenAI
# def detect_questions(comments):
#     if not comments:
#         st.warning("No comments available for question detection.")
#         return []

#     questions = []
#     for comment in comments:
#         try:
#             prompt = f"{TEMPLATE}\n\nComment: '{comment}'"
#             result = query_openai_api(prompt)
#             if result:
#                 questions.append(result)
#         except Exception as e:
#             st.error(f"Error detecting questions via OpenAI: {e}")

#     return questions

# # Function to perform sentiment analysis
# @st.cache_resource
# def load_sentiment_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# sentiment_pipeline = load_sentiment_model()

# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         return pipeline("text-classification", model="distilbert-base-uncased")
#     except Exception as e:
#         st.error(f"Error loading suggestion classification model: {e}")
#         return None

# suggestion_pipeline = load_suggestion_model()

# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']

#             # Map the labels to meaningful names
#             if suggestion_type == "LABEL_0":
#                 suggestion_type = "Suggestion"
#             elif suggestion_type == "LABEL_1":
#                 suggestion_type = "Feedback"
#             else:
#                 suggestion_type = "Other"

#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment and Question Detection")
#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Detecting questions..."):
#                     questions = detect_questions(comments)

#                 if questions:
#                     st.subheader("Questions Detected in Comments")
#                     st.text_area("", "\n".join(questions), height=300, disabled=True)

#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()
# import openai
# import streamlit as st
# from googleapiclient.discovery import build
# from transformers import pipeline
# import pandas as pd
# import requests

# # OpenAI API key
# OPENAI_API_KEY = "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"  # Replace with your OpenAI API key
# openai.api_key = OPENAI_API_KEY

# # Define the template for extracting questions
# TEMPLATE = (
#     "Extract only the sentences that are questions from the provided text. "
#     "A question starts with words like who, what, when, where, why, or how, and ends with a question mark (?). "
#     "Ignore all other content, including statements or non-question sentences. "
#     "Return only the questions verbatim, preserving their exact wording, punctuation, and formatting, with nothing else in the output."
# )

# # Function to query the OpenAI API using gpt-3.5-turbo
# def query_openai_api(prompt):
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",  # Updated to the recommended model
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,
#             temperature=0.2,
#         )
#         return response['choices'][0]['message']['content'].strip()
#     except Exception as e:
#         st.error(f"OpenAI API Error: {e}")
#         raise

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to detect questions using OpenAI
# def detect_questions(comments):
#     if not comments:
#         st.warning("No comments available for question detection.")
#         return []

#     questions = []
#     for comment in comments:
#         try:
#             prompt = f"{TEMPLATE}\n\nComment: '{comment}'"
#             result = query_openai_api(prompt)
#             if result:
#                 questions.append(result)
#         except Exception as e:
#             st.error(f"Error detecting questions via OpenAI: {e}")

#     return questions

# # Function to perform sentiment analysis
# @st.cache_resource
# def load_sentiment_model():
#     try:
#         return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
#     except Exception as e:
#         st.error(f"Error loading sentiment analysis model: {e}")
#         return None

# sentiment_pipeline = load_sentiment_model()

# def analyze_sentiment(comments):
#     if not comments:
#         st.warning("No comments available for analysis.")
#         return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

#     sentiments = []
#     for comment in comments:
#         try:
#             analysis = sentiment_pipeline(comment)
#             sentiment = analysis[0]['label']
#             score = analysis[0]['score']
#             sentiments.append((comment, sentiment, score))
#         except Exception as e:
#             st.error(f"Error analyzing sentiment: {e}")

#     return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# # Function to classify suggestions
# @st.cache_resource
# def load_suggestion_model():
#     try:
#         return pipeline("text-classification", model="distilbert-base-uncased")
#     except Exception as e:
#         st.error(f"Error loading suggestion classification model: {e}")
#         return None

# suggestion_pipeline = load_suggestion_model()

# def classify_suggestions(comments):
#     if not comments:
#         st.warning("No comments available for suggestions.")
#         return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

#     suggestions = []
#     for comment in comments:
#         try:
#             suggestion = suggestion_pipeline(comment)
#             suggestion_type = suggestion[0]['label']

#             # Map the labels to meaningful names
#             if suggestion_type == "LABEL_0":
#                 suggestion_type = "Suggestion"
#             elif suggestion_type == "LABEL_1":
#                 suggestion_type = "Feedback"
#             else:
#                 suggestion_type = "Other"

#             suggestions.append((comment, suggestion_type))
#         except Exception as e:
#             st.error(f"Error classifying suggestion: {e}")

#     return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# # Streamlit app
# def main():
#     st.title("YouTube Sentiment and Question Detection")
#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Detecting questions..."):
#                     questions = detect_questions(comments)

#                 if questions:
#                     st.subheader("Questions Detected in Comments")
#                     st.text_area("", "\n".join(questions), height=300, disabled=True)

#                 with st.spinner("Analyzing sentiment..."):
#                     sentiment_data = analyze_sentiment(comments)

#                 with st.spinner("Classifying suggestions..."):
#                     suggestion_data = classify_suggestions(comments)

#                 if not sentiment_data.empty:
#                     st.success("Analysis complete!")
#                     st.subheader("Sentiment Analysis")
#                     st.dataframe(sentiment_data, height=400)

#                     # Display sentiment summary
#                     st.subheader("Sentiment Summary")
#                     sentiment_summary = sentiment_data['Sentiment'].value_counts()
#                     st.bar_chart(sentiment_summary)

#                 if not suggestion_data.empty:
#                     st.subheader("Suggestions Classification")
#                     st.dataframe(suggestion_data, height=400)

# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()
# import openai
# import streamlit as st
# from googleapiclient.discovery import build
# import pandas as pd
# import os

# # Set OpenAI API Key
# openai.api_key = os.getenv("OPENAI_API_KEY", "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")  # Replace with your actual API key or set it as an environment variable

# # Define the optimized prompt for extracting only questions
# TEMPLATE = (
#     "Extract only the sentences that are questions from the provided text. "
#     "A question starts with words like who, what, when, where, why, or how and ends with a question mark (?). "
#     "Ignore everything else, including statements, usernames, and additional context. "
#     "Return only the questions verbatim, preserving their exact wording and punctuation."
# )

# # Function to query the OpenAI API using gpt-3.5-turbo
# def query_openai_api(prompt):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,
#             temperature=0.2,
#         )
#         # Properly access the response content
#         content = response['choices'][0]['message']['content']
#         return content.strip()
#     except Exception as e:
#         st.error(f"OpenAI API Error: {e}")
#         raise

# # Function to fetch YouTube comments
# def fetch_comments(api_key, video_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     comments = []
#     try:
#         response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id,
#             textFormat='plainText',
#             maxResults=100
#         ).execute()

#         for item in response.get('items', []):
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
#     except Exception as e:
#         st.error(f"Error fetching comments: {e}")
#     return comments

# # Function to detect questions using OpenAI
# def detect_questions(comments):
#     if not comments:
#         st.warning("No comments available for question detection.")
#         return []

#     combined_comments = "\n".join([f"- {comment}" for comment in comments])
#     prompt = f"{TEMPLATE}\n\nHere are the comments:\n{combined_comments}"

#     try:
#         result = query_openai_api(prompt)
#         return result.split("\n")  # Split the result into individual questions
#     except Exception as e:
#         st.error(f"Error detecting questions via OpenAI: {e}")
#         return []

# # Streamlit app
# def main():
#     st.title("YouTube Question Detection")
#     api_key = st.text_input("Enter your YouTube API Key:", type="password")
#     video_id = st.text_input("Enter YouTube Video ID:")

#     if st.button("Analyze Comments"):
#         if not api_key or not video_id:
#             st.error("Please provide both API Key and Video ID.")
#         else:
#             with st.spinner("Fetching comments..."):
#                 comments = fetch_comments(api_key, video_id)

#             if comments:
#                 with st.spinner("Detecting questions..."):
#                     questions = detect_questions(comments)

#                 if questions:
#                     st.subheader("Questions Detected in Comments")
#                     st.text_area("", "\n".join(questions), height=300, disabled=True)
#                 else:
#                     st.warning("No questions were detected in the comments.")

# if __name__ == "__main__":
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"
#     main()
import openai
import streamlit as st
from googleapiclient.discovery import build
from transformers import pipeline
import pandas as pd
import os

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY", "ReplacethiswithyourAPIkey")  # Replace with your actual API key or set it as an environment variable

# Define the optimized prompt for extracting only questions
TEMPLATE = (
    "Extract only the sentences that are questions from the provided text. "
    "A question starts with words like who, what, when, where, why, or how and ends with a question mark (?). "
    "Ignore everything else, including statements, usernames, and additional context. "
    "Return only the questions verbatim, preserving their exact wording and punctuation."
)

# Function to query the OpenAI API using gpt-3.5-turbo
def query_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.2,
        )
        content = response['choices'][0]['message']['content']
        return content.strip()
    except Exception as e:
        st.error(f"OpenAI API Error: {e}")
        raise

# Function to fetch YouTube comments
def fetch_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    try:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100
        ).execute()

        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
    except Exception as e:
        st.error(f"Error fetching comments: {e}")
    return comments

# Function to detect questions using OpenAI
def detect_questions(comments):
    if not comments:
        st.warning("No comments available for question detection.")
        return []

    combined_comments = "\n".join([f"- {comment}" for comment in comments])
    prompt = f"{TEMPLATE}\n\nHere are the comments:\n{combined_comments}"

    try:
        result = query_openai_api(prompt)
        return result.split("\n")  # Split the result into individual questions
    except Exception as e:
        st.error(f"Error detecting questions via OpenAI: {e}")
        return []

# Function to perform sentiment analysis
@st.cache_resource
def load_sentiment_model():
    try:
        return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    except Exception as e:
        st.error(f"Error loading sentiment analysis model: {e}")
        return None

sentiment_pipeline = load_sentiment_model()

def analyze_sentiment(comments):
    if not comments:
        st.warning("No comments available for analysis.")
        return pd.DataFrame(columns=['Comment', 'Sentiment', 'Confidence'])

    sentiments = []
    for comment in comments:
        try:
            analysis = sentiment_pipeline(comment)
            sentiment = analysis[0]['label']
            score = analysis[0]['score']
            sentiments.append((comment, sentiment, score))
        except Exception as e:
            st.error(f"Error analyzing sentiment: {e}")

    return pd.DataFrame(sentiments, columns=['Comment', 'Sentiment', 'Confidence'])

# Function to classify suggestions
@st.cache_resource
def load_suggestion_model():
    try:
        return pipeline("text-classification", model="distilbert-base-uncased")
    except Exception as e:
        st.error(f"Error loading suggestion classification model: {e}")
        return None

suggestion_pipeline = load_suggestion_model()

def classify_suggestions(comments):
    if not comments:
        st.warning("No comments available for suggestions.")
        return pd.DataFrame(columns=['Comment', 'Suggestion Type'])

    suggestions = []
    for comment in comments:
        try:
            suggestion = suggestion_pipeline(comment)
            suggestion_type = suggestion[0]['label']

            # Map the labels to meaningful names
            if suggestion_type == "LABEL_0":
                suggestion_type = "Suggestion"
            elif suggestion_type == "LABEL_1":
                suggestion_type = "Feedback"
            else:
                suggestion_type = "Other"

            suggestions.append((comment, suggestion_type))
        except Exception as e:
            st.error(f"Error classifying suggestion: {e}")

    return pd.DataFrame(suggestions, columns=['Comment', 'Suggestion Type'])

# Streamlit app
def main():
    st.title("YouTube Sentiment, Question Detection, and Suggestion Classification")
    api_key = st.text_input("Enter your YouTube API Key:", type="password")
    video_id = st.text_input("Enter YouTube Video ID:")

    if st.button("Analyze Comments"):
        if not api_key or not video_id:
            st.error("Please provide both API Key and Video ID.")
        else:
            with st.spinner("Fetching comments..."):
                comments = fetch_comments(api_key, video_id)

            if comments:
                with st.spinner("Detecting questions..."):
                    questions = detect_questions(comments)

                if questions:
                    st.subheader("Questions Detected in Comments")
                    st.text_area("", "\n".join(questions), height=300, disabled=True)

                with st.spinner("Analyzing sentiment..."):
                    sentiment_data = analyze_sentiment(comments)

                with st.spinner("Classifying suggestions..."):
                    suggestion_data = classify_suggestions(comments)

                if not sentiment_data.empty:
                    st.success("Analysis complete!")
                    st.subheader("Sentiment Analysis")
                    st.dataframe(sentiment_data, height=400)

                    # Display sentiment summary
                    st.subheader("Sentiment Summary")
                    sentiment_summary = sentiment_data['Sentiment'].value_counts()
                    st.bar_chart(sentiment_summary)

                if not suggestion_data.empty:
                    st.subheader("Suggestions Classification")
                    st.dataframe(suggestion_data, height=400)

if __name__ == "__main__":
    os.environ["STREAMLIT_SERVER_PORT"] = "8503"
    main()




# if __name__ == "__main__":
#     import os
#     os.environ["STREAMLIT_SERVER_PORT"] = "8503"  # Change to an unused port
#     main()
