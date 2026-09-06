from debate_engine import Debate

debate = Debate(
    topic="Should artificial intelligence replace most software developers?",
    user_position="Yes, AI should eventually replace most software developers.",
    agent_position="No, AI should not replace most software developers.",
    max_rounds=2,
)

debate.start()

print("Round 1")
print("AI:", debate.respond(
    "AI can already write a large amount of production code, so human developers are unnecessary."
))

print("\nRound 2")
print("AI:", debate.respond(
    "AI is improving rapidly, and it can also review and improve its own code."
))

print("\nStatus:", debate.status)

result = debate.judge()

print("\n*** FINAL VERDICT ***")
print("Winner:", result["winner"])
print("User score:", result["user_score"])
print("Agent score:", result["agent_score"])
print("Summary:", result["summary"])