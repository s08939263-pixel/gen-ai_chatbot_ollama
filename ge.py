import ollama
model_name = "llama3.2:latest"

response = ollama.generate(model = model_name,
 prompt = "explain how ai works in three line")
print(response.response)