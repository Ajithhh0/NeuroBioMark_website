import streamlit as st

def render(encoded):

    # ---- PAGE BACKGROUND ----
    st.markdown(
        f"""
        <style>
        html, body, .stApp {{
            background-color: #000000 !important;
        }}

        /* Responsive brain image with gradient overlay */
        [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(to bottom, rgba(0,0,0,0.85), rgba(0,0,0,0.45)),
                url("data:image/jpg;base64,{encoded}");
            background-size: clamp(350px, 70vw, 1200px) auto;
            background-position: center top;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # ---- MAIN CONTENT ----
    st.markdown(
        """
<div class="bg-box fade-in">

<h2>Background</h2>

<div class="section-title">What is ALS?</div>
<p>
Amyotrophic Lateral Sclerosis (ALS) is a progressive neurodegenerative disease
that affects nerve cells in the brain and spinal cord. It leads to muscle weakness,
loss of motor function, and eventually respiratory failure. The exact cause of ALS
is unknown, and there is currently no cure.
</p>

<div class="section-divider"></div>

<div class="section-title">The Need for Early Diagnosis</div>

<p>Early diagnosis of ALS is crucial for:</p>

<ul> 
    <li>Starting treatments sooner to potentially slow disease progression.</li>
    <li>Improving quality of life through symptom management.</li>  
    <li>Enabling patients to participate in clinical trials for new therapies.</li>
</ul>

<p>However, diagnosing ALS early is challenging due to:</p>

<ul>    
    <li>Symptom overlap with other neurological conditions.</li>
    <li>Lack of definitive diagnostic tests.</li>
    <li>Variability in disease presentation among patients.</li>
</ul>

<div class="section-divider"></div>

<div class="section-title">What Are Neurological Biomarkers?</div>

<p>
Neurological biomarkers are measurable indicators that reflect changes in brain structure,
function, or physiology. They can be derived from:
</p>

<ul>
    <li>Brain imaging (MRI, CT, PET)</li>
    <li>Signals (EEG, EMG)</li>
    <li>Biological samples (blood, CSF)</li>
    <li>Digital features (speech, gait, facial analysis)</li>
    <li>Tongue images and emerging modalities</li>
</ul>

<div class="section-divider"></div>

<div class="section-title">Why Biomarkers Matter</div>

<p>
Neurodegenerative diseases such as ALS, Alzheimer’s, Parkinson’s, and FTD present major diagnostic challenges:
</p>

<ul>
    <li><b>Late Diagnosis</b> — Symptoms appear only after major neuron loss.</li>
    <li><b>No Definitive Tests</b> — Diagnosis often relies on clinical judgement.</li>
    <li><b>Hidden Symptoms</b> — Cognitive or behavioural changes may go unnoticed.</li>
</ul>

<div class="section-divider"></div>

<div class="section-title">Why explainability is crucial?</div>

<div class="callout">
<b>Medical AI must be trusted.</b> Clinicians will not act on a prediction unless the reasoning behind it is clear.
Explainability builds confidence and enables clinical adoption.
</div>

<ul>

  <li><b>Black-box decisions are unsafe</b> – A model may be accurate but focus on irrelevant features.</li>

  <li><b>Validates biological relevance</b> – Ensures model decisions are based on true pathological patterns.</li>

  <li><b>Supports clinical reasoning</b> – Allows pathologists to compare AI outputs with known disease markers.</li>

  <li><b>Essential for regulatory approval</b> – Medical AI must provide:
    <ul>
      <li>auditability</li>
      <li>transparency</li>
      <li>risk assessment</li>
      <li>regulatory compliance</li>
    </ul>
  </li>

  <li><b>Model improvement</b> – Explainability highlights failure points, enabling:
    <ul>
      <li>better training</li>
      <li>better data selection</li>
      <li>safer model refinement</li>
    </ul>
  </li>

  <li><b>Critical for patient safety</b> – Reduces risks of biased and unpredictable decisions.</li>

</ul>

<div class="section-divider"></div>

<div class="section-title">Challenges & Opportunity</div>

<ul>
    <li>Voice</li>
    <li>Movement</li>
    <li>Physiological signals</li>
    <li>Tongue images</li>
</ul>

<p>Challenges include:</p>
<ul>
    <li>Limited interpretability</li>
    <li>Small or inconsistent datasets</li>
    <li>Need for clinical validation</li>
    <li>Ethical and privacy concerns</li>
</ul>

<div class="section-divider"></div>

<div class="section-title">Diagnostic Software Overview</div>

<p>
Our diagnostic assistant is a clinician-friendly software platform designed to support ALS
detection using TDP-43 stained histopathology images. It integrates deep learning with
explainability and pathology validation to provide transparent, clinically meaningful outputs.
</p>

</div>

<style>

/* ---- RESPONSIVE GLASS BOX ---- */
.bg-box {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    padding: clamp(20px, 4vw, 60px);
    border-radius: 18px;
    width: 95%;
    max-width: 1200px;
    margin: clamp(80px, 12vh, 130px) auto clamp(40px, 12vh, 60px) auto;
    color: white;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.45);
    font-size: clamp(15px, 1.2vw, 19px);
    line-height: 1.75;
    animation: fadeIn 1.1s ease-out forwards;
    opacity: 0;
}

/* ---- TITLES ---- */

h2 {
    font-size: clamp(26px, 3vw, 40px);
    margin-bottom: 20px;
}

.section-title {
    font-size: clamp(20px, 2vw, 28px);
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 12px;
    color: #00eaff;
    padding-left: 14px;
    position: relative;
}

.section-title::before {
    content: "";
    position: absolute;
    left: 0;
    top: 4px;
    width: 5px;
    height: 22px;
    background: #00eaff;
    border-radius: 3px;
}

/* ---- DIVIDERS ---- */

.section-divider {
    width: 100%;
    height: 2px;
    background: rgba(0, 255, 255, 0.25);
    margin: 40px 0;
    border-radius: 3px;
}

/* ---- LISTS ---- */

ul {
    margin-left: clamp(20px, 4vw, 40px);
}

ul li {
    margin-bottom: clamp(6px, 1.2vw, 14px);
}

/* ---- CALLOUT ---- */

.callout {
    background: rgba(0, 255, 255, 0.08);
    border-left: 4px solid #00eaff;
    padding: 16px 20px;
    border-radius: 6px;
    margin: 18px 0;
}

/* ---- FADE IN ANIMATION ---- */

@keyframes fadeIn {
    0%   { opacity: 0; transform: translateY(25px); }
    100% { opacity: 1; transform: translateY(0); }
}

</style>
        """,
        unsafe_allow_html=True
    )
