import streamlit as st

from debate_engine import Debate

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
    if debate.status == "active":

        with st.form("debate_form", clear_on_submit=True):

            user_input = st.text_area(
                "Your argument",
                placeholder="Enter your argument...",
            )

            submitted = st.form_submit_button("Send Argument")

        if submitted:

            if not user_input.strip():
                st.warning("Please enter an argument.")
            else:
                with st.spinner("AI is thinking..."):
                    debate.respond(user_input)

                st.rerun()

    else:
        st.success("Debate complete!")

        if "result" not in st.session_state:
            with st.spinner("Judging the debate..."):
                st.session_state.result = debate.judge()

        result = st.session_state.result

        st.divider()

        st.subheader("Final Verdict")

        if result["winner"] == "user":
            st.success("Winner: You")
        elif result["winner"] == "agent":
            st.info("Winner: AI")
        else:
            st.warning("Result: Tie")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Your Score", result["user_score"])

        with col2:
            st.metric("AI Score", result["agent_score"])

        st.subheader("Your Performance")

        st.write("**Strengths**")
        for strength in result["user_strengths"]:
            st.write(f"- {strength}")

        st.write("**Weaknesses**")
        for weakness in result["user_weaknesses"]:
            st.write(f"- {weakness}")

        st.subheader("AI Performance")

        st.write("**Strengths**")
        for strength in result["agent_strengths"]:
            st.write(f"- {strength}")

        st.write("**Weaknesses**")
        for weakness in result["agent_weaknesses"]:
            st.write(f"- {weakness}")

        st.subheader("Summary")
        st.write(result["summary"])

        st.divider()

        if st.button("New Debate"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()