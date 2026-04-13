import streamlit as st
import time
import requests
import io
from PIL import Image

# --- 1. SETTINGS & BRANDING ---
st.set_page_config(page_title="AnatoSeva Global Video Factory", layout="wide", initial_sidebar_state="collapsed")

# --- 2. THE UI ENGINE (Clean & Professional) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    body {background-color: #010103; color: white;}
    .stTabs [data-baseweb="tab-list"] {gap: 10px;}
    .stTabs [data-baseweb="tab"] {background-color: #111; border-radius: 12px; color: #fff; padding: 10px 15px;}
    .stTabs [aria-selected="true"] {background-color: #00f3ff; color: #000; font-weight: bold;}
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; background-color: #00f3ff; color: black; font-weight: bold;}
    .reportview-container .main .block-container{ padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. IDENTITY ---
st.title("🛡️ AnatoSeva: Global Video Factory")
st.write(f"**Commander:** Robin Kumar | **Status:** V36.2 Ultra-Fast Ready")

tabs = st.tabs(["🎥 1-Click Video Maker", "🔬 Medical Logic", "📊 Mission Haridwar", "📺 Channel Control"])

# --- TAB 1: THE VIDEO ENGINE (सुपर-फास्ट तरीका) ---
with tabs[0]:
    st.header("🎬 Create Video (No Login & Ultra-Fast)")
    
    col_input, col_video = st.columns([1, 2])
    
    with col_input:
        st.subheader("1. Enter Topic")
        topic = st.text_input("Enter Topic (e.g., Human Heart 3D):", "Human Brain Anatomy")
        
        # This is the secret, pre-optimized prompt
        final_p = f"Hyper-realistic 3D cinematic animation of {topic}, 8k, medical accuracy, soft studio lighting, dark background, subtle motion."
        
        st.markdown("---")
        st.subheader("2. Start Engine")
        generate_btn = st.button("🚀 Generate 3D Video")

    with col_video:
        st.subheader("3. Video Output")
        
        if generate_btn:
            with st.spinner(f"Bhai ji, background mein AI engine chal raha hai... {topic} ki video ban rahi hai. Thoda sukoon rakhein..."):
                try:
                    # --- SECRET API CONNECTION (No Login Required) ---
                    # We are using a reliable API endpoint for Stable Video Diffusion
                    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-video-diffusion-img2vid-xt"
                    
                    # You don't need a token for small requests, but let's make it robust
                    headers = {} 
                    
                    # We need a base image first. Let's generate a quick one.
                    img_api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
                    img_response = requests.post(img_api_url, headers=headers, json={"inputs": final_p})
                    
                    if img_response.status_code == 200:
                        img_bytes = img_response.content
                        
                        # Now convert image to video
                        payload = {
                            "inputs": img_bytes,
                            "parameters": {
                                "fps": 6,
                                "motion_bucket_id": 127,
                                "noise_aug_strength": 0.02
                            }
                        }
                        
                        video_response = requests.post(API_URL, headers=headers, json=payload)
                        
                        if video_response.status_code == 200:
                            video_bytes = video_response.content
                            st.video(video_bytes)
                            st.success("🎉 Video taiyar hai, Commander! Neeche download karein.")
                            st.download_button(label="💾 Download Video", data=video_bytes, file_name=f"{topic}_3d.mp4", mime="video/mp4")
                        else:
                            st.error(f"Error: Video generation failed (Code: {video_response.status_code}). Server might be busy, please try again.")
                    else:
                        st.error(f"Error: Base image generation failed (Code: {img_response.status_code}).")
                        
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

# --- OTHER TABS (Same as before) ---
with tabs[1]:
    st.write("198 Medical Points Engine: **ONLINE**")
with tabs[2]:
    st.metric("Haridwar Mission Fund", "₹15.4 Cr", "+12% Growth")
with tabs[3]:
    st.write("Channel: **Anatoseva Global** | Target Audience: **USA / UK**")

st.sidebar.caption("AnatoSeva V36.2 | Ultra-Fast Edition")
