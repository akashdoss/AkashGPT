import streamlit as st
import google.generativeai as genai

# Set page configuration with title, icon, and layout
st.set_page_config(page_title="Akash's GPT Chatbot", page_icon="🤖", layout="wide")

# Configure the API key
genai.configure(api_key="AIzaSyDXMaMzAsrNZNX5zv2onAZ7PthYejKumWc")

# Add a sidebar with additional information and navigation
st.sidebar.title("🤖 Akash's GPT Chatbot")
 # Add your logo here
st.sidebar.markdown("""
### Chatbot Features:
- AI-powered natural language responses
- Instant and accurate answers
- Optimized for desktop, tablet, and mobile experiences.
""")
st.sidebar.markdown("---")
st.sidebar.info("### 🔗 [Connect](https://www.linkedin.com/in/akash-selvadoss-n-542765252/)")
st.sidebar.markdown("---")

# Main page title and description
st.title("Welcome to Akash's GPT Chatbot")
st.markdown("""
### 🤖 Ask any question, and get instant AI-powered answers!
This chatbot is powered by **Gemini GPT** to provide smart responses in real-time.
""")

# Input area for the user's question
text = st.text_area("Enter Your Question Here", height=150, placeholder="Type your question...")

# Progress bar to simulate the response processing
progress_bar = st.progress(0)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Trigger the response if there's input and the button is clicked
if st.button("💬 Get Response"):
    if text:
        progress_bar.progress(50)  # Simulate loading
        response = chat.send_message(text)
        progress_bar.progress(100)  # Complete loading
        
        # Display the response directly below the question input
        st.write(response.text)
    else:
        st.warning("Please enter a question!")

# Add a section for FAQs to assist users
st.markdown("---")
st.header("💡 Frequently Asked Questions (FAQs)")
with st.expander("What can I ask this chatbot?"):
    st.write("You can ask about any topic related to AI, technology, healthcare, education, or general knowledge.")
with st.expander("How does this chatbot work?"):
    st.write("The chatbot is powered by Gemini GPT, which generates responses based on the input question. It uses natural language processing to provide relevant answers.")
with st.expander("Can I get personalized advice?"):
    st.write("While the chatbot can give general advice, it is not intended for personalized medical, financial, or legal advice.")
