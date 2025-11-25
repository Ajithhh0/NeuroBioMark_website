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

<h2>Research</h2>

<div class="section-title">Dataset Overview</div>
The dataset consists of TDP-43–stained post-mortem histopathology images from frontal cortex regions associated with motor and cognitive function.
Specifically: 
 <ul> 
  <li> Brodmann Area 44 (BA44) </li>
  <li> Brodmann Area 46 (BA46) </li>
 </ul>

These regions are chosen because they are linked to both ALS motor pathology and FTD-related cognitive decline.

<b> Sample Size:</b> 190 original brain tissue images.

<b> Output Classes:</b> 
<ul> 
 <li> <b> Control </b> – No ALS </li>
 <li> <b> Discordant </b> – ALS without cognitive impairment </li>
 <li> <b> Concordant </b> – ALS with cognitive impairment </li>
</ul>
These labels support both flat 3-class classification and the proposed hierarchical approach (ALS detection → cognitive stratification).

<div class="section-title">Data Augmentation</div>
To expand the dataset and reduce overfitting, a large augmentation pipeline is applied:
<ul> 
 <li> 15 augmentation techniques </li>
 <li> Applied across 5 cross-validation folds, creating
      190 × 10 = 1,900 images per fold </li>
</ul>
Best techniques identified: 
<ul> 
 <li> Horizontal flip </li>
 <li> Brightness/contrast adjustments </li>
 <li> Shift-scale-rotate </li>
 <li> Elastic deformation </li>
 <li> Colour jitter </li>
</ul>

<div class="section-title">Data Preprocessing</div>
Standard preprocessing steps include:
<ul>
<li> ImageNet Normalization </li>
<li> Resizing and formatting for model input </li>
<li> Removal of patient-level data leakage </li>
</ul>

<div class="section-title">Cross-Validation Strategy</div>
To ensure robust and unbiased performance estimation:
<ul>
 <li> 5-fold cross-validation  </li>
 <li> 5 Group-CV (patient-level grouping) </li>
 <li> Leave-One-Group-Out (LOGO) validation </li>
</ul>

These strategies guarantee that images from the same patient never appear in both training and testing sets.

<div class="section-title">Biological Annotation</div>
To verify bilogical relevance: 
<ul>
 <li> QuPath software used to annotate TDP-43–positive regions </li>
 <li> These ROI masks are used for: </li>
   <ul> 
    <li> super-pixel analysis </li>
    <li> Focus Relevance Score computation </li>
   </ul>
</ul>

<div class="section-title">Performance Metrics</div>
<div class="section-title">Visualisation</div>
<div class="section-title">Focus Relevance Score</div>
The Focus Relevance Score (FRS) quantifies how well the model's attention aligns with biologically relevant regions annotated in QuPath. It is calculated as the ratio of the area of overlap between the model's activation map and the QuPath-defined ROIs to the total area of the activation map. A higher FRS indicates that the model is focusing on clinically meaningful features, enhancing trustworthiness and interpretability.

<div class="section-title">Results</div>

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
