import streamlit as st
#from Home import Summary_Value

#st.title("Projects")
st.subheader( f"Summary of the RFP Document",divider='rainbow')
Summary_P= """ Combine the extracted information into a comprehensive summary that covers all key aspects of the RFP.  Consider the following while providing summary:

Provide Title of the RFP - it is generally the Header at the beginning of RFP document
Provide Synopsis / Solicitation number
Provide name of Issuing Agency - (include full name and do not use abbreviations)
Provide the Response deadline
Summary of Synopsis based on the RFP
List of Key requirements related to Technical aspects, pricing aspects and business aspects, and any other similar aspects
List out Additional information
List out Other important recommendations:

Furthermore, Ensure the summary is clear, concise, and accurately reflects the contents of the original document.
Include any additional insights or recommendations based on the RFP requirements.
"""
#Summary_V = st.session_state.get['new_variable1'] ,None
st.write(st.session_state.get('Summary' ,None))