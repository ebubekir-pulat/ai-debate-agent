from debate_engine import Debate

def main():
    print("=" * 40)
    print("        AI DEBATE AGENT")
    print("=" * 40)

    topic = input("\nTopic: ").strip()
    user_position = input("Your position: ").strip()
    agent_position = input("AI's opposing position: ").strip()

    rounds_input = input("Number of rounds (Press Enter for 5): ").strip()

    if rounds_input:
        max_rounds = int(rounds_input)
    else:
        max_rounds = 5

    debate = Debate(
        topic=topic,
        user_position=user_position,
        agent_position=agent_position,
        max_rounds=max_rounds,
    )

    debate.start()

    print("\nDebate started!")
    print(f"AI will argue: {agent_position}")
    print(f"Rounds: {max_rounds}")

    while debate.status == "active":
        print(f"\n--- Round {debate.round_number + 1} / {max_rounds} ---")

        try:
            user_input = input("\nYou: ")
        except EOFError:
            print("\nInput stream closed. Exiting.")
            break

        if not user_input.strip():
            print("Please enter an argument.")
            continue

        if user_input.lower() == "quit":
            print("Debate ended.")
            break

        response = debate.respond(user_input)

        print(f"\nAI: {response}")

    if debate.status == "finished":
        print("\nDebate complete!")
        print("Judging the debate...")

        result = debate.judge()

        print("\n=== FINAL VERDICT ===")
        print(f"Winner: {result['winner']}")
        print(f"Your score: {result['user_score']}")
        print(f"AI score: {result['agent_score']}")
        print(f"\nSummary: {result['summary']}")

    
if __name__ == "__main__":
    main()