import streamlit as st
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

st.title("Download & Email Report")

if "filtered" not in st.session_state:
    st.warning("No filtered data")
    st.stop()

df = st.session_state["filtered"]

file_name = "filtered_results.xlsx"
df.to_excel(file_name, index=False)

with open(file_name, "rb") as f:
    st.download_button("Download Excel", f, file_name=file_name)

receiver = st.text_input("Receiver Email")

if st.button("Send Email"):
    sender = "kulasrireddy@gmail.com"
    password = "hisqxokuqtbvucan"

    msg = MIMEMultipart()
    msg["Subject"] = "Sentiment Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.attach(MIMEText("Attached report", "plain"))

    with open(file_name, "rb") as f:
        part = MIMEApplication(f.read(), Name=file_name)
        part['Content-Disposition'] = f'attachment; filename="{file_name}"'
        msg.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

    st.success("Email Sent")