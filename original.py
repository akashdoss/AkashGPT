import streamlit as st
import requests
import io
from PIL import Image
import google.generativeai as genai

# Set page configuration with title, icon, and layout
st.set_page_config(page_title="Akash's AI Features", page_icon="🤖", layout="wide")

# Configure the API key for the chatbot
genai.configure(api_key="AIzaSyDXMaMzAsrNZNX5zv2onAZ7PthYejKumWc")

# Add a sidebar with additional information and navigation
st.sidebar.title("🤖 Akash's AI Features")

# Chatbot features at the top of the sidebar
st.sidebar.markdown("""
### Chatbot Features:
- AI-powered natural language responses
- Instant and accurate answers
- Optimized for desktop, tablet, and mobile experiences.
""")
st.sidebar.markdown("---")

# Sidebar navigation for features
option = st.sidebar.selectbox("Choose a feature:", ["Chatbot", "Image Generation"])

# Connect link at the bottom
st.sidebar.info("### 🔗 [Connect](https://www.linkedin.com/in/akash-selvadoss-n-542765252/)")
st.sidebar.markdown("---")

# Chatbot Feature
if option == "Chatbot":
    # Main page title and description for the chatbot
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

# Image Generation Feature
elif option == "Image Generation":
    st.title("🖼️ Image Generation")
    
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    prompt = st.text_input("Enter the prompt:")
    
    if st.button("Generate Image"):
        if prompt:
            image_bytes = query({"inputs": prompt})
            # Open the image with PIL
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
        else:
            st.warning("Please enter a prompt!")

# Add a section for FAQs to assist users
st.markdown("---")
st.header("💡 Frequently Asked Questions (FAQs)")
with st.expander("What can I ask this chatbot?"):
    st.write("You can ask the chatbot questions about various topics, including technology, AI concepts, general knowledge, and educational content. It is designed to provide information and insights based on your queries.")
with st.expander("How does this chatbot work?"):
    st.write("The chatbot leverages the capabilities of the Gemini GPT model, which uses advanced natural language processing techniques. It analyzes your questions and generates coherent and contextually relevant responses in real-time.")
with st.expander("Can I get personalized advice?"):
    st.write("While the chatbot can provide general advice and information, it is not a substitute for professional guidance. For personalized advice in areas like healthcare, finance, or legal matters, please consult a qualified expert.")
