import streamlit as st

def render(encoded):

    st.markdown(f"""
    <style>
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
