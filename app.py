import streamlit as st
from nta import calculate_score

# 1. Set up the page layout and default theme
st.set_page_config(page_title="UGC NET Score Calculator", page_icon="🎓", layout="centered")

# 2. Inject Custom CSS for the "Cyber-Dark" aesthetic
st.markdown("""
<style>
    /* Deep dark background */
    .stApp {
        background-color: #0b0f19;
    }

    /* Neo-Header: Dark Gradient */
    .neo-header {
        background: linear-gradient(135deg, #111827, #1f2937);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
        border: 1px solid #374151;
    }
    
    .neo-header h1 {
        margin: 0;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
        color: #3b82f6; /* Bright Cyber Blue */
    }
    
    .neo-header p {
        margin: 5px 0 0 0;
        font-size: 1.1rem;
        color: #9ca3af;
        font-weight: 300;
    }

    /* Upload Box Styling (Dark and sleek) */
    div[data-testid="stFileUploader"] {
        background: #1f2937;
        border: 2px dashed #3b82f6;
        border-radius: 16px;
        padding: 15px;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stFileUploader"]:hover {
        border-color: #f97316; /* NTA Orange on hover */
        background: #374151;
    }

    /* FORCE text colors inside the uploader so it never vanishes */
    div[data-testid="stFileUploader"] * {
        color: #e5e7eb !important; 
    }

    /* Futuristic Action Button (NTA Orange Gradient) */
    .stButton>button {
        background: linear-gradient(90deg, #f97316, #fb923c);
        color: white !important;
        font-weight: bold;
        font-size: 1.1rem;
        border: none;
        border-radius: 50px; /* Pill shape */
        padding: 12px 0;
        box-shadow: 0 4px 15px rgba(249, 115, 22, 0.4);
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(249, 115, 22, 0.6);
        background: linear-gradient(90deg, #ea580c, #f97316);
    }
    
    /* Subheaders */
    h3 {
        color: #60a5fa !important;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# 3. Custom HTML Header (replaces standard st.title)
st.markdown("""
    <div class="neo-header">
        <h1>UGC-NET Score Automator</h1>
        <p>Next-Generation Evaluation Portal</p>
    </div>
""", unsafe_allow_html=True)

# 4. Create columns for a cleaner UI layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1. Response Sheet")
    response_pdf = st.file_uploader("Upload your attempted paper (PDF)", type="pdf", key="response")

with col2:
    st.markdown("### 2. Answer Key")
    answer_key_pdf = st.file_uploader("Upload the official key (PDF)", type="pdf", key="key")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Core Logic
if response_pdf and answer_key_pdf:
    if st.button("Calculate My Score", use_container_width=True):
        
        with st.spinner("Analyzing PDFs and computing score..."):
            try:
                result_excel_buffer = calculate_score(response_pdf, answer_key_pdf)
                
                st.success("✅ Calculation Complete! Your file is ready.")
                
                st.download_button(
                    label="⬇️ Download Result.xlsx",
                    data=result_excel_buffer,
                    file_name="UGC_NET_Result.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"An error occurred. Please ensure these are the correct PDFs. Details: {e}")
else:
    st.info("👆 Please upload both PDF files to unlock the calculator.")
