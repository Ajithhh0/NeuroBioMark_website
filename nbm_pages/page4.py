import streamlit as st
from PIL import Image
import base64

def render():

    # Background image
    with open("Resources/brainbg.jpg", "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    st.markdown(f"""
    <style>
    html, body, .stApp {{
        background-color: black !important;
    }}
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: 70% auto;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Page 4")
    st.write("This is page 4 content.")
