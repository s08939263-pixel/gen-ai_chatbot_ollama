from langchain_ollama import ChatOllama 
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage("you are funny uncle in banglore"),
    HumanMessage("what is AI?")


]

model_name = "llama3.2:latest"
llm = ChatOllama(model=model_name)

response = llm.invoke(messages)
print(response.content)