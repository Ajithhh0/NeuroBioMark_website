import streamlit as st
from PIL import Image

st.set_page_config(page_title="NeuroBioMark", layout="wide")

# ------------------------------------------------------
# CSS (minimal + gradient only)
# ------------------------------------------------------
st.markdown("""
<style>

    /* Remove header + top padding */
    header {visibility: hidden;}
    .block-container {padding-top: 0 !important;}

    /* Inverted Gradient Background (Cyan → Navy) */
    .stApp {
        background: linear-gradient(180deg, #0CCDD6, #0E1B3A);
    }

    /* Borderless nav buttons */
    .nav-btn button {
        background: transparent !important;
        border: none !important;
        color: white !important;
        font-size: 16px !important;
        padding: 6px 14px !important;
        cursor: pointer;
    }

    .nav-btn button:hover {
        color: #002d6b !important;  /* darker blue hover */
    }

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------
# LOGO + BUTTONS (NO NAVBAR)
# ------------------------------------------------------
col_logo, col_btns = st.columns([1, 3])

with col_logo:
    logo = Image.open("Resources/NBMLogoNobg_cropped.png")
    st.image(logo, width=150)

with col_btns:
    b1, b2, b3, b4 = st.columns(4)

    with b1:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        st.button("Button 1")
        st.markdown('</div>', unsafe_allow_html=True)

    with b2:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        st.button("Button 2")
        st.markdown('</div>', unsafe_allow_html=True)

    with b3:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        st.button("Button 3")
        st.markdown('</div>', unsafe_allow_html=True)

    with b4:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        st.button("Button 4")
        st.markdown('</div>', unsafe_allow_html=True)


# ------------------------------------------------------
# CONTENT
# ------------------------------------------------------
st.markdown("## **NeuroBioMark**")

st.write("""
Welcome to NeuroBioMark, your comprehensive platform for exploring the
intersection of neuroscience and biometrics.

Our mission is to provide researchers, clinicians, and enthusiasts with
insights, tools, and resources to advance the understanding of neurological
biomarkers and their applications in diagnosis, treatment, and research.
""")
