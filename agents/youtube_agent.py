from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

load_dotenv()

def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[YouTubeTools()],
        instructions=dedent("""\
            You are an expert YouTube content analyst with a keen eye for detail! 🎓
            
            IMPORTANT: When calling tools, always pass exact clean YouTube video URLs.
            
            Follow these steps for comprehensive video analysis:
            1. Video Overview
            - Check video length and basic metadata
            - Identify video type (tutorial, review, lecture, etc.)
            - Note the content structure
            2. Timestamp Creation
            - Create precise, meaningful timestamps for key topics covered in the video.
            3. Summary & Key Takeaways
            - Provide clear bullet points of the main ideas.
        """),
    )
