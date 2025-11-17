import streamlit as st
import base64

st.set_page_config(page_title="NeuroBioMark", layout="wide")

# --- GLOBAL BLACK BACKGROUND (loads instantly) ---
st.markdown("""
<style>
html, body, .stApp {
    background-color: black !important;
}
</style>
""", unsafe_allow_html=True)

# --- HIDE STREAMLIT DEFAULT UI ---
st.markdown("""
<style>
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}
.block-container {padding-top: 0 !important;}
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)


# ========== EAGER LOAD BACKGROUND IMAGE ==========
@st.cache_resource
def load_bg_image():
    with open("Resources/brainbg.jpg", "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

BG_IMAGE = load_bg_image()
# =================================================


# --- IMPORTS MUST COME AFTER BG_IMAGE LOAD ---
from nbm_pages.home import render as home_render
from nbm_pages.page2 import render as page2_render
from nbm_pages.page3 import render as page3_render
from nbm_pages.page4 import render as page4_render
from nbm_pages.components.nav_buttons import nav_buttons


# --- READ QUERY PARAMS ---
params = st.query_params
page = params.get("page", "Home")

# Store active page in session
st.session_state.active_page = page

# Navbar — now safe to render
nav_buttons()


# --- PAGE ROUTING (PASS BG_IMAGE TO EACH PAGE) ---
if page == "Home":
    home_render(BG_IMAGE)
elif page == "Page2":
    page2_render(BG_IMAGE)
elif page == "Page3":
    page3_render(BG_IMAGE)
elif page == "Page4":
    page4_render(BG_IMAGE)
else:
    home_render(BG_IMAGE)
