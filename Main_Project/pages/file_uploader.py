import streamlit as st
import pandas as pd
from module.loader import read_file
from pipeline import run_pipeline
from database.database import create_tables

st.title("File Upload & Processing")

create_tables()

uploaded_file = st.file_uploader("Upload File", type=["txt", "csv", "xlsx", "pdf", "docx"])

if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()
    content = read_file(uploaded_file.name, uploaded_file.read(), ext)

    if isinstance(content, pd.DataFrame):
        lines = content.astype(str).agg(" ".join, axis=1).tolist()
    else:
        lines = content.splitlines()

    st.write("Total Lines:", len(lines))

    if st.button("Start Processing"):
        df = run_pipeline(lines)
        st.session_state["data"] = df
        st.success("Processing Completed")