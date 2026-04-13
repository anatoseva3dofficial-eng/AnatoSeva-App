import streamlit as st
import streamlit.components.v1 as components

# --- 1. SETTINGS & BRANDING ---
st.set_page_config(page_title="AnatoSeva Global Video Hub", layout="wide", initial_sidebar_state="collapsed")

# --- 2. THE UI ENGINE (Clean & Professional) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    body {background-color: #010103; color: white;}
    .stTabs [data-baseweb="tab-list"] {gap: 10px;}
    .stTabs [data-baseweb="tab"] {background-color: #111; border-radius: 12px; color: #fff; padding: 10px 15px;}
    .stTabs [aria-selected="true"] {background-color: #00f3ff; color: #000; font-weight: bold;}
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; background-color: #00f3ff; color: black; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. IDENTITY ---
st.title("🛡️ AnatoSeva: Global Video Hub")
st.write(f"**Commander:** Robin Kumar | **Status:** AI Engine Ready")

tabs = st.tabs(["🎥 1-Click Video Maker", "🔬 Medical Logic", "📊 Mission Haridwar", "📺 Channel Control"])

# --- TAB 1: THE VIDEO ENGINE (भटकना बंद) ---
with tabs[0]:
    st.header("🎬 Create Video (No Login Required)")
    st.write("नीचे दी गई विंडो में अपना टॉपिक लिखें और रेंडर करें।")
    
    col_input, col_video = st.columns([1, 2])
    
    with col_input:
        st.subheader("1. Get Master Prompt")
        topic = st.text_input("Enter Topic (e.g., Human Heart 3D):", "Human Brain Anatomy")
        if st.button("Generate Final Prompt"):
            # This is the prompt you will copy and paste into the box on the right
            master_p = f"Cinematic 3D animation of {topic}, 8k, medical accuracy, professional lighting, dark background, rotating view."
            st.code(master_p)
            st.info("Bhai ji, upar wale prompt ko copy karein aur RIGHT SIDE wale box mein 'Prompt' ki jagah paste kar dein.")

    with col_video:
        st.subheader("2. Live AI Video Generator")
        # Direct Embed of a stable, free video AI space (No login required)
        components.iframe("https://multimodalart-stable-video-diffusion.hf.space", height=600, scrolling=True)

# --- TAB 2, 3, 4 (Logical Data) ---
with tabs[1]:
    st.write("198 Medical Points Engine: **ONLINE**")
with tabs[2]:
    st.metric("Haridwar Mission Fund", "₹15.4 Cr", "+12% Growth")
with tabs[3]:
    st.write("Channel: **Anatoseva Global** | Target Audience: **USA / UK**")

st.sidebar.caption("AnatoSeva V36.1 | No-Login Edition")
