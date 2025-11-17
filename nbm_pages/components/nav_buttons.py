import streamlit as st
from PIL import Image
import base64

def nav_buttons():
    current = st.session_state.get("active_page", "Home")

    # Load logo and convert to base64 (required for inside HTML)
    with open("Resources/NBMLogoNobg_cropped.png", "rb") as f:
        logo_data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
<style>
.nav-wrapper {{
    position: sticky;
    top: 0;
    z-index: 9999;
    padding: 10px 0;
    background: black;  /* navbar background */
}}

.nav-container {{
    display: flex;
    gap: 35px;
    align-items: center;
}}

.nav-logo {{
    height: 48px;
    margin-right: 20px;
}}

.nav-btn {{
    background: transparent;
    color: white;
    font-size: 18px;
    padding: 6px 6px;
    cursor: pointer;
    position: relative;
    text-decoration: none !important;
}}

.nav-btn:link,
.nav-btn:visited,
.nav-btn:hover,
.nav-btn:active {{
    text-decoration: none !important;
}}

/* Hover underline animation */
.nav-btn::after {{
    content: "";
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 0%;
    height: 2px;
    background: white;
    transition: width 0.25s ease-out;
}}

.nav-btn:hover::after {{
    width: 100%;
}}

/* Active page */
.active {{
    color: #00f3ff !important;
    font-weight: 700;
}}

.active::after {{
    width: 0 !important;
    height: 0 !important;
}}
</style>

<div class="nav-wrapper">
    <div class="nav-container">
        <img class="nav-logo" src="data:image/png;base64,{logo_data}">
        <a class="nav-btn {'active' if current=='Home' else ''}" href="/?page=Home" target="_self">Home</a>
        <a class="nav-btn {'active' if current=='Page2' else ''}" href="/?page=Page2" target="_self">Background</a>
        <a class="nav-btn {'active' if current=='Page3' else ''}" href="/?page=Page3" target="_self">Research</a>
        <a class="nav-btn {'active' if current=='Page4' else ''}" href="/?page=Page4" target="_self">Team</a>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )
