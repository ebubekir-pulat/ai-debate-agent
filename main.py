from debate_engine import Debate

def main():
    print("=" * 40)
    print("        AI DEBATE AGENT")
    print("=" * 40)

    # Get Topic
    while True:
        topic = input("\nTopic: ").strip()

        if topic:
            break

        print("Topic cannot be empty.")

    # Get User Position
    while True:
        user_position = input("Your position: ").strip()
        
        if user_position:
            break
        
        print("Your position cannot be empty.")

    # Get Agent's Position
    while True:
        agent_position = input("AI's opposing position: ").strip()

        if agent_position:
            break

        print("AI's position cannot be empty.")

    # Get Number of Rounds
    while True:
        rounds_input = input("Number of rounds (Press Enter for 5): ").strip()

        if not rounds_input:
            max_rounds = 5
            break
        
        try:
            max_rounds = int(rounds_input)

            if max_rounds < 1:
                print("Please enter a number greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

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