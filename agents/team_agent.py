from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

groq_model = Groq(id="llama-3.3-70b-versatile")

eng_agent = Agent(name="English Agent", role="You answer questions in English", model=groq_model)
chi_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese", model=groq_model)
hindi_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi", model=groq_model)

team_leader = Team(
    name="Answer & Translation Team",
    members=[eng_agent, chi_agent, hindi_agent],
    model=groq_model,
    markdown=True,
    show_members_responses=True,
    instructions=""" All member agents must respond to answer the query in their specific language. 
                        Do not route to just one agent.
                        Output the response of all agents.
                """
)

if __name__ == "__main__":
    team_leader.print_response("What is the capital of India?")