import ollama
messages = [
    {
        "role":"system",#dictionary
        "content": "you are a freindly assistant."#tells how to behave
    }
]
while True:# to take real time questions,infinite loop repeats the block of code,by this you can ask multiple questions
    user_prompt = input("you: ")
    if user_prompt == "bye":
        break
    user_role = {
        "role":"user",
         "content":user_prompt}
    messages.append(user_role)#to send conversation history to ai,help the model answer to follow up questions
    model_name = "llama3.2:latest"
    response = ollama.chat(model= model_name,messages = messages)
    #ollama.chat request to response from the selected model
    response = response.message.content
    # to remove meta data
    print("assistant :",response)
    assistant_role = {
            "role":"assistant",#to save ai reply in history
             "content":response}
    messages.append(assistant_role)

