import os
from crewai import Crew
from crewai import Process
from langchain_groq import ChatGroq
from agents import RoastAgent
from tasks import Roast
import streamlit as st
import PyPDF2

st.set_page_config(page_icon=":bar_chart:", layout="wide")



def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )



def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file, strict=False)
        pdf_text = []
        for page in reader.pages:
            content = page.extract_text()
            if content:  
                pdf_text.append(content)
        return pdf_text
    except Exception as e:
        st.write(f"Error extracting text from PDF: {e}")
        return []    



def text_cleaning(extracted_text):
    cleaned_text = []
    for text in extracted_text:
        cleaned = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
        cleaned_text.append(cleaned)
    return cleaned_text

class RoastCrew:

    def __init__(self, cleaned_data):
        self.cleaned_data = cleaned_data
        self.output_placeholder = st.empty()

    def run(self):
        agents = RoastAgent()
        tasks = Roast()

        r1 = agents.r1()
        

        task1 = tasks.task1(
            r1,
            self.cleaned_data
            
        )

        

        crew = Crew(
            agents=[
            r1
            ],
            tasks=[task1],
            process=Process.sequential,
            verbose=False
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result


if __name__ == "__main__":
    icon("Resume Roaster")

    st.subheader("Think your resume is flawless? Let us roast it to a crisp!",
                 divider="rainbow", anchor=False)

    

    with st.sidebar:
        
        st.header("👇 Upload Your Resume")
        st.info("Get started by uploading your resume in PDF format.")
        uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
        
        if uploaded_file is not None:
            extracted_text = extract_text_from_pdf(uploaded_file)
            cleaned_data = text_cleaning(extracted_text)
            
        

        st.link_button("GitHub", "https://github.com/TheVixhal", use_container_width=True)
        st.link_button("LinkedIn", "https://www.linkedin.com/in/vixhal", use_container_width=True)
        


if st.button("Roast My Career!", type="primary"):
    if uploaded_file is None:
        st.warning("Ch#tiye Resume Toh Upload Karle...")
    else: 
        with st.status("🤖 **Roasting...**", state="running", expanded=False) as status:
            with st.spinner("Roasting Your Career..."):
                with st.container(height=500, border=True):
                
                     legal_crew = RoastCrew(cleaned_data)
                     result = legal_crew.run()
                status.update(label="✅ Crispy Roasted Resume!", state="complete", expanded=False) 
        with st.subheader("Crispy Roasted Resume", anchor=False, divider="rainbow"):  
            with st.container(height=None, border=True):

                 st.markdown(result)