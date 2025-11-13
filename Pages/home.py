import streamlit as st
from PIL import Image

st.set_page_config(page_title="NeuroBioMark", layout="wide")

# ---- REMOVE ALL TOP SPACE ----
st.markdown("""
    <style>
        header {visibility: hidden;}  /* Hide Streamlit default top bar */

        .block-container {
            padding-top: 0rem !important;
            margin-top: -3rem !important; /* Move everything up */
        }

        div.stButton > button {
            border: none;
            background-color: transparent;
            color: #0a58ca;
            font-size: 17px;
            padding: 6px 12px;
            cursor: pointer;
        }
        div.stButton > button:hover {
            color: #084298;
            background-color: rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)


# -------- NAVBAR ----------
def navbar():
    col_logo, col_btns = st.columns([1.2, 6])

    with col_logo:
        logo = Image.open("Resources/NBMLogoNobg.png")
        st.image(logo, width=150)

    with col_btns:
        b1, b2, b3, b4 = st.columns(4)

        # Keep buttons aligned with logo
        spacer = 2
        for _ in range(spacer):
            b1.write("")
            b2.write("")
            b3.write("")
            b4.write("")

        b1.button("Button 1")
        b2.button("Button 2")
        b3.button("Button 3")
        b4.button("Button 4")


navbar()


# -------- CONTENT ----------
st.title("NeuroBioMark")

st.write("""
Welcome to NeuroBioMark, your comprehensive platform for exploring the intersection 
of neuroscience and biometrics.

Our mission is to provide researchers, clinicians, and enthusiasts with the latest 
insights, tools, and resources to advance the understanding of neurological biomarkers 
and their applications in diagnosis, treatment, and research.
""")
