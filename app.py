import streamlit as st

st.title("AI Debate Agent")

st.subheader("Debate setup")

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
        st.success("Debate configuration is valid!")
