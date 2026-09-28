import streamlit as st

from debate_engine import Debate

if "ai_thinking" not in st.session_state:
    st.session_state.ai_thinking = False

if "pending_user_input" not in st.session_state:
    st.session_state.pending_user_input = None

st.title("AI Debate Agent")

# --------------------------------------------------
# Debate Setup
# --------------------------------------------------

if not st.session_state.get("debate_started", False):

    st.subheader("Debate Setup")

    topic = st.text_input(
        "Topic",
        placeholder="e.g. Should AI replace most software developers?",
    )

    user_position = st.text_area(
        "Your position",
        placeholder="Explain the position you will defend...",
    )

    agent_position = st.text_area(
        "AI's opposing position",
        placeholder="Explain the position the AI will defend...",
    )

    max_rounds = st.number_input(
        "Number of rounds",
        min_value=1,
        value=5,
        step=1,
    )

    if st.button("Start Debate"):
        if not topic.strip():
            st.error("Please enter a topic.")
        elif not user_position.strip():
            st.error("Please enter your position.")
        elif not agent_position.strip():
            st.error("Please enter the AI's position.")
        else:
            debate = Debate(
                topic=topic,
                user_position=user_position,
                agent_position=agent_position,
                max_rounds=max_rounds,
            )

            debate.start()

            st.session_state.debate = debate
            st.session_state.debate_started = True
            st.session_state.ai_thinking = False
            st.session_state.pending_user_input = None

            st.rerun()


# --------------------------------------------------
# Debate
# --------------------------------------------------

else:

    debate = st.session_state.debate

    st.subheader("Debate")

    st.write(f"**Topic:** {debate.topic}")
    st.write(f"**Your position:** {debate.user_position}")
    st.write(f"**AI's position:** {debate.agent_position}")

    st.divider()

    # Display previous messages
    for message in debate.messages:

        if message["role"] == "user":
            with st.chat_message("user"):
                st.write(message["content"])

        elif message["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(message["content"])

    # User input
    if debate.status == "active" and not st.session_state.ai_thinking:

        user_input = st.chat_input(
            "Enter your argument..."
        )

        if user_input:

            st.session_state.pending_user_input = user_input
            st.session_state.ai_thinking = True
            st.rerun()

    elif debate.status == "active" and st.session_state.ai_thinking:
        
        with st.spinner("AI is thinking..."):
            response = debate.respond(
                st.session_state.pending_user_input
            )

        st.session_state.pending_user_input = None
        st.session_state.ai_thinking = False
        st.rerun()

    else:
        st.success("Debate complete!")

        if st.button("Show Final Verdict"):
            result = debate.judge()
            st.session_state.result = result