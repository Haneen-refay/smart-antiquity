import streamlit as st
from google import genai
from PIL import Image

# 1. Setup Gemini API
# ⚠️ Make sure to put your real API Key here between the quotes ""
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)
# 2. Page Configuration
st.set_page_config(page_title="Antiquity Explorer", page_icon="🏛️", layout="centered")

# Website Title & Description
st.title("🏛️ Smart Antiquity Explorer")
st.write("Upload a photo of any historical landmark or antiquity, and get instant information about it!")

# Image Uploader
uploaded_file = st.file_uploader("Choose an image (JPG, JPEG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    st.write("---")
    
    # Analyze Button
    if st.button("Identify Landmark 🔍"):
        with st.spinner("Analyzing the image and fetching historical data..."):
            try:
                # The prompt is now in English to get the response in English
                prompt = (
                    "Identify this historical monument, landmark, or antiquity from the image accurately. "
                    "Provide its name, current location, historical era/date of construction, "
                    "its historical significance, and a brief interesting story about it. "
                    "Format the response beautifully in clear English using bullet points and headings."
                )
                
                # Send request to Gemini
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image, prompt]
                )
                
                # Display the results
                st.success("Successfully Identified!")
                st.subheader("📋 Historical Information:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
