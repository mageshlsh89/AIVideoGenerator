import streamlit as st
import requests

st.set_page_config(page_title="AI Video Generator", layout="wide")
st.title("🎬 AI-Powered Video Generator")

# Step 1: Prompt Input and Script Generation
st.header("Step 1: Enter Prompt and Generate Script")
prompt = st.text_area("Enter your idea or line:")
language = st.selectbox("Selectt Language", ["English", "Tamil"])

import requests

import requests
import json


def generate_script_with_gemini(prompt, language):
    import requests

    API_KEY = st.secrets["gemini"]["api_key"] # Replace with your actual Gemini API key
    GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"Write a short video script in {language} for the following idea:\n{prompt}"}
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error communicating with Gemini: {e}"

if st.button("Generate Script"):
    if prompt:
        script = generate_script_with_gemini(prompt, language)
        st.text_area("Generated Script", value=script, height=300)
    else:
        st.warning("Please enter a prompt to generate the script.")

# Step 2: YouTube URL Input
st.header("Step 2: Upload Reference Video")
youtube_url = st.text_input("Enter YouTube URL:")
if st.button("Upload & Process"):
    st.info("Processing video...")
    st.text_area("Extracted Script", value="[Extracted script from video]", height=200)
    st.image("https://via.placeholder.com/400x200.png?text=Suggested+Video+Preview")

# Step 3: Voiceover Section
st.header("Step 3: Add Voiceover and Generate Video")
language = st.selectbox("Select Voiceover Language", ["Tamil", "English"])
if st.button("Generate Video with Voiceover"):
    st.success(f"Video generated with {language} voiceover!")
    st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
    st.download_button("Download 360p", "video_360p.mp4")
    st.download_button("Download 720p", "video_720p.mp4")
    st.download_button("Download HD", "video_hd.mp4")

# Step 4: Viral Tags
st.header("Step 4: Generate Viral Tags")
if st.button("Generate Tags"):
    st.write(["#AI", "#TamilShorts", "#Trending", "#StoryTime"])
if st.button("Add Tags"):
    st.success("Tags added to video metadata")

# Step 5: Thumbnail Creation
st.header("Step 5: Create Thumbnail")
if st.button("Create Thumbnail"):
    st.image("https://via.placeholder.com/300x200.png?text=Thumbnail+Preview")
if st.button("Add Thumbnail"):
    st.success("Thumbnail added to video")

# Step 6: Upload Section
st.header("Step 6: Upload to YouTube")
video_type = st.radio("Select Video Type", ["Shorts", "Long Video"])
schedule_time = st.time_input("Select Time to Upload")
if st.button("Publish - Public"):
    st.success("Video scheduled for upload")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
