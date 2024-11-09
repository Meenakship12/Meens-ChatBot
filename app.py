import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Streamlit app setup
st.title("GPT Chat Interface")
st.subheader("Chat with GPT-3")

# Initialize session state for storing conversation history if it doesn't already exist
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Display chat history
for message in st.session_state['messages']:
    if message['role'] == 'user':
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**GPT-3:** {message['content']}")

# Input for user query
user_input = st.text_input("Enter your message:", "")

# Handle user input and get response from OpenAI
if st.button("Send") and user_input:
    # Add user message to the session state
    st.session_state['messages'].append({"role": "user", "content": user_input})

    # Call OpenAI's API to get GPT response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available and preferred
        messages=st.session_state['messages']
    )

    # Extract the response content
    gpt_response = response['choices'][0]['message']['content']

    # Add GPT response to the session state
    st.session_state['messages'].append({"role": "assistant", "content": gpt_response})

    # Display the GPT response
    st.markdown(f"**GPT-3:** {gpt_response}")

# Provide information about API key handling
st.caption("Make sure to set your OpenAI API key securely.")
