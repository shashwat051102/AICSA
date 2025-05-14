from crewai import Agent
from Tools.Website_rag_tool import website_tool
from Tools.PDF_rag_tool import PDF_tool
from Tools.YouTube_tool import youtube_search_tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import openai
from dotenv import load_dotenv


import os
load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# llm = ChatGroq(api_key=api_key, model="groq/llama-3.3-70b-versatile")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

openai.api_key = api_key
llm = ChatOpenAI(api_key=api_key, model="gpt-4.1-mini")

# llm = OllamaLLM(model="gemma3:4b")

NoteMakingAgent = Agent(
    role = "Note Maker",
    goal = """
    Based on the content provided in {extracted_text}, you are a note maker. 
    You can create notes from any content, including text, PDF, and website content.
    Use tools based on the content type if it plain text or PDF then use PDF_tool and it uses Website then use website_tool
    
    While using the website tools and scrapping the content, make sure to extract the main content and avoid any unnecessary information.
    And make sure the website content in the note format
    Make sure to include the following:
    - Key points
    - Important information
    - Summarized content
    - Any other relevant information
    - Use bullet points for clarity
    - Use headings and subheadings to organize the content
    - Use clear and concise language
    - Use examples to illustrate key points
    
    Make sure you make it concise short and clear
    
    """,
    backstory = "A student is asking for help with note-making. You are a note maker who can create notes from any content, including text, PDF, and website content.",
    tools = [PDF_tool, website_tool, youtube_search_tool],
    llm = llm
    
)