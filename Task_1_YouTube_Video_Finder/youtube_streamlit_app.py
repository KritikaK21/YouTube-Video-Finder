import streamlit as st
import speech_recognition as sr
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import openai

# ----------------------- CONFIGURATION -----------------------

YOUTUBE_API_KEY = "AIzaSyAWTRVWGSIX2HPgZUr6qw9eqBTVrdW_TxU"
openai.api_key = "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"

# ----------------------- YOUTUBE SEARCH FUNCTION -----------------------

def search_youtube_videos(query):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    published_after = (datetime.utcnow() - timedelta(days=14)).isoformat("T") + "Z"
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        order="relevance",
        publishedAfter=published_after,
        maxResults=20,
        relevanceLanguage="en"
    )
    response = request.execute()
    
    video_ids = [item["id"]["videoId"] for item in response["items"]]
    
    # Get video details for filtering duration
    video_details = youtube.videos().list(
        part="contentDetails,snippet",
        id=",".join(video_ids)
    ).execute()
    
    final_results = []
    for item in video_details["items"]:
        duration = item["contentDetails"]["duration"]
        
        # Parse ISO 8601 duration to minutes
        minutes = convert_iso8601_to_minutes(duration)
        
        if 4 <= minutes <= 20:
            final_results.append({
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "duration": f"{minutes} mins"
            })
    
    return final_results

def convert_iso8601_to_minutes(duration):
    import isodate
    try:
        td = isodate.parse_duration(duration)
        return int(td.total_seconds() / 60)
    except:
        return 0

# ----------------------- AI ANALYSIS -----------------------

def get_best_title_from_ai(titles):
    prompt = f"""You are an AI assistant helping a beginner. Given these YouTube video titles about AI:

{chr(10).join([f"{i+1}. {title}" for i, title in enumerate(titles)])}

Which one is most suitable for a beginner trying to learn about AI? Just return the best title."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# ----------------------- VOICE INPUT -----------------------

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("❌ Could not understand your speech.")
        except sr.RequestError as e:
            st.error(f"❌ Could not request results; {e}")
    return None

# ----------------------- STREAMLIT UI -----------------------

st.set_page_config(page_title="YouTube Video Finder with AI", layout="centered")

st.title("🎬 YouTube Video Finder with AI Analysis")

col1, col2 = st.columns([1, 4])
with col1:
    use_voice = st.button("🎤 Use Voice")
with col2:
    query = st.text_input("Or type your query here:", "")

if use_voice:
    voice_text = get_voice_input()
    if voice_text:
        query = voice_text

if query:
    st.markdown(f"🔍 Searching YouTube for: **{query}**")
    results = search_youtube_videos(query)

    if results:
        st.subheader("📺 Filtered Results")
        titles = []
        for vid in results:
            st.markdown(f"**{vid['title']}**\n\n🔗 [Watch here]({vid['url']})\n⏱️ {vid['duration']}")
            titles.append(vid["title"])
        
        # AI-based title selection
        best_title = get_best_title_from_ai(titles)
        st.success(f"🤖 AI recommends this title for beginners: **{best_title}**")
    else:
        st.warning("😕 No suitable videos found.")

