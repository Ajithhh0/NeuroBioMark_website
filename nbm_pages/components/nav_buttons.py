import streamlit as st
import base64


def nav_buttons():
    current = st.session_state.get("active_page", "Home")

    with open("Resources/NBMLogoNobg_cropped.png", "rb") as f:
        logo_data = base64.b64encode(f.read()).decode()

    def cls(page):
        return "nav-btn active" if current == page else "nav-btn"

    html = f"""
<style>
.nav-wrapper {{
    position: sticky;
    top: 0;
    z-index: 9999;
    height: 70px;
    width: 100%;
    background: black;
}}
.nav-container {{
    position: relative;
    height: 100%;
    width: 100%;
}}
.nav-left {{
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
}}
.nav-center {{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    gap: 40px;
}}
.nav-logo {{
    height: 48px;
}}
.nav-btn {{
    background: transparent;
    color: white;
    font-size: 18px;
    cursor: pointer;
    text-decoration: none !important;
    position: relative;
    padding: 6px 6px;
}}
.nav-btn::after {{
    content: "";
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 0%;
    height: 2px;
    background: white;
    transition: width 0.25s ease;
}}
.nav-btn:hover::after {{
    width: 100%;
}}
.active {{
    color: #00f3ff !important;
    font-weight: 700;
}}
.active::after {{
    width: 0 !important;
}}
</style>

<div class="nav-wrapper">
<div class="nav-container">
<div class="nav-left">
<img class="nav-logo" src="data:image/png;base64,{logo_data}">
</div>

<div class="nav-center">
<a class="{cls("Home")}" href="?page=Home" target="_self">Home</a>
<a class="{cls("Background")}" href="?page=Background" target="_self">Background</a>
<a class="{cls("Research")}" href="?page=Research" target="_self">Research</a>
<a class="{cls("Team")}" href="?page=Team" target="_self">Team</a>


</div>

</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)