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

response: ChatResponse = chat(
    model="llama3.1",
    messages=[
        {
            "role": "system",
            "content": system_prompt, 
        },
        {
            "role": "user",
            "content": """
            AI can already write production-quality code,
            debug programs, explain technical concepts, and
            work continuously without getting tired.

            Why would companies continue paying large numbers
            of software developers when AI can do much of their work?
            """,
        },
    ],
) 

print(response.message.content)