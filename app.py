import streamlit as st
from nta import calculate_score

# 1. Set up the page layout and default theme
st.set_page_config(page_title="UGC NET Score Calculator", page_icon="🎓", layout="centered")

# 2. Inject Custom CSS for the "Futuristic NTA" aesthetic
st.markdown("""
<style>
    /* Light, clean background to make the blue/orange pop */
    .stApp {
        background-color: #f4f7f9;
    }

    /* Neo-Generation Header: Deep Navy Blue Gradient */
    .neo-header {
        background: linear-gradient(135deg, #001f3f, #003366, #00509e);
        padding: 30px;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 51, 102, 0.3);
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .neo-header h1 {
        margin: 0;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
        color: #ffffff;
    }
    
    .neo-header p {
        margin: 5px 0 0 0;
        font-size: 1.1rem;
        color: #e0e0e0;
        font-weight: 300;
    }

    /* Upload Box Styling (Sleek and rounded) */
    div[data-testid="stFileUploader"] {
        background: #ffffff;
        border: 2px dashed #00509e;
        border-radius: 16px;
        padding: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stFileUploader"]:hover {
        border-color: #ff9900;
        background: #fffcf9;
        box-shadow: 0 6px 20px rgba(255, 153, 0, 0.15);
    }

    /* Futuristic Action Button (NTA Orange Gradient) */
    .stButton>button {
        background: linear-gradient(90deg, #ff8c00, #ffb347);
        color: white !important;
        font-weight: bold;
        font-size: 1.1rem;
        border: none;
        border-radius: 50px; /* Pill shape */
        padding: 12px 0;
        box-shadow: 0 8px 20px rgba(255, 140, 0, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(255, 140, 0, 0.5);
        background: linear-gradient(90deg, #ff9d2e, #ffc061);
    }
    
    /* Subheaders */
    h3 {
        color: #003366;
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
