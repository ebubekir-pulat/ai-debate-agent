from ollama import chat, ChatResponse

response: ChatResponse = chat(
    model="llama3.1",
    messages=[
        {
            "role": "user",
            "content": "Give me one short argument for why software developers are still valuable in the age of AI."
        }
    ],
)

print(response.message.content)