import streamlit as st
import base64

st.set_page_config(page_title="NeuroBioMark", layout="wide")

# ---- GLOBAL CSS (MUST BE FIRST) ----
st.markdown("""
<style>
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}

/* REMOVE TOP PADDING + SIDEBAR */
.block-container {padding-top: 0 !important;}
[data-testid="stSidebar"] {display: none !important;}

/* >>> GLOBAL BACKGROUND PURE BLACK <<< */
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"] {
    background-color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# ---- Import pages AFTER CSS ----
from nbm_pages.home import render as home_render
from nbm_pages.page2 import render as page2_render
from nbm_pages.page3 import render as page3_render
from nbm_pages.page4 import render as page4_render
from nbm_pages.components.nav_buttons import nav_buttons


# ---- Shared background image, encoded once ----
def load_background():
    with open("Resources/brainbg.jpg", "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_bg = load_background()

# ---- Read the current page from URL ----
params = st.query_params          # property, not a function
current_page = params.get("page", "Home")

st.session_state.active_page = current_page

# ---- Render NAVBAR ----
nav_buttons()

# ---- Load Selected Page (PASS encoded_bg) ----
if current_page == "Home":
    home_render(encoded_bg)
elif current_page == "Page2":
    page2_render(encoded_bg)
elif current_page == "Page3":
    page3_render(encoded_bg)
elif current_page == "Page4":
    page4_render(encoded_bg)
else:
    home_render(encoded_bg)   # default fallback
