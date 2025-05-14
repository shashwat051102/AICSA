from crewai import Task
from Agents.Flash_card_agent import FlashCardAgent
from Tools.PDF_rag_tool import PDF_tool
from Tools.Website_rag_tool import website_tool
from Tools.YouTube_tool import youtube_search_tool

FlashCard_task = Task(
    description="""
    A student is requesting flash cards based on provided content.
    ALWAYS use the PDF tool to process the input before generating any output.
    
    While using the website tools and scrapping the content, make sure to extract the main content and avoid any unnecessary information.
    And make sure the website content in the flash card format

    The content will be passed to you in {extracted_text} and will be:
    - Extracted text from a PDF file
    - Website content

    Use the PDF tool to process the input and then generate flashcards from the content in Anki format.
    """,
    expected_output="Flash cards in Anki format.",
    input_variable="extracted_text",
    tools=[PDF_tool,website_tool],
    agent=FlashCardAgent,
)
