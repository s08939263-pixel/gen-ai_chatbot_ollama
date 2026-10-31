from langchain_ollama import ChatOllama #class from package
model_name = "llama3.2:latest"
llm = ChatOllama(model=model_name)

response = llm.invoke("what is AI")
print(response.content)