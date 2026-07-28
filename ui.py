import streamlit as st
import re
from agents.youtube_agent import build_youtube_agent

def clean_youtube_url(url: str) -> str:
    """Extract standard YouTube URL without tracking parameters."""
    url = url.strip().strip('"').strip("'")
    pattern = r"(?:v=|\/|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# Input box
video_url = st.text_input("Enter Youtube Video Link")
button = st.button("Analyze Video")

if video_url and button:
    cleaned_url = clean_youtube_url(video_url)
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {cleaned_url}"
        )

    st.markdown("### Analysis Report of Video:")
    st.markdown(response.content)