# YouTube-Video-Finder

# 🎥 YouTube Video Finder with Voice/Text + AI Analysis

## 📌 Features:
- Accepts search query via **text** or **voice** (Hindi/English).
- Searches YouTube using the **YouTube Data API**.
- **Filters**:
  - Duration: 4–20 minutes
  - Published in the last 14 days
  - Returns top 20 results.
- Analyzes video titles using **AI** (ChatGPT or Gemini 2.0).
- Recommends the best video based on AI analysis.

## 🛠️ How to Run:
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

2. **Set your API keys in environment variables or directly in the code:**

- YouTube API Key

- OpenAI API Key (if using ChatGPT or Gemini 2.0)

3. **Run using Streamlit:**
```
streamlit run youtube_streamlit_app.py
```
## ✅ **Example Query:**
```
- AI for beginners
```
## 📂 Output:
- The best video based on title analysis will be shown on the UI.

- The video recommendation will appear based on the filters and AI analysis.

## 🤖 AI Analysis:
- Uses ChatGPT or Gemini 2.0 for analyzing and recommending the best video based on the search query.

- The AI looks at video titles, descriptions, and relevance to provide the best suggestions.

## 🚀 Demo:
You can test the YouTube Video Finder app and try searching for your favorite topics like "AI for beginners" to get the top recommendations.
