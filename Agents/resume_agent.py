from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import openai
import os

load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# llm = ChatGroq(api_key=api_key, model="groq/llama-3.3-70b-versatile")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

openai.api_key = api_key
llm = ChatOpenAI(api_key=api_key, model="gpt-4.1-mini")


Resume_agent = Agent(
    role = "Resume Builder",
    goal = """
    Your are a resume builder.
    User Will provide {Name} and {address} and {email} and {phone} and {skills} and {experience} and {education} and {certifications} and {projects} to create a resume.
    with all this information you have to create a resume in a professional format.
    
    """,
    backstory="A student is asking for help with resume building. You are a resume builder who can create a resume in a professional format.",
    llm=llm,
)