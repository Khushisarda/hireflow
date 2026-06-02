import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from tools.pdf_parser import parse_pdf
from main_crew import run_evaluation_crew, run_post_approval_crew

load_dotenv()

st.set_page_config(page_title="HireFlow: Agentic Recruitment Copilot", page_icon="🤖", layout="wide")

st.title("🤖 HireFlow: Agentic Recruitment Copilot")
st.markdown("Automate your recruitment pipeline from screening to scheduling using CrewAI.")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    
    st.info("Upload the Job Description and Resumes here.")
    jd_file = st.file_uploader("Upload Job Description (TXT or PDF)", type=["txt", "pdf"])
    resume_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if not os.environ.get("OPENAI_API_KEY"):
    st.warning("Please enter your OpenAI API Key in the sidebar to proceed.")
    st.stop()

if 'evaluation_result' not in st.session_state:
    st.session_state.evaluation_result = None

if jd_file and resume_files:
    if st.button("Start Screening Pipeline"):
        with st.spinner("Extracting text and analyzing candidates..."):
            # Parse JD
            jd_text = ""
            if jd_file.name.endswith(".pdf"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_jd:
                    tmp_jd.write(jd_file.getvalue())
                    tmp_jd_path = tmp_jd.name
                jd_text = parse_pdf(tmp_jd_path)
            else:
                jd_text = jd_file.getvalue().decode("utf-8")
            
            # Parse Resumes
            candidates_data = ""
            for resume in resume_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_res:
                    tmp_res.write(resume.getvalue())
                    tmp_res_path = tmp_res.name
                res_text = parse_pdf(tmp_res_path)
                candidates_data += f"\\n--- Candidate Resume: {resume.name} ---\\n{res_text}\\n"

            # Run Evaluation Crew
            result = run_evaluation_crew(jd_text, candidates_data)
            
            if hasattr(result, 'raw'):
                st.session_state.evaluation_result = result.raw
            else:
                st.session_state.evaluation_result = str(result)
            st.success("Screening Complete!")
            st.rerun()

if st.session_state.evaluation_result:
    st.header("📊 Shortlist & Ranking")
    st.markdown(st.session_state.evaluation_result)
    
    st.divider()
    st.header("⚠️ Human Approval Gate")
    st.markdown("Review the recommended candidates above. Proceed to schedule interviews and send emails?")
    
    candidate_to_approve = st.text_input("Enter the name and email of the candidate to approve (e.g., 'John Doe - john@example.com')")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Approve & Schedule", use_container_width=True):
            if not candidate_to_approve:
                st.error("Please enter candidate info.")
            else:
                with st.spinner(f"Scheduling interview and emailing {candidate_to_approve}..."):
                    post_result = run_post_approval_crew(candidate_to_approve)
                    if hasattr(post_result, 'raw'):
                        st.success(post_result.raw)
                    else:
                        st.success(str(post_result))
                    st.balloons()
    with col2:
        if st.button("❌ Reject List", use_container_width=True):
            st.session_state.evaluation_result = None
            st.warning("Candidate list rejected. Please upload new resumes.")
            st.rerun()
