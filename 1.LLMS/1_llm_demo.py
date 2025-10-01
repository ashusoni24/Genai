from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-oss-20b')  #object created of our model
results = llm.invoke("What is the capital of india")
print(results)