import os
from apikey import apikey

import streamlit as st
from langchain.llms import openai

os.environ['OPENAI_API_KEY'] = apikey

# app framework
st.title('chatgpt for testing..')
prompt = st.text_input('your prompt..')

#llms
llm = openai.OpenAI(temperature=0.9)

if prompt:
    response=llm(prompt)
    st.write(response)