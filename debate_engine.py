from ollama import chat, ChatResponse

from prompts import DEBATE_SYSTEM_PROMPT
from judge import judge_debate

class Debate:
    def __init__(
        self,
        topic,
        user_position,
        agent_position,
        max_rounds=5,
    ):
        self.topic = topic
        self.user_position = user_position
        self.agent_position = agent_position
        self.max_rounds = max_rounds

        self.round_number = 0
        self.status = "not_started"

        self.messages = [
            {
                "role": "system",
                "content": DEBATE_SYSTEM_PROMPT.format(
                    topic=topic,
                    user_position=user_position,
                    agent_position=agent_position,
                ),
            }
        ]

    def start(self):
        self.status = "active"

    def respond(self, user_input):
        if self.status != "active":
            raise RuntimeError("The debate is not active.")

        if not user_input.strip():
            raise ValueError("User input cannot be empty.")

        self.messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response: ChatResponse = chat(
            model="llama3.1",
            messages=self.messages,
        )

        agent_response = response.message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": agent_response,
            }
        )

        self.round_number += 1

        if self.round_number >= self.max_rounds:
            self.status = "finished"

        return agent_response

    
    def judge(self):
        if self.status != "finished":
            raise RuntimeError("The debate is not finished.")

        return judge_debate(self.messages)