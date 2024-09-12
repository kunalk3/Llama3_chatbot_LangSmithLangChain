## -- Importing library -- ##
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
# from langchain_openai import ChatOpenAI                    # For GPT env
import streamlit as st
import os
from dotenv import load_dotenv

## -- Load API credentials env -- ##
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"                  # LangSmith tracking
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") # For GPT env
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"

## -- Prompt template -- ##
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title('Chatbot Using Langchain: LLAMA3')
input_text = st.text_input("Enter your prompt (user):")

## -- LLM: Llama3 -- ## 
llm = Ollama(model="llama3")                                 # ChatOpenAI(model="gpt-3.5-turbo") 3 For GPT env

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))