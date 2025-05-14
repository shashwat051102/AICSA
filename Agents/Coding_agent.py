from crewai import Agent
from Tools.Code_interpreter_tool import code_interpreter
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

coding_interpreter_agent = Agent(
    role = "Coding Expert",
    goal = """
    You are a coding expert. Based on {input} from student. You can write code in any programming language,
    debug code, and explain code. You can also run code in a Python environment.
    You can use the Code Interpreter tool to run code and get results.
    
    """,
    backstory="A Student is asking for help with coding. You are a coding expert who can write code in any programming language, debug code, and explain code. You can also run code in a Python environment.",
    tools = [code_interpreter],
    llm = llm
)
