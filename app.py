import streamlit as st
import nltk

# Download NLTK resources
def download_nltk_resources():
    nltk.download('stopwords')

download_nltk_resources()

import hangul
  # Import the detect function from your hangul module

st.title('Hangul PDF Detector')
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner('Processing...'):
        # Directly pass the uploaded file to the detect function
        result = hangul.detect(uploaded_file, 5)  # Assume 5 is an appropriate keyword number

    st.write('Detection Result:')
    if result:
        # Displaying structured results in a cleaner way
        for key, value in result.items():
            st.subheader(f"{key.capitalize()}:")
            if isinstance(value, dict):
                st.json(value)
            else:
                st.write(value)
    else:
        st.error("No data was returned from the detection process.")