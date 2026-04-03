import streamlit as st

st.title("Results & Filter")

if "data" not in st.session_state:
    st.warning("No data")
else:
    df = st.session_state["data"]

    sentiment_filter = st.selectbox(
        "Filter by Sentiment",
        ["All"] + list(df["Sentiment"].unique())
    )

    if sentiment_filter != "All":
        filtered = df[df["Sentiment"] == sentiment_filter]
    else:
        filtered = df

    st.write(filtered)
    st.session_state["filtered"] = filtered