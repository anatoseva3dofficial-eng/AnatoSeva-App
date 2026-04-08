import streamlit as st

st.set_page_config(page_title="AnatoSeva 3D", page_icon="🩺")

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔐 AnatoSeva Private Access")
    pwd = st.text_input("Master Key", type="password")
    if st.button("Unlock"):
        if pwd == "Robin@2026":
            st.session_state['auth'] = True
            st.rerun()
else:
    st.title("🚀 AnatoSeva 3D - Universal Hub")
    st.sidebar.write("Creator: Robin Kumar")
    option = st.selectbox("Select Mode", ["MBBS/Medical", "Class 1-12"])
    st.file_uploader(f"Upload {option} Content", type=['pdf', 'jpg', 'png'])
    if st.button("Generate Video"):
        st.success("Branding Applied: Robin Kumar. Rendering...")
