from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
#chat tempelate
chat_tempelate = ChatPromptTemplate({
    ('system' , 'You are a helpful costem support agent'),
    MessagesPlaceholder(variable_name='chat_history'), #to get full context 
    ('human' , '{query}') #user enters the new prompt next day so to get full context we use message placehodler
}) 
#load chat history
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extent(f.readlines())
print(chat_history)

#create prompt
prompt = chat_tempelate.invoke({'chat_history' : chat_history , 'query' :'where is my resfund' })
print(prompt)