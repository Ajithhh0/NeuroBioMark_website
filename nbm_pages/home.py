import streamlit as st

def render(encoded):

    # --- TRUE BLACK BACKGROUND ---
    st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- BACKGROUND IMAGE (RESTORED TO ORIGINAL WORKING LAYER) ---
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: 70% auto;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- CONTENT BOX (UNCHANGED) ---
    st.markdown(
        """
        <div class="content-box fade-in">
            <h2>NeuroBioMark</h2>
            <p>
                Welcome to NeuroBioMark, your comprehensive platform for exploring 
                the intersection of neuroscience and biometrics.
                <br><br>
                Our mission is to provide researchers, clinicians, and enthusiasts 
                with insights, tools, and resources to advance the understanding of 
                neurological biomarkers and their applications in diagnosis, 
                treatment, and research.
            </p>
        </div>

        <style>
        /* Fade-in Animation */
        @keyframes fadeInAnim {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .fade-in {
            animation: fadeInAnim 0.8s ease-out;
        }

        .content-box {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 25px 35px;
            border-radius: 14px;
            width: 70%;
            margin: 120px auto 50px auto;
            color: white;
            box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.35);
        }

        .content-box h2 {
            font-weight: 700;
            margin-bottom: 15px;
        }

        .content-box p {
            font-size: 16px;
            line-height: 1.6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
