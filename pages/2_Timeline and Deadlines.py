import streamlit as st
from src.GenAI import user_input

st.subheader( f"Deadlines,Timelines,Contact Information",divider='rainbow')
Deadlines = """  
Please provide the following information from the given RFP documentation:


1.Deadlines:
List all key deadlines mentioned in the RFP, including:
- Deadline / date for proposal submission.
- Deadline / date for Submission of solicitation 
- Deadline/ date  for submitting questions.

For each deadline, provide the specific date or timeline (e.g., "Proposal submission deadline: June 15, 2023").


2. Project Timelines:
   - Outline the overall project timeline as described in the RFP, including the anticipated duration of the project, key phases or milestones, and any specific timelines for deliverables or project stages like contract award, project start, and any other important milestones.


3. Contact Information:
   - Identify the primary points of contact for the RFP, including the name, title, email address, and phone number of the person(s) responsible for managing the RFP process.
4. Extract Info:
   - Give the Page Number Where you Extract This information So user can go through This DOcumnet 

Key Points:
- Carefully review the RFP document to extract the requested information.
- Provide the details in a clear and concise format, using bullet points or a table if appropriate.
- Ensure that all dates, timelines, and contact information are accurate and match the RFP documentation.
- Highlight any important or time-sensitive deadlines that require special attention.
"""

st.write(st.session_state.get('Deadline' ,None))

