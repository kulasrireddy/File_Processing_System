# File_Processing_System

## Project Overview
This project is a Parallel Text Processing and Sentiment Analysis System built using Python and Streamlit. The system processes large text datasets, performs sentiment analysis, classifies categories, and generates visual insights.

## Features
- Multi-file upload (CSV, TXT, PDF, DOCX, XLSX)
- Parallel text processing
- Rule-based NLP sentiment analysis
- Sentiment Types:
  - Strong Positive
  - Positive
  - Neutral
  - Negative
  - Strong Negative
  - Spam
  - Scam
  - Sarcasm
- Category Detection:
  - Refund
  - Delivery
  - Damage
  - Service
  - Price
  - General
- Dashboard (Bar Chart & Pie Chart)
- Filter Results
- Download Excel Report
- Send Email Report
- SQLite Database Storage

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- SQLite
- Multiprocessing

## How to Run
```bash
pip install -r requirements.txt
streamlit run Home.py
