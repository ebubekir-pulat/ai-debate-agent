import json

from ollama import chat, ChatResponse

JUDGE_SYSTEM_PROMPT = """
You are an impartial debate judge.

You will be given a complete debate transcript.

Evaluate the debate based on the quality of the arguments, not on whether
you personally agree with the topic or either position.

Evaluate both sides on:

1. Argument quality
2. Rebuttal quality
3. Evidence and reasoning
4. Consistency
5. Persuasiveness

Give each side a score from 0 to 100.

Do not reward a side merely for having the final response.

Do not invent facts or evidence that were not present in the debate.

Return ONLY valid JSON using exactly this structure:

{
    "winner": "user" or "agent" or "tie",
    "user_score": integer,
    "agent_score": integer,
    "user_strengths": ["string"],
    "user_weaknesses": ["string"],
    "agent_strengths": ["string"],
    "agent_weaknesses": ["string"],
    "summary": "string"
}
"""

def judge_debate(messages):
    transcript = "\n\n".join(
        f"{message['role'].upper()}: {message["content"]}"
        for message in messages
        if message["role"] != "system"
    )

    response: ChatResponse = chat(
            model="llama3.1",
            messages=[
                {
                    "role": "system",
                    "content": JUDGE_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""
Here is the complete debate transcript:

{transcript}

Evaluate the debate and return your verdict as JSON. 
""",
                },
            ],
    )

    result = json.loads(response.message.content)

    if result["winner"] == "assistant":
        result["winner"] = "agent"

    return result