import streamlit as st
from src.GenAI import user_input
#st.title("Projects")
st.subheader( f"Sections to be included in RFP Response",divider='rainbow')
Sections = """ You are an expert in crafting RFP response documents. I need your help in extracting the relevant sections that should be included in an RFP response for this given RFP needs
Your task is to search the entire given RFP document based on following aspects:
-Various sections and volumes provided in the RFP document
-Requirements and scope of the given RFP
-Evaluation and submission criterion of the RFP document
Once this is done, list out the sections to be included in the RFP response as per instructions below
Submission Requirements / Sections to be included:
Identify and list all the elements and information that the proposal submission must contain, such as:
  - Proposal format and structure
  - Required sections based on RFP needs (e.g., executive summary, technical approach, Company Overview, project plan, team qualifications)
  - Any supporting documents or attachments required

Also, provide a brief description and concise 1-2 paragraph summary of each of the sections that are to be responded to in the RFP strictly based on the RFP needs, RFP evaluation criteria and other relevant information in the RFP. Do not include any generic content

"""
st.write(st.session_state.get('Sections' ,None))