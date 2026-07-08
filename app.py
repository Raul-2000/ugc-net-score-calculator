import streamlit as st
from nta import calculate_score

# Set up the page layout
st.set_page_config(page_title="UGC NET Score Calculator", page_icon="📝", layout="centered")

st.title("📝 UGC NET Score Calculator")
st.markdown("Automate your score calculation. Upload your response sheet and the official answer key below.")

# Create columns for a cleaner UI layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Response Sheet")
    response_pdf = st.file_uploader("Upload your attempted paper (PDF)", type="pdf", key="response")

with col2:
    st.subheader("2. Answer Key")
    answer_key_pdf = st.file_uploader("Upload the official key (PDF)", type="pdf", key="key")

st.divider()

# Only show the button if both files are uploaded
if response_pdf and answer_key_pdf:
    if st.button("Calculate My Score", type="primary", use_container_width=True):
        
        # Show a loading spinner while your Python code runs
        with st.spinner("Parsing PDFs and calculating scores... This may take a few seconds."):
            try:
                # Call your backend logic
                result_excel_buffer = calculate_score(response_pdf, answer_key_pdf)
                
                st.success("✅ Calculation Complete!")
                
                # Provide the download button for the in-memory Excel file
                st.download_button(
                    label="📊 Download Result.xlsx",
                    data=result_excel_buffer,
                    file_name="UGC_NET_Result.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"An error occurred while processing the files. Please ensure they are the correct UGC NET PDFs. Details: {e}")
else:
    st.info("👆 Please upload both PDF files to begin.")
