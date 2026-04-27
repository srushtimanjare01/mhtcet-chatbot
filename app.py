import streamlit as st
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

# Prepare data
data = load_data()
questions = list(data.keys())
answers = list(data.values())

# AI-like response
def get_answer(user_input):
    user_input = user_input.lower()

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions + [user_input])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_match_index = similarity.argmax()

    if similarity[0][best_match_index] > 0.2:
        return answers[best_match_index]
    else:
        return "Sorry, I couldn't understand. Try asking differently."

# UI
st.set_page_config(page_title="MHT-CET AI Chatbot", page_icon="🎓")

st.title("MHT-CET AI Chatbot 🎓")
st.markdown("### Ask about eligibility, colleges, cutoffs, documents, etc.")

with st.sidebar:
    st.header("About")
    st.write("AI-like chatbot for MHT-CET students.")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# SINGLE INPUT (important)
user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = get_answer(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)st.title("MHT-CET Chatbot 🎓")
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
