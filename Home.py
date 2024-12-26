import streamlit as st
from src.GenAI import get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain,user_input
from src.utils.load_config import LoadConfig

Values_P = LoadConfig()
def main():
    #st.set_page_config(page_title="Automating RFP Analysis")  
    
    st.markdown(
        """
        <div style="text-align:center;">
        <h1> RFP Analysis</h1>
        <h3>Automated Feature Extraction & Document Template Generation</h3>
        <p> Our project automates the process of analyzing Request for Proposals (RFPs) by
          extracting essential features and generating document templates. 
          By leveraging advanced models, we streamline the tedious task of identifying key elements from RFPs, 
          enabling efficient proposal preparation. ✨</p>
        </div>

    """,
    unsafe_allow_html=True,
    )

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None

    st.subheader("Upload your Documents")
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
                 st.session_state['dictionary'] = {}
                 raw_text = get_pdf_text(pdf_docs)
                 text_chunks = get_text_chunks(raw_text)
                 get_vector_store(text_chunks)
                 Summary_Value = user_input(Values_P.Summary)
                 st.session_state['Summary'] = Summary_Value
                 Dedline =user_input(Values_P.Dedline)
                 st.session_state['Deadline'] = Dedline
                 Requirements = user_input(Values_P.Requirements)
                 st.session_state['Requirements']= Requirements
                 Scope = user_input(Values_P.Scope)
                 st.session_state['Scope'] = Scope
                 Sections= user_input(Values_P.Sections)
                 st.session_state['Sections'] = Sections
                 Formating= user_input(Values_P.Formating)
                 st.session_state['Formating'] = Formating

                
                 st.success("Done")


if __name__ == "__main__":
     main()
