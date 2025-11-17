import streamlit as st

def render(encoded):

    st.markdown("<div style='height:70px'></div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: black !important;
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: 70% auto;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='color:white; font-weight:700;'>Team</h2>",
        unsafe_allow_html=True
    )
