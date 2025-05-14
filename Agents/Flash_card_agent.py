from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from Tools.Code_interpreter_tool import code_interpreter
from Tools.PDF_rag_tool import PDF_tool
from Tools.Website_rag_tool import website_tool
from Tools.YouTube_tool import youtube_search_tool
from langchain_openai import ChatOpenAI
import openai
import os

load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")
# llm = ChatGroq(api_key=api_key, model="groq/llama-3.3-70b-versatile")
api_key = os.getenv("OPENAI_API_KEY")
# llm = Ollama(model="gemma3:4b")
if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

openai.api_key = api_key
llm = ChatOpenAI(api_key=api_key, model="gpt-4.1-mini")

FlashCardAgent = Agent(
    role="Flash Card Creator",
    goal="""
You are a flash card generator. A student will provide educational material in {extracted_text}, which will always be text content from a PDF.

While using the website tools and scrapping the content, make sure to extract the main content and avoid any unnecessary information.
And make sure the website content in the flash card format

Your responsibilities:
- Process the input text content from the PDF or Website directly.
- Generate educational flash cards from it in Anki format.
""",
    backstory="You're an expert at turning raw educational material into effective flashcards to help students study efficiently.",
    tools=[PDF_tool,website_tool],
    llm=llm
)
