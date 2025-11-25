import streamlit as st

def render(encoded):

  
    st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
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
        """
<div class="bg-box fade-in">

<h2>Background</h2>

<div class="section-title">What is ALS?</div>
Amyotrophic Lateral Sclerosis (ALS) is a progressive neurodegenerative
disease that affects nerve cells in the brain and spinal cord. 
It leads to muscle weakness, loss of motor function, and eventually respiratory failure.
The exact cause of ALS is unknown, and there is currently no cure.

<div class="section-title">The Need for Early Diagnosis</div>
Early diagnosis of ALS is crucial for:
<ul> 
    <li>Starting treatments sooner to potentially slow disease progression.</li>
    <li>Improving quality of life through symptom management.</li>  
    <li>Enabling patients to participate in clinical trials for new therapies.</li>
</ul>
However, diagnosing ALS early is challenging due to:
<ul>    
    <li>Symptom overlap with other neurological conditions.</li>
    <li>Lack of definitive diagnostic tests.</li>
    <li>Variability in disease presentation among patients.</li>
</ul>

<div class="section-title">What Are Neurological Biomarkers?</div>
Neurological biomarkers are measurable indicators that reflect changes 
in brain structure, function, or physiology. They can be derived from:
<ul>
    <li>Brain imaging (MRI, CT, PET)</li>
    <li>Signals (EEG, EMG)</li>
    <li>Biological samples (blood, CSF)</li>
    <li>Digital features (speech, gait, facial analysis)</li>
    <li>Tongue images and other emerging modalities</li>
</ul>
These biomarkers enable earlier and more objective detection of 
neurological conditions.

<div class="section-title">Why Biomarkers Matter</div>
Neurodegenerative diseases such as ALS, Alzheimer’s, Parkinson’s, 
and FTD present major diagnostic challenges:
<ul>
    <li><b>Late Diagnosis</b> — Symptoms appear only after major neuron loss.</li>
    <li><b>No Definitive Tests</b> — Diagnosis often relies on clinical judgement.</li>
    <li><b>Hidden Symptoms</b> — Cognitive or behavioural changes may go unnoticed.</li>
</ul>
Biomarkers help detect these changes earlier and with better accuracy.



<div class="section-title">Why explainability is crucial?</div>
<ul>

  <li><b>Medical AI must be trusted</b> – Clinicians will not act on a prediction unless the reasoning behind it is clear. Explainability builds confidence and enables clinical adoption.</li>

  <li><b>Black-box decisions are unsafe</b> – A model may achieve high accuracy yet still focus on irrelevant or misleading features. Explainability helps detect and prevent errors that could harm patients.</li>

  <li><b>Validates biological relevance</b> – Explainability ensures that model decisions are grounded in true pathological signals, such as TDP-43–positive regions identified through Grad-CAM/Layer-CAM and QuPath-defined ROIs. This confirms that predictions arise from meaningful biological features rather than noise or artefacts.</li>

  <li><b>Supports clinical reasoning</b> – Explainability allows pathologists to compare AI-highlighted regions with known disease markers, making the system a supportive tool rather than a black box.</li>

  <li><b>Essential for regulatory approval</b> – Medical AI must provide interpretable outputs for:
    <ul>
      <li>auditability</li>
      <li>transparency</li>
      <li>risk assessment</li>
      <li>compliance with medical device standards</li>
    </ul>
  </li>

  <li><b>Enables error analysis and model improvement</b> – When misclassifications occur, explainability reveals where they arise, supporting:
    <ul>
      <li>better training</li>
      <li>better data selection</li>
      <li>safer model refinement</li>
    </ul>
  </li>

  <li><b>Critical for patient safety</b> – Transparent models reduce the risks of:
    <ul>
      <li>biased decisions</li>
      <li>misclassification</li>
      <li>unpredictable behaviour</li>
    </ul>
    Ensuring attention to clinically meaningful regions protects patients.
  </li>

<div class="section-title">Challenges & Opportunity</div>
AI enables extraction of subtle, clinically relevant patterns from:
<ul>
    <li>Voice</li>
    <li>Movement</li>
    <li>Physiological signals</li>
    <li>Tongue images</li>
</ul>

Despite this potential, challenges include:
<ul>
    <li>Limited interpretability</li>
    <li>Small or inconsistent datasets</li>
    <li>Need for clinical validation</li>
    <li>Ethical and privacy concerns</li>
</ul>
</ul>
<div class="section-title">Diagnostic Software Overview</div>

The NeuroBioMark diagnostic assistant is a clinician-friendly software platform designed to support ALS detection and cognitive subtype stratification using TDP-43–stained histopathology images. The system integrates deep learning predictions with explainability and pathology validation to provide transparent, interpretable, and clinically meaningful outputs.

<br>Key Features:</br>
<ul>    
  <li> <b> Image Upload & Preview: </b> The software allows users to load high-resolution TDP-43 histopathology slides from Brodmann areas BA44/BA46. Images are automatically preprocessed using the same pipeline applied during model training, ensuring consistent and reliable inference. </li>
  <li> <b> AI-Driven Prediction with Confidence Scores: </b> The integrated deep learning model (DenseNet121 + SE Attention) produces: 
    <ul> 
        <li> ALS vs Control classification, and </li>
        <li> Cognitive subtype stratification (Concordant vs Discordant). </li>
    </ul> Prediction probabilities are displayed as intuitive confidence bars to support clinical interpretation. </li>
   <li> Explainability Integration (Layer-CAM / Grad-CAM): The software generates class-activation heatmaps that highlight regions most influential in the model’s decision. These heatmaps allow: 
    <ul> 
     <li> verification of model focus, </li>
     <li> comparison with known disease markers, and </li> 
     <li> improved transparency for diagnostic decision-making. </li>
    </ul>
      </li>
   <li> <b> QuPath ROI Overlay: </b> To validate biological relevance, the system overlays QuPath-defined regions of interest (TDP-43–positive areas) onto the image.
   This alignment ensures model attention corresponds to genuine pathological structures rather than artefacts or irrelevant tissue. </li> 
   <li> <b> Focus Relevance Score (FRS): </b> The FRS quantifies the overlap between the model’s activation regions and QuPath-derived pathological ROIs.
   This metric provides a numerical assessment of how clinically meaningful the model’s attention is, strengthening trust in the prediction. </li>
   <li> <b> User Interface Designed for Clinical Settings: </b>
   Built in PySide6, the interface is designed for: 
    <ul>  
    <li> mouse-only navigation, </li>
    <li> large, readable components, </li>
    <li> minimal cognitive load for lab technicians and clinicians, </li>
    <li> quick review of multiple images. </li>
    </ul> 
    The clean layout allows users to switch rapidly between:
    <ul>  
    <li> raw images </li>
    <li> activation maps </li>
    <li> QuPath annotations </li>
    <li> prediction outputs </li>
    </ul> </li>
    <li> <b> Annotation & Metadata Panel: </b> Users can record notes, observations, or clinical comments directly within the software.
    Associated metadata—patient ID, brain region, staining method—provides essential context for each slide. </li>
    <li> <b> Exportable Reports: </b> The system can generate comprehensive reports that include:
    <ul> 
        <li> original images, </li>
        <li> activation heatmaps, </li>
        <li> QuPath overlays, </li>
        <li> prediction results, </li>
        <li> FRS values, </li>
        <li> user annotations. </li>        
    </ul> These reports facilitate documentation, case review, and integration into patient records. </li>
    
</ul>

<div class="section-title">Purpose of the Software</div> 
The platform bridges the gap between AI research and clinical pathology by converting deep learning outputs into transparent, verifiable, and actionable diagnostic information.
It supports safer, earlier, and more informed assessment of ALS and its cognitive subtypes, aligning model behaviour with biological evidence.

</div>



<style>

    @keyframes fadeInAnim {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .fade-in {
        animation: fadeInAnim 0.8s ease-out;
    }

    .bg-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 40px 50px;
        border-radius: 16px;
        width: 90%;
        margin: 120px auto 60px auto;
        color: white;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.35);
        font-size: 16px;
        line-height: 1.6;
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 10px;
        color: #00eaff;
    }

</style>
        """,
        unsafe_allow_html=True
    )
