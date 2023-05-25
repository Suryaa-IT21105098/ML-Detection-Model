import os
import streamlit as st

from file_checker import checkFile

# Set custom styles
st.set_page_config(
    page_title="Malware Detection",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="auto"
)

# Define custom CSS styles
st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 800px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}
        .streamlit-file_uploader{{
            padding: 1rem;
            border: 2px dashed #ddd;
            border-radius: 5px;
        }}
        .streamlit-button.primary-button{{
            background-color: #702963;
            border-color: #702963;
            color: white;
        }}
        .streamlit-button.primary-button:hover{{
            background-color: #874f82;
            border-color: #874f82;
        }}
        .streamlit-button.warning-button{{
            background-color: #D70040;
            border-color: #D70040;
            color: white;
        }}
        .streamlit-button.warning-button:hover{{
            background-color: #f74767;
            border-color: #f74767;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Malware Detection using Random Forest Algorithm")

st.markdown("""
This is a Python program for detecting whether a given file is a probable malware or not!
""")

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
