from langchain_ollama import ChatOllama #class from package
model_name = "llama3.2:latest"
temperature = [0, 0.5, 1.2]
for temp in temperature:
     llm = ChatOllama(model=model_name, model_kwargs={"temperature":temp}
     )

     response = llm.invoke ("what is AI?,give in one line")
     print(f"Temperature:{temp},output:{response.content}")