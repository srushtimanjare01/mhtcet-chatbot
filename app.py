import streamlit as st


# Function to get answer from data file
def get_answer(question):
    try:
        with open("data.txt", "r") as f:
            data = f.readlines()
    except:
        return "Data file not found."

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


# Streamlit UI
st.title("MHT-CET Chatbot 🎓")

st.write("Ask any question related to MHT-CET!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input box
user_input = st.chat_input("Type your question here...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get
