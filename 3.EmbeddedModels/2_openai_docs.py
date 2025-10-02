from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=32)
documents = {
    "delhi is the caputa of india",
    "kolkaata is the inda" ,
    "paris is the caipatl "
}
result = embedding.embed_documents(documents)
print(str(result))
