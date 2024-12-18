import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv  # For loading environment variables
import google.generativeai as genai  # Google Generative AI SDK

# Load environment variables
load_dotenv()

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")
genai.configure(api_key=api_key)

# Function to get Gemini response
def get_gemini_response(input_text, image_parts, prompt):
    """
    Generate a response using Google Gemini model.
    """
    # Load the correct Gemini model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Correct model name
    response = model.generate_content([input_text, image_parts, prompt])
    return response.text

# Function to set up the uploaded image for Gemini
def input_image_setup(uploaded_file):
    """
    Prepare the uploaded image for processing.
    """
    if uploaded_file is not None:
        # Convert the uploaded image to bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = {
            "mime_type": uploaded_file.type,  
            "data": bytes_data
        }
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit app setup
st.header("Gemini Diet Planner 🍎🥦🥛")

# Input for text prompt
input_text = st.text_input("Enter Prompt: ", key="input")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_display = None

if uploaded_file is not None:
    # Display the uploaded image
    image_display = Image.open(uploaded_file)
    st.image(image_display, caption="Uploaded Image", use_container_width=True)

# Submit button
submit = st.button("Explain the image to me 👇")

# Instruction prompt
input_prompt = """
You are an expert GYM trainer tasked with analyzing the daily diet from the image.
Your task is to provide answers based on the diet chart in the following format:

1. How many items should the person take?
2. How much of each item should the person take?
----
----
"""

# Logic for processing when submit is clicked
if submit:
    if uploaded_file:
        try:
            # Prepare image data for the API
            image_data = input_image_setup(uploaded_file)
            # Get response from Gemini API
            response = get_gemini_response(input_text, image_data, input_prompt)
            st.subheader("Here is the Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload an image before submitting.")
