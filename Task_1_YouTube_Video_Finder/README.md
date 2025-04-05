# 🎥 YouTube Video Finder with Voice/Text + AI Analysis

## 📌 Features:
- Accepts search query via text or voice (Hindi/English).
- Searches YouTube using YouTube Data API.
- Filters:
  - Duration: 4–20 minutes
  - Published in the last 14 days
- Returns top 20 results.
- Analyzes titles using AI (ChatGPT or Gemini 2.0).
- Recommends the best video.

## 🛠️ How to Run
1. Install dependencies:

pip install -r requirements.txt


2. Set your API keys in environment variables or directly in the code:
   - YouTube API Key
   - OpenAI API Key (if using ChatGPT)
3. Run using Streamlit:

streamlit run youtube_streamlit_app.py


## ✅ Example Query:

AI for beginners


## 📂 Output:
- Best video based on title analysis shown on UI.
