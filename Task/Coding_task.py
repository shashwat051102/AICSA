from crewai import Task
from Tools.Code_interpreter_tool import code_interpreter
from Agents.Coding_agent import coding_interpreter_agent

Coding_interpreter_task = Task(
    description = """
    Student will give you {input} and you will help them with coding. You can write code in any programming language,
    debug code, and explain code. You can also run code in a Python environment.
    You can use the Code Interpreter tool to run code and get results.
    """,
    expected_output="Code, explanation, and results of the code execution.",
    input_variable="input",
    tools=[code_interpreter],
    agent=coding_interpreter_agent,
)