import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
llm = ChatOpenAI(openai_api_key = OPEN_API_KEY, model = "gpt-4")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
print(chain.invoke({"topic" : "icecream" }))



