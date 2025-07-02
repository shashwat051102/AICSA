# AI Career & Study Assistant (AICSA)

AI Career & Study Assistant (AICSA) is a Streamlit-powered application designed to help students and professionals with coding, study, and career-related tasks using AI agents. The app can generate summaries, notes, flashcards, quizzes, and resumes from PDFs, websites, or user input.

## Features

- **Coding Task:** Get help with coding problems and tasks.
- **Flash Card Task:** Generate flashcards from PDFs or websites.
- **Note Making Task:** Create concise notes from educational content.
- **Summary Task:** Summarize large documents or web pages.
- **Quiz Task:** Generate quiz questions from study material.
- **Resume Task:** Build professional resumes from your details.

## Project Structure

```
AICSA/
├── app.py
├── Agents/
├── Task/
├── Tools/
├── Utils/
├── db/
├── requirements.txt
└── .env.example
```

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd AICSA
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure environment variables:**
    - Copy `.env.example` to `.env` and fill in your API keys (OpenAI, Groq, etc.).

4. **Run the app:**
    ```sh
    streamlit run app.py
    ```

## Usage

- Select a task from the sidebar.
- Provide the required input (text, PDF, website URL, or personal details).
- Click the relevant button to process.
- Download results as PDF if needed.

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies.

## File Overview

- `app.py`: Main Streamlit app.
- `Agents/`: AI agent definitions for each task.
- `Task/`: Task logic for each workflow.
- `Tools/`: Utility tools for PDF, website, and YouTube processing.
- `Utils/`: Helper functions (e.g., text extraction, PDF download).
- `db/`: Local database files.

## License

MIT License

---

**Note:** Ensure you have valid API keys for OpenAI, Groq, and other services in your
