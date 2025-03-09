import streamlit as st
from src.Services.Agent_Service import AgentService

# Initialize the AI Agent
agent_service = AgentService()

# Streamlit UI
st.set_page_config(page_title="AI AgenticScholar", layout="centered")

# App Title
st.title("🤖 AI AgenticScholar")

# Description
st.markdown("🚀 **Find the latest articles on Agentic AI**")
st.write("Enter your query below, and I'll fetch the top 5 articles related to Agentic AI.")

# Input Field for User Query
query = st.text_input("🔍 Enter your query:", "")

# Button to Submit the Query
if st.button("Ask AI 🤖"):
    if query:
        with st.spinner("🔎 Searching for the best articles on Agentic AI..."):
            response = agent_service.handle_query(query)

        # Display AI Response
        st.success("✅ AI Response:")
        if isinstance(response, list):
            for idx, article in enumerate(response):
                st.markdown(f"**{idx+1}. [{article['title']}]({article['link']})**")
        else:
            st.warning(response)  # If there's an error
    else:
        st.warning("⚠️ Please enter a query before submitting.")

# Chat History (Maintains Conversation)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if query:
    # Ensure response is initialized to prevent NameError
    response = agent_service.handle_query(query)

    # Append user query & AI response to chat history
    st.session_state.chat_history.append(("🧑‍💻 You", query))
    st.session_state.chat_history.append(("🤖 AI", response))
else:
    st.warning("⚠️ Please enter a query before submitting.")


# Display Chat History
st.subheader("💬 Chat History")
for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")

# Run with: streamlit run app.py
