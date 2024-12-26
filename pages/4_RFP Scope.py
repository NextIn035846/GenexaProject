import streamlit as st
from src.GenAI import user_input
#st.title("Projects")
st.subheader( f"Scope of RFP",divider='rainbow')
Scope = """
You are an expert in understanding the scope of a given RFP. Look for the scope of the RFP in entire document, especially look out for statement of work (SOW), which defines the scope of work or the scope of service(s) to be provided.  From the RFP, understand the tasks to be performed by the winning bidder and a timeline for providing deliverables. 
Based on the above understanding, please list out

- The Scope of the work in given RFP.
- What are the services to be provided by bidder for this RFP.
- What kind of tasks are to be performed by the bidder for this RFP.
- Extract and summarise the key deliverables
 - summarise other important scope related aspects from the RPF document .


Please present the extracted information in a clear and structured format."""


st.write(st.session_state.get('Scope' ,None))