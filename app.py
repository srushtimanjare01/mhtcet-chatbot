import streamlit as st

# Function to get answer
def get_answer(question):
    try:
        with open("data.txt", "r") as f:
            data = f.readlines()
    except:
        return "Error: data.txt not found"

    question = question.lower()

    best_match = ""
    max_score = 0

    for line in data:
        line_lower = line.lower()
        score = sum(1 for word in question.split() if word in line_lower)

        if score > max_score:
            max_score = score
            best_match = line.strip()

    if max_score > 0:
        return best_match
    else:
        return "Sorry, I don't have information about that yet."


# UI
st.title("MHT-CET Chatbot 🎓")
st.write("Ask anything about MHT-CET")

# Debug
st.write("DEBUG: App is running")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    st.write("DEBUG: Question received:", user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    reply = get_answer(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
