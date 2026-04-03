import streamlit as st
import matplotlib.pyplot as plt

st.title("Insights Dashboard")

if "data" not in st.session_state:
    st.warning("No data available")
else:
    df = st.session_state["data"]

    sentiment_counts = df["Sentiment"].value_counts()

    # Color map
    colors = {
        "Strong Positive": "darkgreen",
        "Positive": "green",
        "Neutral": "gray",
        "Negative": "orange",
        "Strong Negative": "red",
        "Spam": "purple",
        "Scam": "black",
        "Sarcasm": "blue"
    }

    color_list = [colors.get(s, "gray") for s in sentiment_counts.index]

    # -------- BAR CHART --------
    st.subheader("Sentiment Bar Chart")
    fig1 = plt.figure()
    plt.bar(sentiment_counts.index, sentiment_counts.values, color=color_list)
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # -------- PIE CHART --------
    st.subheader("Sentiment Pie Chart")
    fig2 = plt.figure()
    plt.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%', colors=color_list)
    plt.axis("equal")
    st.pyplot(fig2)

    # -------- CATEGORY BAR CHART --------
    st.subheader("Category Bar Chart")
    cat_counts = df["Category"].value_counts()

    fig3 = plt.figure()
    plt.bar(cat_counts.index, cat_counts.values)
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig3)