import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Assistant")
st.write("Ask me anything!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Display user's message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Call your Render API
    API_URL = st.secrets["API_URL"]

    try:
        response = requests.post(
            API_URL,
            json={
                "message": user_input
            }
        )

        response.raise_for_status()

        data = response.json()

        # We will adjust this depending on your API response
        assistant_response = data["response"]

    except Exception as e:
        assistant_response = f"Error: {e}"

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(assistant_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_response
    })