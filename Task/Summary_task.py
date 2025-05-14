from crewai import Task
from Agents.Summary_agent import Summary_agent
from Tools.PDF_rag_tool import PDF_tool
from Tools.Website_rag_tool import website_tool


Summary_task = Task(
    description="""
    A student is requesting a summary based on provided content.


    The content will be passed to you in {extracted_text} and will be:
    - Extracted text from a PDF file
    - Website content
    
    While using the website tools and scrapping the content, make sure to extract the main content and create summary of it.
    And make sure the website content in the summary format
    
    Make it short, concise.
    Use bullet points for clarity.
    Use headings and subheadings to organize the content
    Use clear and concise language

    """,
    expected_output="Create a summary based on the content provided in {extracted_text}.Make it short, concise.Use bullet points for clarity.Use headings and subheadings to organize the contentUse clear and concise language",  
    input_variable="extracted_text",
    tools=[PDF_tool, website_tool],
    agent=Summary_agent,
)
