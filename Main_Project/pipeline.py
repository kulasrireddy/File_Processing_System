import pandas as pd
from parallel_text_processor import parallel_process
from database.database import insert_review

def run_pipeline(lines):
    results = parallel_process(lines)

    # 4 columns
    df = pd.DataFrame(results, columns=["Text", "Score", "Sentiment", "Category"])

    for row in results:
        insert_review(row[0], row[1], row[2], row[3])

    return df