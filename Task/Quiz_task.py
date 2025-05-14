from crewai import Task
from Agents.Quizz_agent import Quiz_agent
from Tools.PDF_rag_tool import PDF_tool
from Tools.Website_rag_tool import website_tool

Quizz_task = Task(
    description="""
    A student is requesting quiz questions based on provided content.
    The content will be passed to you in {extracted_text} and will be:
    - Extracted text from a PDF file
    - Website content
    While using the website tools and scrapping the content, make sure to extract the main content and create quiz questions from it.
    And make sure the website content in the quiz format
    
    Make sure to create only quiz questions not any other content.
    """,
    expected_output="Create quiz questions based on the content provided in {extracted_text}.",
    input_variable="extracted_text",
    tools=[PDF_tool, website_tool],
    agent=Quiz_agent,
)
