import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
_ = load_dotenv()
openai_model = ChatOpenAI(model="gpt-4o")
