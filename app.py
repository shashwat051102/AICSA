import patch_sqlite
import streamlit as st
from Agents.Coding_agent import coding_interpreter_agent
from Agents.Flash_card_agent import FlashCardAgent
from Task.Coding_task import Coding_interpreter_task
from Task.Flash_card_task import FlashCard_task
from Agents.Note_making_agent import NoteMakingAgent
from Task.Note_making_task import NoteMaking_task
from Task.Summary_task import Summary_task
from Agents.Summary_agent import Summary_agent
from Agents.Quizz_agent import Quiz_agent
from Task.Quiz_task import Quizz_task
from Agents.resume_agent import Resume_agent
from Task.resume_task import Resume_task
from Utils.Extract_text import extract_text_from_pdf
from Utils.Download import download_pdf_report
from crewai import Crew

# --- Import libraries for image processing ---
from PIL import Image
import pytesseract

# If Tesseract is not in your system's PATH, you might need to specify the path.
# For example, on Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


st.set_page_config(page_title="AI Career & Study Assistant (AICSA)", page_icon=":rocket:", layout="wide")

# --- Header ---
st.markdown("""
    <h1 style='text-align: center; color: #4F8BF9;'>AI Career & Study Assistant (AICSA)</h1>
    <p style='text-align: center; color: #555;'>Your all-in-one assistant for coding, study, and career tasks.</p>
    <hr>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("AICSA Menu")
    st.info("Select a task to get started!")
    task = st.selectbox(
        "Choose a task",
        (
            "Coding Task", "Flash Card Task", "Note Making Task",
            "Summary Task", "Quiz Task", "Resume Task"
        )
    )

# --- Main Content ---
if task == "Coding Task":
    st.header("💻 Coding Task")
    st.write("Describe your coding problem or request below.")
    choice = st.selectbox("Select input type", ("Text", "Image"))
    
    user_input = None
    if choice == "Text":
        user_input = st.text_area("Enter your coding task:", help="Type your coding question or task here.")
    elif choice == "Image":
        user_input = st.file_uploader("Upload an image of your coding task:", type=["jpg", "jpeg", "png"])

    if st.button("🚀 Submit"):
        if not user_input:
            st.warning("Please provide an input (text or image) before submitting.")
        else:
            with st.spinner("Processing your coding task..."):
                final_input_str = ""
                if choice == "Text":
                    final_input_str = user_input
                elif choice == "Image":
                    try:
                        # Open the uploaded image file
                        image = Image.open(user_input)
                        # Use pytesseract to perform OCR and extract text
                        final_input_str = pytesseract.image_to_string(image)
                        if not final_input_str.strip():
                             st.error("Could not extract any text from the image. Please ensure the image is clear and contains machine-readable text.")
                             st.stop()
                    except Exception as e:
                        st.error(f"An error occurred while processing the image: {e}")
                        st.stop()

                # Kick off the crew with the extracted string
                crew = Crew(agents=[coding_interpreter_agent], tasks=[Coding_interpreter_task], memory=False)
                result = crew.kickoff({"input": final_input_str})
                
                st.success("Task completed!")
                st.markdown(result)
                download_pdf_report(result, "coding_task")

elif task == "Flash Card Task":
    st.header("📚 Flash Card Task")
    Method_input = st.selectbox("Select a method", ("PDF", "Website"))
    
    if Method_input == "PDF":
        method = st.file_uploader("Upload PDF file", type="pdf")
        
        if method is not None:
            st.success("PDF file uploaded successfully!")
            
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    extracted_text = extract_text_from_pdf(method)
                    crew = Crew(agents = [FlashCardAgent], tasks = [FlashCard_task],memory = False)
                    result = crew.kickoff(
                        {
                            "extracted_text": extracted_text
                        }
                    )
                    st.success("Task completed!")
                    st.markdown(result)
                    download_pdf_report(result, "flashcard")
    elif Method_input == "Website":
        extracted_text = st.text_input("Enter website URL")
        
        if extracted_text:
            st.success("Website URL entered successfully!")
            
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    
                    crew = Crew(agents = [FlashCardAgent], tasks = [FlashCard_task],memory = False)
                    result = crew.kickoff({"extracted_text": f"Website URL: {extracted_text}"})

                    st.success("Task completed!")
                    st.markdown(result) 
                    download_pdf_report(result, "flashcard")


elif task == "Note Making Task":
    st.header("📝 Note Making")
    Method_input = st.selectbox("Select a method", ("PDF", "Website"))
    if Method_input == "PDF":
        method = st.file_uploader("Upload PDF file", type="pdf")
        
        if method is not None:
            st.success("PDF file uploaded successfully!")
    
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    try:
                        extracted_text = extract_text_from_pdf(method)
                        crew = Crew(agents = [NoteMakingAgent], tasks = [NoteMaking_task],memory = False)
                        result = crew.kickoff({"extracted_text": extracted_text})
                        st.success("Task completed!")
                        st.markdown(result, unsafe_allow_html=True)
                        download_pdf_report(result, "notes")
                    except Exception as e:
                        st.error(f"Error occurred: {e}")
    elif Method_input == "Website":
        extracted_text= st.text_input("Enter website URL")
        
        if extracted_text:
            st.success("Website URL entered successfully!")
            
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    crew = Crew(agents = [NoteMakingAgent], tasks = [NoteMaking_task],memory = False)
                    result = crew.kickoff({"extracted_text": f"Website URL: {extracted_text}"})

                    st.success("Task completed!")
                    st.markdown(result, unsafe_allow_html=True)
                    download_pdf_report(result, "notes")
if task == "Summary Task":
    st.header("📊 Summary Task")
    Method_input = st.selectbox("Select a method", ("PDF", "Website"))
    if Method_input == "PDF":
        method = st.file_uploader("Upload PDF file", type="pdf")
        
        if method is not None:
            st.success("PDF file uploaded successfully!")
    
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    try:
                        extracted_text = extract_text_from_pdf(method)
                        crew = Crew(agents = [Summary_agent], tasks = [Summary_task],memory = False)
                        result = crew.kickoff({"extracted_text": extracted_text})
                        st.success("Task completed!")
                        st.markdown(result, unsafe_allow_html=True)
                        download_pdf_report(result, "summary")
                    except Exception as e:
                        st.error(f"Error occurred: {e}")
    elif Method_input == "Website":
        extracted_text= st.text_input("Enter website URL")
        
        if extracted_text:
            st.success("Website URL entered successfully!")
            
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    crew = Crew(agents = [Summary_agent], tasks = [Summary_task],memory = False)
                    result = crew.kickoff({"extracted_text": f"Website URL: {extracted_text}"})

                    st.success("Task completed!")
                    st.markdown(result, unsafe_allow_html=True)
                    download_pdf_report(result, "summary")
elif task == "Quiz Task":
    st.header("📝 Quiz Task")
    Method_input = st.selectbox("Select a method", ("PDF", "Website"))
    if Method_input == "PDF":
        method = st.file_uploader("Upload PDF file", type="pdf")
        
        if method is not None:
            st.success("PDF file uploaded successfully!")
    
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    try:
                        extracted_text = extract_text_from_pdf(method)
                        crew = Crew(agents = [Quiz_agent], tasks = [Quizz_task],memory = False)
                        result = crew.kickoff({"extracted_text": extracted_text})
                        st.success("Task completed!")
                        st.markdown(result, unsafe_allow_html=True)
                        download_pdf_report(result, "quiz")
                    except Exception as e:
                        st.error(f"Error occurred: {e}")
    elif Method_input == "Website":
        extracted_text= st.text_input("Enter website URL")
        
        if extracted_text:
            st.success("Website URL entered successfully!")
            
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    crew = Crew(agents = [Quiz_agent], tasks = [Quizz_task],memory = False)
                    result = crew.kickoff({"extracted_text": f"Website URL: {extracted_text}"})

                    st.success("Task completed!")
                    st.markdown(result, unsafe_allow_html=True)
                    download_pdf_report(result, "quiz")
elif task == "Resume Task":
    st.header("📝 Resume Task")
    Name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    phone = st.text_input("Enter your phone number:")
    address = st.text_input("Enter your address:")
    skills = st.text_input("Enter your skills (comma-separated):")
    experience = st.text_input("Enter your experience (e.g., 5 years):")
    education = st.text_input("Enter your education (e.g., Bachelor's in Computer Science):")
    projects = st.text_input("Enter your projects (comma-separated):")
    certifications = st.text_input("Enter your certifications (comma-separated):")
    if st.button("Generate Resume"):
        with st.spinner("Generating resume..."):
            crew = Crew(agents = [Resume_agent], tasks = [Resume_task],memory = False)
            result = crew.kickoff(
                {
                    "Name": Name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "skills": skills,
                    "experience": experience,
                    "education": education,
                    "projects": projects,
                    "certifications": certifications,
                }
            )
            st.success("Resume generated!")
            st.markdown(result)
            download_pdf_report(result, Name or "resume")

# --- Footer ---
st.markdown("""
    <hr>
    <div style='text-align: center; color: #888; font-size: 0.9em;'>
        &copy; 2024 AI Career & Study Assistant (AICSA) | Powered by Streamlit
    </div>
""", unsafe_allow_html=True)
