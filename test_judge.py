from judge import judge_debate

messages = [
    {
        "role": "user",
        "content": "AI can write code faster than humans, so developers are unnecessary.",
    },
    {
        "role": "assistant",
        "content": "Writing code is only part of software development. Developers also make architectural decisions, understand business requirements, and manage complex trade-offs.",
    },
    {
        "role": "user",
        "content": "But AI can learn those things too, so this may only delay replacement.",
    },
    {
        "role": "assistant",
        "content": "That's possible in principle, but it doesn't establish that replacement is inevitable. The question is whether AI can reliably take responsibility for ambiguous real-world decisions, not simply whether it can perform more technical tasks.",
    },
]

result = judge_debate(messages)

print(result)