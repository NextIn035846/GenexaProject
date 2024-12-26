import streamlit as st
from src.GenAI import user_input
#st.title("Projects")
st.subheader( f"RFP Requirements",divider='rainbow')
Requirement = """ 1. Requirement Extraction:
   - List all the technical, functional, and non-functional , security requirements specified in the RFP.
   - Organize the requirements in a clear, concise format (e.g., a table or bullet points).
   - For each requirement, include a brief description, any specific details or constraints, and the priority level (e.g., mandatory, desirable).

2. Other Important Information:
   - Summarize any other key details from the RFP that the RFP response team should be aware of:
     - Project scope and objectives
     - Evaluation criteria and selection process
     - Budget or pricing guidelines
     - Contract terms and conditions

Present the extracted information in a clear, organized manner, using appropriate headings, bullet points, and formatting to make it easy for the client to understand and reference."""


st.write(st.session_state.get('Requirements' ,None))