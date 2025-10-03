from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

st.header('Research Tool')
user_input = st.text_input('Enter your prompt')

if st.button('Summarizer'):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)
