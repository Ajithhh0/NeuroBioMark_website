import streamlit as st
import base64
from streamlit.components.v1 import html

def load_person():
    with open("Resources/person.png", "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_person = load_person()


def render(encoded):

    page_html = f"""
    <html>
    <head>
    <style>

    body {{
        background-color: #000000 !important;
        background-image: url('data:image/jpg;base64,{encoded}');
        background-size: 70% auto;
        background-position: center;
        background-repeat: no-repeat;
    }}

    .bg-box {{
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(12px);
        padding: 40px 50px;
        border-radius: 16px;
        width: 90%;
        margin: 120px auto 60px auto;
        color: white;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.40);
    }}

    h2 {{
        margin: 0;
        padding-bottom: 20px;
        color: white;
        font-size: 34px;
    }}

    /* --- TEAM GRID --- */
    .team-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 30px;
        justify-items: center;
        margin-top: 30px;
    }}

    /* --- CARD STYLE --- */
    .card {{
        background: rgba(0,0,0,0.35);
        border-radius: 16px;
        width: 220px;
        padding: 20px;
        text-align: center;
        transition: 0.3s ease;
        border: 2px solid rgba(0,255,255,0.15);
    }}

    .card:hover {{
        transform: translateY(-6px);
        box-shadow: 0px 0px 18px rgba(0,255,255,0.45);
        border-color: rgba(0,255,255,0.7);
    }}

    .pfp {{
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: contain;
        background: rgba(255,255,255,0.2);
        padding: 10px;
        border: 3px solid rgba(0,255,255,0.4);
        transition: 0.3s ease;
    }}

    .card:hover .pfp {{
        box-shadow: 0px 0px 16px rgba(0,255,255,0.6);
        border-color: rgba(0,255,255,1);
    }}

    .name {{
        margin-top: 12px;
        font-size: 20px;
        font-weight: 700;
        color: white;
    }}

    .role {{
        font-size: 14px;
        color: #81faff;
        margin-top: 4px;
        font-weight: 600;
    }}

    .desc {{
        font-size: 13px;
        color: #d6f7ff;
        margin-top: 6px;
        line-height: 1.4;
    }}

    /* --- SOCIAL LINKS --- */
    .socials {{
        margin-top: 10px;
        display: flex;
        justify-content: center;
        gap: 12px;
    }}

    .icon {{
        width: 22px;
        height: 22px;
        filter: drop-shadow(0 0 4px rgba(0,255,255,0.7));
        transition: 0.25s ease;
    }}

    .icon:hover {{
        transform: scale(1.15);
        filter: drop-shadow(0 0 8px rgba(0,255,255,1));
    }}

    @keyframes fadeInAnim {{
        0% {{ opacity: 0; transform: translateY(20px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}

    .fade-in {{
        animation: fadeInAnim 0.8s ease-out;
    }}
    </style>
    </head>

    <body>

    <div class="bg-box fade-in">
        <h2>Team</h2>

        <div class="team-grid">

            <!-- MEMBER A -->
            <div class="card">
                <img src="data:image/png;base64,{encoded_person}" class="pfp">
                <div class="name">A</div>
                <div class="role">Lead Researcher</div>
                <div class="desc">Responsible for coordinating project direction, validating AI outputs, and ensuring scientific quality.</div>

                <div class="socials">
                    <a href="https://linkedin.com" target="_blank">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
                    </a>
                    <a href="mailto:placeholder@example.com">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/542/542689.png">
                    </a>
                </div>
            </div>

            <!-- MEMBER B -->
            <div class="card">
                <img src="data:image/png;base64,{encoded_person}" class="pfp">
                <div class="name">B</div>
                <div class="role">Machine Learning Engineer</div>
                <div class="desc">Develops and optimizes models, handles data processing, and ensures high-performance inference.</div>

                <div class="socials">
                    <a href="https://linkedin.com" target="_blank">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
                    </a>
                    <a href="mailto:placeholder@example.com">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/542/542689.png">
                    </a>
                </div>
            </div>

            <!-- MEMBER C -->
            <div class="card">
                <img src="data:image/png;base64,{encoded_person}" class="pfp">
                <div class="name">C</div>
                <div class="role">Data Scientist</div>
                <div class="desc">Handles statistical analysis, feature extraction, and dataset quality assurance.</div>

                <div class="socials">
                    <a href="https://linkedin.com" target="_blank">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
                    </a>
                    <a href="mailto:placeholder@example.com">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/542/542689.png">
                    </a>
                </div>
            </div>

            <!-- MEMBER D -->
            <div class="card">
                <img src="data:image/png;base64,{encoded_person}" class="pfp">
                <div class="name">D</div>
                <div class="role">Software Developer</div>
                <div class="desc">Implements application logic, builds interfaces, and integrates backend services.</div>

                <div class="socials">
                    <a href="https://linkedin.com" target="_blank">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
                    </a>
                    <a href="mailto:placeholder@example.com">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/542/542689.png">
                    </a>
                </div>
            </div>

            <!-- MEMBER E -->
            <div class="card">
                <img src="data:image/png;base64,{encoded_person}" class="pfp">
                <div class="name">E</div>
                <div class="role">UX / UI Designer</div>
                <div class="desc">Designs interactive interfaces and improves the user experience throughout the platform.</div>

                <div class="socials">
                    <a href="https://linkedin.com" target="_blank">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
                    </a>
                    <a href="mailto:placeholder@example.com">
                        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/542/542689.png">
                    </a>
                </div>
            </div>

        </div>
    </div>

    </body>
    </html>
    """

    html(page_html, height=1500, scrolling=True)
