from debate_engine import Debate

def test_single_response_end_to_end():
    debate = Debate(
        topic="Should artificial intelligence replace most software developers?",
        user_position="Yes, AI should eventually replace most software developers.",
        agent_position="No, AI should not replace most software developers.",
        max_rounds=3,
    )

    print(f"Debate Status: {debate.status}")

    debate.start()

    print(f"Debate Status: {debate.status}")
    print(f"Round: {debate.round_number}")

    response = debate.respond(
        "AI can already write code faster than most humans."
    )

    print(f"\nAI: {response}")
    print(f"Debate Status: {debate.status}")
    print(f"Round: {debate.round_number}")


def test_round_limit():
    debate = Debate(
        topic="Should artificial intelligence replace most software developers?",
        user_position="Yes, AI should eventually replace most software developers.",
        agent_position="No, AI should not replace most software developers.",
        max_rounds=3,
    )

    debate.start()

    print(f"Debate Status: {debate.status}")
    print(f"Round: {debate.round_number}")

    arguments = [
        "AI can already write code faster than most humans.",
        "Companies care about cost, so they will prefer AI.",
        "AI can continue improving, so human developers may eventually become unnecessary.",
        "You can review AI generated code with other AI models.",
    ]

    for argument in arguments:
        print(f"\nYou: {argument}")

        response = debate.respond(argument)

        print(f"\nAI: {response}")
        print(f"\nRound: {debate.round_number}")
        print(f"Status: {debate.status}")


def test_no_response_when_debate_not_started():
    debate = Debate(
        topic="Should artificial intelligence replace most software developers?",
        user_position="Yes, AI should eventually replace most software developers.",
        agent_position="No, AI should not replace most software developers.",
        max_rounds=3,
    )

    response = debate.respond("AI can already write code faster than most humans.")


test_round_limit()