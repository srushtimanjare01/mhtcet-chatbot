import streamlit as st
import json

# Function to get answer from JSON
def get_answer(question):
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        return "Error: data.json not found."

    question = question.lower()

    best_match = ""
    max_score = 0

    for key, value in data.items():
        key = key.lower()
        value_lower = value.lower()

        # Calculate matching score
        score = 0
        for word in question.split():
            if word in key or word in value_lower:
                score += 1

        # Select best match
        if score > max_score:
            max_score = score
            best_match = value

    if max_score > 0:
        return best_match
    else:
        return "Sorry, I don't have information about that yet."


# Streamlit UI
st.set_page_config(page_title="MHT-CET Chatbot", page_icon="🎓")

st.title("MHT-CET Chatbot 🎓")
st.markdown("### Ask about eligibility, colleges, cutoffs, documents, etc.")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("This chatbot helps MHT-CET students with common queries.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Ask your question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get bot response
    response = get_answer(user_input)

    # Show bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
