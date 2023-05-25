import os
import streamlit as st

from file_checker import checkFile

# Set custom styles
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;
        padding: 2rem;
    }
    .stFileUploader .content.dropzone,
    .stButton button {
        background-color: #702963 !important;
        color: white !important;
    }
    .stButton button:hover {
        background-color: #874f82 !important;
    }
    .stSuccess {
        color: #702963 !important;
    }
    .stError {
        color: #D70040 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set app title and description
st.title("Malware Detection using Random Forest Algorithm")
st.markdown("""
This is a Python program for detecting whether a given file is a probable malware or not!
""")

# File uploading and processing
st.subheader("Try it yourself:")
file = st.file_uploader("Upload a file to check for malware:", accept_multiple_files=True)

if file:
    with st.spinner("Checking..."):
        for uploaded_file in file:
            temp_file_path = "malwares/tempFile"
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.getvalue())
            legitimate = checkFile(temp_file_path)
            os.remove(temp_file_path)
            if legitimate:
                st.success(f"File {uploaded_file.name} seems *LEGITIMATE*!")
            else:
                st.error(f"File {uploaded_file.name} is probably a **MALWARE**!")
