from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from pydantic.v1 import BaseModel, ConfigDict

os.environ['GOOGLE_API_KEY']="AIzaSyD7LudRAM2Y70wvmFCzJOuC36Ke3rue6P4"

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings,)
    vector_store.save_local("faiss_index")
    #return vector_store


def get_conversational_chain():

    prompt_template = """
    You are an AI assistant with advanced natural language processing and information extraction capabilities. Your task is to extract key details from a given RFP document and provide a structured summary of the most important information.
Present the extracted information in a clear and concise manner, organizing it into well-structured sections. Use markdown formatting for any code snippets or technical details. Ensure that the response provides a comprehensive overview of the RFP's key details to help the user effectively respond to the request.
Do not infer any data based on previous training, strictly use only source text given below as input.If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.2)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    print(prompt)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)
    
    return response["output_text"]