from bs4 import BeautifulSoup
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.environ['GROQ_API_KEY']

if "vector" not in st.session_state:
    st.info("Setting up vector store for the first time... (this takes ~60-90 seconds)")
    st.session_state.embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    st.session_state.loader = WebBaseLoader([
        "https://docs.langchain.com/langsmith/observability",
        "https://docs.langchain.com/langsmith/observability-quickstart",
        "https://docs.smith.langchain.com/tracing"
    ])
    
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs) 
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
    st.session_state.vector = True 
    st.success("Vector store ready!")

st.title("ChatGroq Demo")
llm = ChatGroq(groq_api_key=groq_api_key, 
               model_name="llama-3.3-70b-versatile",
               temperature=0.2 
               )

prompt = ChatPromptTemplate.from_template("""
You are a LangSmith expert. Answer ONLY using the exact information from context.

CRITICAL RULES - NEVER BREAK THESE:
- Use numbered list for steps
- ANY environment variable or command MUST be shown exactly as it appears in context
- Put ALL code/commands in ```bash block
- Never make up commands
- If exact command is in context, show it exactly

Context:
{context}

Question: {input}

Give answer in clean Markdown:
""")


document_chain = create_stuff_documents_chain(llm, prompt)  
retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 8})
retrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt=st.text_input("Input you prompt here")

if prompt:
    start=time.process_time()
    response=retrieval_chain.invoke({"input":prompt})
    print("Response time :",time.process_time()-start)
    st.write(response['answer'])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            clean_content = BeautifulSoup(doc.page_content, "html.parser").get_text(separator=" ", strip=True)
            st.write(f"**Doc {i+1}:**")
            st.write(clean_content[:500] + "..." if len(clean_content) > 500 else clean_content)  
            st.write("--------------------------------")
    