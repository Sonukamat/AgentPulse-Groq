import os
import re
import streamlit as st

# Streamlit secrets se GROQ_API_KEY load karne ke liye
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered"
)

def clean_youtube_url(url: str) -> str:
    """Extract standard YouTube URL without tracking parameters."""
    url = url.strip().strip('"').strip("'")
    pattern = r"(?:v=|\/|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

st.title("🎥 AI YouTube Video Analyzer")
st.write("Analyze YouTube videos instantly using Agno Framework & Groq LLM!")

# Sidebar config (agar Secrets me API key na ho to user yahan daal sake)
with st.sidebar:
    st.header("🔑 Configuration")
    api_key_input = st.text_input("Groq API Key", type="password", help="Enter your Groq API Key")
    if api_key_input:
        os.environ["GROQ_API_KEY"] = api_key_input

youtube_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")
user_prompt = st.text_area("What would you like to analyze?", value="Provide a detailed summary and key timestamps for this video.")

if st.button("Analyze Video", type="primary"):
    if not os.environ.get("GROQ_API_KEY"):
        st.error("⚠️ Please provide a Groq API Key in the sidebar or in Streamlit Secrets!")
    elif not youtube_url:
        st.warning("⚠️ Please enter a valid YouTube Video URL.")
    else:
        cleaned_url = clean_youtube_url(youtube_url)
        with st.spinner("Analyzing YouTube video... Please wait."):
            try:
                from agents.youtube_agent import build_youtube_agent
                agent = build_youtube_agent()
                query = f"Analyze the following video: {cleaned_url}\nUser instructions: {user_prompt}"
                response = agent.run(query)
                st.subheader("📊 Analysis Result")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")
