# ======================================================
# visualization/charts.py
# ======================================================
import matplotlib.pyplot as plt


def show_pie(data):
    sentiments = [row[2] for row in data]
    labels = list(set(sentiments))
    counts = [sentiments.count(l) for l in labels]

    plt.figure()
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title("Sentiment Distribution")
    plt.show()


def show_bar(data):
    sentiments = [row[2] for row in data]
    labels = list(set(sentiments))
    counts = [sentiments.count(l) for l in labels]

    plt.figure()
    plt.bar(labels, counts)
    plt.title("Sentiment Count")
    plt.show()