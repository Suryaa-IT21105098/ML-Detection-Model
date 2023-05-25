import os
import streamlit as st

from file_checker import checkFile

st.title("Malware Detection using Random Forest Algorithm")

st.markdown("""This is a python program for detecting whether a given file is a probable malware or not!""")

st.subheader("Try yourself:-")

file = st.file_uploader("Upload a file to check for malwares:", accept_multiple_files=True)
if len(file):
    with st.spinner("Checking..."):
        for i in file:
            open('malwares/tempFile', 'wb').write(i.getvalue())
            legitimate = checkFile("malwares/tempFile")
            os.remove("malwares/tempFile")
            if legitimate:
                st.write(f"File {i.name} seems *LEGITIMATE*!")
            else:
                st.markdown(f"File {i.name} is probably a **MALWARE**!!!")
