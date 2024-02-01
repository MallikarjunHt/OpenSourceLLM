from dotenv import load_dotenv

import chainlit as chainlit
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain import PromptTemplate

load_dotenv()
model_id = "gpt2-medium"

con_model = HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature":0.8, "max_new_tokens":200})

prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a Amirican telling the storey about India and its culture: {question}"
)
str = "mysore in 1997"
chain = LLMChain(prompt=prompt, llm=con_model, verbose=True)

res = chain.run(str)
print(res)
