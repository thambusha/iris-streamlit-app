import streamlit as st
from chat_agent import ask_chatbot  # uses the LangChain agent from before

st.set_page_config(page_title="Jaggu", page_icon="🎓")

st.title("🎓 Jaggu")
st.write("Ask me about contact details for any major university!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").write(content)

# User input
prompt = st.chat_input("Type your question here...")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get response from LangChain agent
    response = ask_chatbot(prompt)

    # Add response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
