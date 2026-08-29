from ollama import chat, ChatResponse
from prompts import DEBATE_SYSTEM_PROMPT

topic = "Should artificial intelligence replace most software developers?"

user_position = "Yes, AI should eventually replace most software developers."

agent_position = "No, AI should not replace most software developers."

system_prompt = DEBATE_SYSTEM_PROMPT.format(
    topic=topic,
    user_position=user_position,
    agent_position=agent_position,
)

messages = [{
    "role": "system",
    "content": system_prompt,
}]

while True:
    try:
        user_input = input("\nYou: ")
    except EOFError:
        print("\nInput stream closed. Exiting debate.")
        break

    if not user_input.strip():
        print("Please enter an argument.")
        continue

    if user_input.lower() == "quit":
        break

    messages.append({
        "role": "user",
        "content": user_input,
    })

    response: ChatResponse = chat(
        model="llama3.1",
        messages=messages,
    )

    agent_response = response.message.content

    messages.append({
        "role": "assistant",
        "content": agent_response,
    })

    print(f"\nAI: {agent_response}")