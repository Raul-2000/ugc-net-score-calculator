import streamlit as st
from nta import calculate_score

# 1. Page Configuration
st.set_page_config(page_title="UGC NET Score Calculator", page_icon="🎓", layout="centered")

# 2. Universal Theme Stylesheet Injection
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    .neo-header {
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        padding: 35px 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        margin-bottom: 35px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .neo-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #ffffff, #93c5fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .neo-header p {
        margin: 8px 0 0 0;
        font-size: 1.05rem;
        color: #cbd5e1 !important;
        font-weight: 400;
        opacity: 0.9;
    }

    div[data-testid="stFileUploader"] {
        background-color: var(--secondary-background-color) !important;
        border: 2px dashed var(--primary-color) !important;
        border-radius: 16px !important;
        padding: 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.25s ease-in-out !important;
    }
    
    div[data-testid="stFileUploader"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08) !important;
        border-color: #f97316 !important;
    }

    div[data-testid="stFileUploader"] * {
        color: var(--text-color) !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        color: #ffffff !important;
        font-weight: 600;
        font-size: 1.05rem;
        border: none;
        border-radius: 12px;
        padding: 14px 0;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
        transition: all 0.2s ease;
        width: 100%;
        letter-spacing: 0.3px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
        background: linear-gradient(90deg, #1d4ed8, #1e40af);
    }
    
    .block-container h3 {
        color: var(--text-color) !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        margin-bottom: 12px;
    }

    /* Summary Card Text Elements */
    .metric-card-title {
        margin: 0; 
        font-size: 0.9rem; 
        color: var(--text-color); 
        opacity: 0.85; 
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# 3. Application Header
st.markdown("""
    <div class="neo-header">
        <h1>UGC NET Score Calculator</h1>
        <p>Calculate your marks instantly using your response sheet and official answer key</p>
    </div>
""", unsafe_allow_html=True)

# 4. Input Column Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1. Response Sheet")
    response_pdf = st.file_uploader("Upload your attempted paper (PDF)", type="pdf", key="response")

with col2:
    st.markdown("### 2. Answer Key")
    answer_key_pdf = st.file_uploader("Upload the official key (PDF)", type="pdf", key="key")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Runtime Operational Logic
if response_pdf and answer_key_pdf:
    if st.button("Calculate My Score", use_container_width=True):
        with st.spinner("Analyzing data models and calculating final scores..."):
            try:
                # Unpack calculation results
                excel_bytes, score, gained, missed, corrects = calculate_score(response_pdf, answer_key_pdf)
                
                st.success("✅ Calculation Complete! Review your performance matrix below.")
                
                # 6. Live UI Metrics Block (Dynamic Theme Aware Container Rendering)
                st.markdown("### 📊 Performance Overview")
                m_col1, m_col2, m_col3 = st.columns(3)
                
                with m_col1:
                    st.markdown(f"""
                        <div style="background-color: var(--secondary-background-color); padding: 22px 15px; border-radius: 14px; border: 1px solid var(--primary-color); text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                            <p class="metric-card-title">Total Score</p>
                            <h2 style="margin: 8px 0 0 0; color: #2563eb; font-weight: 800; font-size: 1.8rem;">{score} / 300</h2>
                        </div>
                    """, unsafe_allow_html=True)
                    
                with m_col2:
                    st.markdown(f"""
                        <div style="background-color: var(--secondary-background-color); padding: 22px 15px; border-radius: 14px; border: 1px solid #10b981; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                            <p class="metric-card-title">Marks Gained</p>
                            <h2 style="margin: 8px 0 0 0; color: #10b981; font-weight: 800; font-size: 1.8rem;">+{gained}</h2>
                        </div>
                    """, unsafe_allow_html=True)
                    
                with m_col3:
                    st.markdown(f"""
                        <div style="background-color: var(--secondary-background-color); padding: 22px 15px; border-radius: 14px; border: 1px solid #ef4444; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                            <p class="metric-card-title">Marks Missed</p>
                            <h2 style="margin: 8px 0 0 0; color: #ef4444; font-weight: 800; font-size: 1.8rem;">-{missed}</h2>
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # File Export Triggers
                st.download_button(
                    label="⬇️ Download Detailed Result.xlsx",
                    data=excel_bytes,
                    file_name="UGC_NET_Result.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"An error occurred. Please ensure these are the correct PDFs. Details: {e}")
else:
    st.info("👆 Please upload both PDF files to unlock the calculator.")
