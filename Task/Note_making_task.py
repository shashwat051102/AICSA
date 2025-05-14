from crewai import Task
from Tools.PDF_rag_tool import PDF_tool
from Tools.Website_rag_tool import website_tool
from Tools.YouTube_tool import youtube_search_tool
from Agents.Note_making_agent import NoteMakingAgent

NoteMaking_task = Task(
    description="""
    A student is requesting notes based on provided content.
    ALWAYS use the PDF tool to process the input before generating any output.

    The content will be passed to you in {extracted_text} and will be:
    - Extracted text from a PDF file
    - Website content
    
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

    Use the PDF tool to process the input and then generate notes from the content.
    """,
    expected_output="Create notes based on the content provided in {extracted_text}.",  
    input_variable="extracted_text",
    tools=[PDF_tool, website_tool, youtube_search_tool],
    agent=NoteMakingAgent,
)