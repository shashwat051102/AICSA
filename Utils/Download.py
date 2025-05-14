import io
from xhtml2pdf import pisa
import streamlit as st
import markdown

def create_pdf(content):
    pdf_buffer = io.BytesIO()
    html = f"<html><body>{content}</body></html>"
    pisa_status = pisa.CreatePDF(io.StringIO(html), dest=pdf_buffer)
    if pisa_status.err:
        return None
    pdf_buffer.seek(0)
    return pdf_buffer

def markdown_to_html(md_content):
    return markdown.markdown(md_content)

def download_pdf_report(result, filename_prefix="resume", is_markdown=False):
    if is_markdown:
        result = markdown_to_html(result)
    pdf_data = create_pdf(result)
    if pdf_data:
        st.download_button(
            label="📄 Download Resume as PDF",
            data=pdf_data,
            file_name=f"{filename_prefix}.pdf",
            mime="application/pdf",
        )
