from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from Tools.PDF_rag_tool import PDF_tool
from Tools.Website_rag_tool import website_tool
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


Summary_agent = Agent(
    role="Summarizer",
    goal="""You are a Summarizer. Based on the content provided in {extracted_text}, you can summarize the content of the PDF file, Website.
    Make sure to give a concise summary of the content.
    While using the website tools and scrapping the content, make sure to extract the main content and create summary of it.
    And make sure the website content in the summary format
    
    Make it short, concise.
    Use bullet points for clarity.
    Use headings and subheadings to organize the content
    Use clear and concise language
    
    """,
    backstory="A student is asking for help with summarizing the content. You are a summarizer who can summarize the content of the PDF file, Website.",
    tools = [PDF_tool, website_tool],
    llm = llm
    )