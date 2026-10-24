import ollama

messages = [
    {
        "role":"system",
        "content":"you are a bengaluru auto driver."
    },
    {
        "role":"user",
        "content":"what is AI?"
    }
]
model_name = "llama3.2:latest"

response = ollama.chat(model = model_name,messages = messages)
print(response)