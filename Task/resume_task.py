from crewai import Task
from Agents.resume_agent import Resume_agent

Resume_task = Task(
    description="""
    A student is requesting a resume based on provided content.
    The content will be passed to you in {Name} and {address} and {email} and {phone} and {skills} and {experience} and {education} and {certifications} and {projects}.
    While using the website tools and scrapping the content, make sure to extract the main content and create resume from it.
    And make sure the website content in the resume format
    """,
    expected_output="Create a resume based on the content provided in {Name} and {address} and {email} and {phone} and {skills} and {experience} and {education} and {certifications} and {projects}.",
    input_variable="skills",
    agent=Resume_agent,
)